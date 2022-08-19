from django.urls import path, include


urlpatterns = [
    # REST URL
    path('api/v1/', include(('store.api.urls'))),
]
