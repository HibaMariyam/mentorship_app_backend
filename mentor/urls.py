from django.urls import path

from mentor.views import CourseDetailListAPIView, CourseListAPIView, MentorDetailsListAPIView, MentorListAPIView

urlpatterns = [
    path('mentors/',MentorListAPIView.as_view()),
    path('mentors/<int:pk>/',MentorDetailsListAPIView.as_view()),
    path('courses/',CourseListAPIView.as_view()),
    path('courses/<int:pk>/',CourseDetailListAPIView.as_view()),
 ]