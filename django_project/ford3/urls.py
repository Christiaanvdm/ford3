# coding=utf-8
from django.urls import path
from ford3.views import (
    views,
    saqa_qualifications
)
from django.conf.urls import url
from ford3.forms.qualification import (
    QualificationDetailForm,
    QualificationDurationFeesForm,
    QualificationRequirementsForm,
    QualificationInterestsAndJobsForm,
    QualificationImportantDatesForm,
)
from ford3.views.qualification_wizard import QualificationFormWizard
from ford3.forms.campus import (
    CampusDetailForm,
    CampusLocationForm,
    CampusImportantDatesForm,
    CampusQualificationsForm
)
from ford3.views.campus_wizard import CampusFormWizard
from ford3.views import (
    campus,
    provider
)


qualification_wizard = QualificationFormWizard.as_view(
    [
        QualificationDetailForm,
        QualificationDurationFeesForm,
        QualificationRequirementsForm,
        QualificationInterestsAndJobsForm,
        QualificationImportantDatesForm,
    ],
)

CAMPUS_FORMS = [
    ('campus-details', CampusDetailForm),
    ('campus-location', CampusLocationForm),
    ('campus-dates', CampusImportantDatesForm),
    ('campus-qualifications', CampusQualificationsForm)
]

campus_wizard = CampusFormWizard.as_view(CAMPUS_FORMS)

urlpatterns = [
    path('providers/<int:provider_id>',
         provider.show,
         name='show-provider'),
    path('providers/<int:provider_id>/edit',
         provider.edit,
         name='edit-provider'),
    path(
        'providers/<int:provider_id>/campus/<int:campus_id>/edit',
        campus_wizard,
        name='edit-campus'),
    path(
        'providers/<int:provider_id>/campus/<int:campus_id>',
        campus.show,
        name='show-campus'),
    path(
        'providers/<int:provider_id>/campus/create/',
        campus.create,
        name='create-campus'),

    path(
        'saqa_qualifications/search/',
        saqa_qualifications.search,
        name='search-saqa-qualifications'),

    path(
        'saqa_qualifications/create/',
        saqa_qualifications.create,
        name='create-saqa-qualification'),
    path(
        'campus/<int:campus_id>/events/create/',
        saqa_qualifications.create,
        name='create-campus-event'),

    path(
        '/'.join([
            'providers/<int:provider_id>',
            'campus/<int:campus_id>',
            'qualifications/<int:qualification_id>/edit']),
        qualification_wizard,
        name='edit-qualification'),
    path(
        '/'.join([
            'providers/<int:provider_id>',
            'campus/<int:campus_id>',
            'qualifications/<int:qualification_id>']),
        views.show_qualification,
        name='show-qualification'),
    url(r'^test_widgets/$', views.widget_examples, name='test_widgets'),
]
