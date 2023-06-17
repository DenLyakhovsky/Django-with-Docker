from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeFormView.as_view(), name='home_form_url'),
    path('info-about-user/<int:pk>/', InfoAboutUser.as_view(), name='info_about_user'),
]
