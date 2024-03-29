from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('update/<int:pk>/', views.update, name="update"),
    path('<int:pk>/create_comment/', views.create_comment)
] 