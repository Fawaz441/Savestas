
from django.contrib import admin
from django.urls import path,include
from .views import activate_user,deactivate_user,SendMailView

urlpatterns = [    
    path('admin/email_send/', SendMailView.as_view(),name='email_form'),
    path('admin/', admin.site.urls),
    path('',include('emails.urls')),
    path('activate_user/<username>',activate_user,name='activate_user'),
    path('deactivate_user/<username>',deactivate_user,name='deactivate_user')
]
