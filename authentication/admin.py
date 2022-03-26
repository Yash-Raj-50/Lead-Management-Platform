from django.forms import TextInput, Textarea
from django.db import models
# from asyncio.windows_events import NULL
from dataclasses import Field
from pickle import TRUE
from attr import field
from django.contrib import admin
from django.forms import fields_for_model
from platformdirs import user_log_dir
from authentication.models import SiteUser, Lead
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Lead, LeadManager 
from django.contrib import messages
from django.utils.translation import ngettext
from .models import Profile
# from django.urls import reverse
# from django.utils.http import urlencode
# from django.utils.html import format_html

class ProfileAdmin(admin.ModelAdmin):
    exclude=('user',)

admin.site.register(Profile,ProfileAdmin,)



class UserAdmin(admin.ModelAdmin):

    actions = ['approve_users']

    @admin.action(description='Approve selected people as Representatives(Staff)')
    def approve_users(self, request, queryset):
        queryset.update(is_staff='True')
        messages.success(request, "Selected users were approved as Sales Representatives(Staff)")      

    exclude=('password','last_login','user_permissions',)
    # Field=('Profile.manager',)
    
    list_display = ('username','email', 'first_name', 'last_name','is_staff','is_superuser',)
    # list_filter = ('is_staff', 'is_superuser')

    
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name','email',)
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser')
        }),
        ('Roles & Other',{
            'fields':('groups','date_joined')
        }),
    )
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)



class LeadA(admin.ModelAdmin): 
    # exclude=('user_id',)
    list_display=('Name','email','phone_number','user_id','Status','remark',)
    list_filter=('Status',)
    list_per_page= 10
    list_editable=('Status','remark')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':20})},
    }
    def get_queryset(self, request):
        queryset = LeadManager.get_queryset(self, request)
        return queryset

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if  request.user in User.objects.filter(groups__name__in=['Representative']):
            self.exclude.append('user_id') #here!
        return super(LeadA, self).get_form(request, obj, **kwargs)

    # def view_remarks(self, obj):
    #     count = obj.person_set.count()
    #     # url = (
    #     #     reverse("admin:core_person_changelist")
    #     #     + "?"
    #     #     + urlencode({"courses__id": f"{obj.id}"})
    #     # )
    #     return format_html('<a> Students</a>',NULL, count)

    
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
