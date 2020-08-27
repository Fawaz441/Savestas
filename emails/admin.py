from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Count,Sum
from django.utils import timezone




class MyUserAdmin(UserAdmin):
    change_list_template = 'admin/user_metrics.html'
    date_hierarchy = 'date_joined'
    list_display_links = ['username']

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Count('id'),
        }

        response.context_data['summary'] = list(
            qs
            .values('first_name','last_name','username','email','last_login','date_joined','is_active')
            .annotate(**metrics)
            .order_by('first_name')
        )
        last_month_users = 0
        last_month_users_list = []
        last_week_users = 0
        last_week_users_list = []
       
        for user in response.context_data['summary']:
            if (timezone.datetime.now() - user['date_joined'].replace(tzinfo=None)) <= timezone.timedelta(7):
                last_week_users +=1
                last_week_users_list.append(user['username'])
            elif (timezone.datetime.now() - user['date_joined'].replace(tzinfo=None)) <= timezone.timedelta(30):
                last_month_users+=1
                last_month_users_list.append(user['username'])
          
        response.context_data['past_week_users_count'] = last_week_users
        response.context_data['past_week_users'] = last_week_users_list
        response.context_data['past_month_users_count'] = last_month_users
        response.context_data['past_month_users'] = last_month_users_list
        return response

    

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
