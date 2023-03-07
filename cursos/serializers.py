from rest_framework import serializers
from .models import Course, Evaluation


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Evaluation
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'grade',
            'created_at',
            'updated_at'
        )


class CourseSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # evaluations = EvaluationSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    # evaluations = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='evaluation-detail')

    # Primary Key Related Field
    evaluations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
