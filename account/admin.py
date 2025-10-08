from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User , Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email','is_superuser','is_active')
    list_filter =('email','is_superuser','is_active')
    searching_fields = ('email',)
    ordering=('email',)
    
    fieldsets = (
        ('Authentication',{
            "fields": (
                'email','password'
            ),
        }),
        ('permissions',{
            "fields": (
                'is_staff','is_active','is_superuser'
            ),
        }),
        ('group permissions',{
            "fields": (
                'groups','user_permissions'
            ),
        }),
        ('important date',{
            "fields": (
                'last_login',
            ),
        }),
    )
    add_fieldsets =(
        (None,{
            'classes': ('wide',),
            'fields': ('email','password1','password2','is_staff','is_active','is_superuser')
        }),
    )
    
class ProfileAdmine(admin.ModelAdmin):
    model = Profile
    list_display = ('id','first_name')
    
admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)
