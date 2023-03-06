from django.urls import path

from .views import CourseAPIView, EvaluationAPIView, CoursesAPIView, EvaluationsAPIView

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    path('evaluations/', EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluations/<int:pk>', EvaluationAPIView.as_view(), name='evaluation'),
]
