from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name="about"),
    path('delete/<task_id>', views.delete, name= "delete"),
    path ('complete/<task_id>', views.complete, name= "complete"),
    path ('pending/<task_id>', views.pending, name= "pending"),
    path ('edit/<task_id>',views.edit , name="edit"),  
]
