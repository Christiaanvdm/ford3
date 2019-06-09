from rest_framework import viewsets
from ford3.models.qualification import Qualification
from api.serializers.qualification import QualificationSerializer


class QualificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
    Return all details for a qualification specified by ID.

    list:
    Returns a list of all qualifications registered with OpenEdu.
    """
    queryset = Qualification.active_objects.all()
    serializer_class = QualificationSerializer
