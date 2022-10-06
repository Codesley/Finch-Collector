from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('finches/', views.FinchesList.as_view(), name="finches_list"),
    path('finches/new/',views.FinchCreate.as_view(), name ="finch_create"),
    path('finches/<int:pk>/', views.FinchDetail.as_view(), name="finch_detail"),
    path('finches/<int:pk>/update',views.FinchUpdate.as_view(), name="finch_update"),
    path('finches/<int:pk>/delete',views.FinchDelete.as_view(), name="finch_delete"),
]