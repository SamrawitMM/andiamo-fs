from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User Type',
            {
                'fields':(
                    'user_type' ,
                    # 'is_driver',
                    # 'is_owner',
                )
            },
           
            
        ),
        (
            'Personal Details',
            {
                'fields':(
                    'full_name' ,
                    'phone_number',
                    # 'is_owner',
                )
            },
           
            
        ),
    )
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
