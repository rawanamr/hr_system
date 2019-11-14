from rest_framework import serializers

from main.models import Candidates


class CandidatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidates
        fields = ['full_name', 'date_of_birth', 'years_of_experience',
                  'department', 'resume' ]