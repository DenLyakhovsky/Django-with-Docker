from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('detail-goods/<int:pk>', DetailGoods.as_view(), name='detail_page'),
    path('form', ViewForm.as_view(), name='form_url'),
    path('info-about-user/<int:pk>/', InfoAboutUser.as_view(), name='info_about_user'),
    path('successful-form-page', SuccessfulForm.as_view(), name='successful_form_page'),

    path("<str:room_name>/", room, name="room"),
]
