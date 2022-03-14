from pickle import TRUE
from django.contrib import admin
from platformdirs import user_log_dir
from authentication.models import SiteUser, Lead
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Lead
from django.contrib import messages
from django.utils.translation import ngettext

class UserAdmin(admin.ModelAdmin):

    actions = ['approve_users']

    @admin.action(description='Approve selected people as Representatives(Staff)')
    def approve_users(self, request, queryset):
        queryset.update(is_staff='True')
        messages.success(request, "Selected users were approved as Sales Representatives(Staff)")      

    exclude=('password','last_login','user_permissions',)
    list_display = ('username','email', 'first_name', 'last_name','is_staff','is_superuser',)
    # list_filter = ('is_staff', 'is_superuser')

    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class LeadA(admin.ModelAdmin): 
    # exclude=('user_id',)
    list_display=('Name','email','phone_number','user_id','Status')
    list_filter=('Status',)



admin.site.site_header= 'Leads Management Platform'
# admin.site.register(SiteUser, SiteUserAdmin)
admin.site.register(Lead,LeadA)


# admin.site.unregister(Group)



# from django.contrib.auth.models import Group
# Register your models here.

# class SiteUserAdmin(admin.ModelAdmin):
#     # fields=[
#         # "First Name",
#         # "Last Name",
#         # "Email",
#         # "Phone",
#         # "Password"

#     fieldsets = (
#         ("Basic Info",{"fields":["id","First_name", "Last_name", "email", "phone_number"]}),
#             ("Private Info", {"fields":["password", "created_at","is_approved"]})
#     )
