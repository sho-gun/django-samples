from django.urls import path
from file_upload.views import (
    FileUploadSampleView,
    SuccessView,
)

app_name = 'file_upload'

urlpatterns = [
    path('', FileUploadSampleView.as_view(), name='file_upload_sample'),
    path('success/', SuccessView.as_view(), name='success_page'),
]
