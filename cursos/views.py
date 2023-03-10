from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer

"""
API V1
"""


class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EvaluationsAPIView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()


class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(
                self.get_queryset(),
                course_id=self.kwargs.get('course_pk'),
                pk=self.kwargs.get('evaluation_pk')
            )
        return get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs.get('evaluation_pk')
        )


"""
API V2
"""
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['GET'])
    def evaluations(self, request, pk=None):
        self.pagination_class.page_size = 2
        evaluations = Evaluation.objects.filter(course_id=pk)
        page = self.paginate_queryset(evaluations)

        if page is not None:
            serializer = EvaluationSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)


class EvaluationsViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
