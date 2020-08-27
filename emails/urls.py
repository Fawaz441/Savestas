from django.urls import path
from .views import create_user,SendEmail

app_name = 'emails'
urlpatterns = [
    path('',create_user,name='signup'),
    path('send_email',SendEmail.as_view(),name='send_email')
]