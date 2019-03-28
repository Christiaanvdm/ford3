import json
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    render_to_response
)
from django.db import transaction, IntegrityError
from django.db.models import F
from django.http import HttpResponse
from ford3.models.provider import Provider
from ford3.models.campus import Campus
from ford3.models.qualification import Qualification
from ford3.forms.provider_form import ProviderForm
from ford3.models.saqa_qualification import SAQAQualification


def json_response(results):
    return HttpResponse(
        json.dumps({
            'results': results}),
        content_type='application/json')


def saqa_qualifications(request):
    if request.method != 'GET':
        return json_response([])

    query = request.GET.get('q', None)

    if query is None or len(query) == 0:
        return json_response([])

    results = SAQAQualification.search(query)

    return json_response(results)


def show_campus(request, provider_id, campus_id):
    qualif_query = Qualification.objects.filter(
        campus__id=campus_id).values(
            'id',
            'saqa_qualification__name',
            'saqa_qualification__saqa_id')

    context = {
        'campus': get_object_or_404(
            Campus,
            id=campus_id),
        'provider_id': provider_id,
        'qualifications': list(qualif_query)
    }

    return render(request, 'campus.html', context)


@transaction.atomic
def edit_provider(request, provider_id):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            new_provider = Provider.objects.filter(pk=provider_id).first()
            provider_type = form.cleaned_data['provider_type']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            physical_address_line_1 = (
                form.cleaned_data['physical_address_line_1'])
            physical_address_line_2 = (
                form.cleaned_data['physical_address_line_2'])
            physical_address_city = form.cleaned_data['physical_address_city']
            postal_address = form.cleaned_data['postal_address']
            admissions_contact_no = form.cleaned_data['admissions_contact_no']
            new_provider.provider_type = provider_type
            new_provider.telephone = telephone
            new_provider.email = email
            new_provider.physical_address_line_1 = physical_address_line_1
            new_provider.physical_address_line_2 = physical_address_line_2
            new_provider.physical_address_city = physical_address_city
            new_provider.postal_address = postal_address
            new_provider.admissions_contact_no = admissions_contact_no
            new_provider.save()

            number_of_campuses = int(request.POST['number-of-campuses'])
            try:
                with transaction.atomic():
                    for idx in range(number_of_campuses):
                        campus_name = request.POST[f'campus_name_{idx +  1}']
                        Campus.objects.create(provider=new_provider,
                                              name=campus_name)
            except IntegrityError:
                return render(request, 'provider_form.html', {'form': form})
            redirect_url = '/providers/' + str(new_provider.id)
            return redirect(redirect_url)
    else:
        form = ProviderForm(instance=Provider.objects.filter(
            pk=provider_id).first())
    return render(request, 'provider_form.html',
                  {'form': form, 'provider_id': provider_id})


def show_provider(request, provider_id):
    form_data = {}
    campus_query = Campus.objects.filter(provider__id=provider_id).annotate(
        campus_name=F('name'),
        campus_id=F('id'),
        provider_name=F('provider__name')
    )
    campus_data = campus_query.values('campus_name', 'campus_id')
    provider_name = campus_query.values('provider_name')[0]['provider_name']

    form_data['campus_list'] = list(campus_data)
    form_data['provider_name'] = str(provider_name)
    return render(request, 'provider_landing_page.html',
                  {'form_data' : form_data})


def widget_examples(request):
    return render_to_response('test_widgets.html')
