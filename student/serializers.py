from rest_framework import serializers
from .models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['id', 'first_name', 'last_name', 'address', 'city', 'age', 'phone', 'email']

