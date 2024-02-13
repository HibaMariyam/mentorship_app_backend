from rest_framework import serializers

from mentor.models import Course, CustomUser, Mentor



class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    mentor=MentorSerializer()
    class Meta:
       
        model = Course
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user