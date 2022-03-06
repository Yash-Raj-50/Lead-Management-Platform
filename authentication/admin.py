from django.contrib import admin
from authentication.models import SiteUser
# Register your models here.
class SiteUserAdmin(admin.ModelAdmin):
    # fields=[
        # "First Name",
        # "Last Name",
        # "Email",
        # "Phone",
        # "Password"

    fieldsets = (
        ("Basic Info",{"fields":["First_name", "Last_name", "email", "phone_number"]}),
            ("Private Info", {"fields":["password", "created_at"]})
    )
    
    

admin.site.register(SiteUser, SiteUserAdmin)