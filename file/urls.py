from django.urls import path

from . import views

app_name = 'file'
urlpatterns = [
    path('upload/', views.UploadFileView.as_view(), name='upfile'),
    path('', views.file_list, name='file_list'),
    path('<int:pk>/', views.delete_file, name='delete_file'),
]