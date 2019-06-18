from rest_framework import serializers
from ford3.models.campus import Campus
from api.serializers.campus_event import CampusEventSerializer
from api.serializers.qualification import QualificationSerializer
from api.serializers.utilities.common_excluded_fields import CommonExcludedFields  # noqa
from ford3.models.qualification import Qualification


class CampusSerializer(serializers.ModelSerializer):
    """
    This is the campus serializer
    """
    campus_events = CampusEventSerializer(many=True)
    query = Qualification.published_objects.all()
    published_qualifications = serializers.SerializerMethodField()

    def get_published_qualifications(self, obj):
        queryset = list(Qualification.published_objects.filter(
            campus_id=obj.id).all())
        serializer = QualificationSerializer(
            many=True, read_only=True, instance=queryset)
        return serializer.data

    class Meta:
        model = Campus
        exclude = CommonExcludedFields.user_details
