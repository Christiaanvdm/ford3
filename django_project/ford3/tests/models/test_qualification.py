from django.test import TestCase
from ford3.tests.models.model_factories import ModelFactories


class TestQualification(TestCase):

    def test_qualification_description(self):
        new_qualification = ModelFactories.get_qualification_test_object()
        self.assertEqual(new_qualification.__str__(), 'Object Test Name')

