
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from mentor.models import Course, CustomUser, Mentor
from mentor.serializers import CourseSerializer, CustomUserSerializer, MentorSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class MentorListAPIView(generics.ListCreateAPIView):
    
     queryset = Mentor.objects.all()
     serializer_class = MentorSerializer

class MentorDetailsListAPIView(generics.RetrieveUpdateDestroyAPIView):
      
     queryset = Mentor.objects.all()
     serializer_class = MentorSerializer
class CourseListAPIView(generics.ListCreateAPIView):
     filter_backends=(DjangoFilterBackend,SearchFilter,OrderingFilter)
     search_fields=['mentor__full_name']
     queryset = Course.objects.all()
     serializer_class = CourseSerializer

class CourseDetailListAPIView(generics.RetrieveUpdateDestroyAPIView):
    
     queryset = Course.objects.all()
     serializer_class = CourseSerializer

class UserRegister(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if CustomUser.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid email/password combination'}, status=status.HTTP_400_BAD_REQUEST)

        # You can implement JWT token authentication here or any other authentication mechanism

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


