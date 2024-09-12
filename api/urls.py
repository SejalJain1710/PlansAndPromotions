from django.urls import path
from .views import get_plans, create_plan, delete_plan, create_promo, create_selected_plan_entry
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('partners/create-plan', create_plan, name="create_plan"),
    path('partners/create-promo', create_promo, name="create_promo"),
    path('partners/delete-plan/<int:planID>', delete_plan, name="delete_plan"),

    path('users/get-plans', get_plans, name="get_plans"),
    path('users/save-selected-plan', create_selected_plan_entry, name="create_selected_plan_entry"),

]

urlpatterns = format_suffix_patterns(urlpatterns)