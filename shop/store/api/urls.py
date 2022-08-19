from django.urls import path
from .rest_views import (
    town_list,
    street_list,
    shop,
)


urlpatterns = [
    path('shop/', view=shop, name='shop'),
    path('city/', view=town_list, name='town_list'),
    path('city/<town_id>/street/', view=street_list, name='street_list'),

]
