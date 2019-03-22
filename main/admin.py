from .forms import UserProfileCreationForm, UserProfileChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from main.models import Stock, Transaction, UserProfile, NewsPost


admin.site.register(Stock)
admin.site.register(NewsPost)
admin.site.register(Transaction)


class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ['email', 'username', 'name',]
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('name', 'balance')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'name')}
         ),
    )

admin.site.register(UserProfile, UserProfileAdmin)
