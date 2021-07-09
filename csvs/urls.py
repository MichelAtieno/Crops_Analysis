from django.urls import path
from .views import upload_file_view, variety_profile, index

app_name='csvs'

urlpatterns = [
    path('', index, name="index"),
    path('upload', upload_file_view, name="upload-view"),
    path('variety/<id>', variety_profile, name="variety_profile"),
]
