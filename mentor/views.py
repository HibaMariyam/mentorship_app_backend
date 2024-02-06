from django.shortcuts import render

from mentor.models import Course, Mentor
from mentor.serializers import CourseSerializer, MentorSerializer
from rest_framework import generics

class MentorListAPIView(generics.ListCreateAPIView):
    
     queryset = Mentor.objects.all()
     serializer_class = MentorSerializer

class MentorDetailsListAPIView(generics.RetrieveUpdateDestroyAPIView):
    
     queryset = Mentor.objects.all()
     serializer_class = MentorSerializer
class CourseListAPIView(generics.ListCreateAPIView):
    
     queryset = Course.objects.all()
     serializer_class = CourseSerializer

class CourseDetailListAPIView(generics.RetrieveUpdateDestroyAPIView):
    
     queryset = Course.objects.all()
     serializer_class = CourseSerializer


