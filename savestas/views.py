from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


def activate_user(request,username):
    user = User.objects.filter(username=username)
    if user.exists():
        user = user.first()
        user.is_active = True
        user.save()
        messages.info(request,"User {} successfully activated".format(username))
        return redirect('admin:auth_user_changelist')

    
def deactivate_user(request,username):
    user = User.objects.filter(username=username)
    if user.exists():
        user = user.first()
        user.is_active = False
        user.save()
        messages.info(request,'User {} successfully deactivated'.format(username))
        return redirect('admin:auth_user_changelist')
        

class SendMailView(UserPassesTestMixin,TemplateView):
    template_name = 'admin/email_send.html'
    def test_func(self):
        return self.request.user.is_superuser
