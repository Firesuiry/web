from django.urls import path

from . import views

app_name = 'file'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('upload/', views.UploadFileView.as_view(), name='upfile'),
    path('', views.file_list, name='file_list'),
    path('<int:pk>/', views.delete_file, name='delete_file'),
]