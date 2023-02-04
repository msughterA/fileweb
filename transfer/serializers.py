from .models import FileUploadModel
from rest_framework.serializers import ModelSerializer


class ExperimentSerializer(ModelSerializer):
    class Meta:
        model = FileUploadModel
        fields = "__all__"
