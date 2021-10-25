from django.urls import path

from . import views

urlpatterns = [
    path('', views.RadioPageView.as_view(), name='radio'),
]
