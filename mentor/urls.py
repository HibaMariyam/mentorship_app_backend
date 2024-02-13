from django.urls import path

from mentor.views import CourseDetailListAPIView, CourseListAPIView, MentorDetailsListAPIView, MentorListAPIView, UserLogin, UserRegister

urlpatterns = [
    path('mentors/',MentorListAPIView.as_view()),
    path('mentors/<int:pk>/',MentorDetailsListAPIView.as_view()),
    path('courses/',CourseListAPIView.as_view()),
    path('courses/<int:pk>/',CourseDetailListAPIView.as_view()),
    path('register/', UserRegister.as_view(), name='user_register'),
    path('login/', UserLogin.as_view(), name='user_login'),
]
 