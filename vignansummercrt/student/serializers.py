from rest_framework import serializers
from . models import student_model
class student_serializers(serializers.ModelSerializer):
    class Meta:
        model=student_model
        fields='__all__'