from django.urls import path
from .views import upload_file_view, variety_profile

app_name='csvs'

urlpatterns = [
    path('', upload_file_view, name="upload-view"),
    path('variety/<id>', variety_profile, name="variety_profile"),
]
