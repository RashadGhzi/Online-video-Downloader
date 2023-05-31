from django.urls import path
from core import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('facebook/', views.Facebook.as_view(), name='facebook'),
    path('youtube/', views.Youtube.as_view(), name='youtube'),
    path('download/', views.vid_download, name="download")
]
