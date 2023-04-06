from django import path
from bookmark import views

app_name = 'bookmark'


urlpatterns = [
    path('create-delete-bookmark', views.AddRemoveBookmark.as_view(), name='create-delete-bookmark'),
]