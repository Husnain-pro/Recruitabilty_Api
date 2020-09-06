from django.urls import include, path

from blog import views

urlpatterns = [
    path('api/album',views.AlbumListView.as_view()), 
    path('api/album/<pk>',views.AlbumListDetailView.as_view()), 
    
]
