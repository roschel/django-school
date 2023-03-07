from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    CoursesAPIView,
    CourseAPIView,
    EvaluationAPIView,
    EvaluationsAPIView,
    CourseViewSet,
    EvaluationsViewSet
)

router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('evaluations', EvaluationsViewSet)

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    path('courses/<int:course_pk>/evaluations/', EvaluationsAPIView.as_view(), name='course_evaluations'),
    path('courses/<int:course_pk>/evaluations/<int:evaluation_pk>', EvaluationAPIView.as_view(),
         name='course_evaluation'),
    path('evaluations/', EvaluationsAPIView.as_view(), name='evaluations'),
    path('evaluations/<int:evaluation_pk>', EvaluationAPIView.as_view(), name='evaluation'),
]
