from django.urls import path
from . import views

app_name = "animals"

urlpatterns = [
    path('upload/', views.upload_photo),
    path('animal_list/', views.animal_list),
    path('post_list/', views.post_list),
    path('post_list/<int:post_pk>', views.delete, name='delete'),
]