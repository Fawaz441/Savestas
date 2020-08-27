from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail,send_mass_mail
from django.views.generic import View

from .forms import SignupForm

def create_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.create(username=username,
                                    first_name=first_name,
                                    email=email,)
            user.set_password(password)
            user.save()
            messages.info(request,'User successfully created')
            return redirect('emails:signup')
    else:
        form = SignupForm()
    context = {'form':form}
    return render(request,'home_page.html',context)


class SendEmail(View):
    def get(self,request):
        emails = []
        receipents = User.objects.filter(is_staff=False)
        for user in receipents:
            emails.append(user.email)
        subject = request.GET.get('subject',None)
        message = request.GET.get('message',None)

        send_mail(
            subject,message,'admin@test.com',recipient_list=emails
        )
        print(emails)
        messages.info(request,'Email sent successfully')
        return redirect('admin:auth_user_changelist')

        
