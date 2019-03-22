from .forms import UserProfileCreationForm, UserProfileChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from main.models import Stock, Transaction, UserProfile, NewsPost


admin.site.register(Stock)
admin.site.register(NewsPost)
admin.site.register(Transaction)

fieldsets = (
    (('User'), {'fields': ('username', 'email', 'name')}),
    (('Permissions'), {'fields': ('is_active', 'is_staff')}),
)

class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ['email', 'username', 'name',]



admin.site.register(UserProfile, UserProfileAdmin)
