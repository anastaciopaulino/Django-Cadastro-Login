from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('detail/<slug:slug>', views.DetailPageView.as_view(), name="detail"),
    path('novo/', views.NewPost.as_view(), name="novo"),
    ]
