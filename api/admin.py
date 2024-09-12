from django.contrib import admin
from .models import Plan, Promo, UserSelectedPlans, User
# Register your models here.

admin.site.register(Plan)
admin.site.register(Promo)
admin.site.register(UserSelectedPlans)
admin.site.register(User)

