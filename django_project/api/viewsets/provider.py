from rest_framework import viewsets
from ford3.models.provider import Provider
from api.serializers.provider import ProviderSerializer


class ProvidersViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Return all details associated with a provider.

    list:
    Returns a list of all providers registered with OpenEdu.
    """
    queryset = Provider.active_objects.all()
    serializer_class = ProviderSerializer
