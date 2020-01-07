from django.conf.urls import url, include
from ghost import models, views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ghostpost', views.PostViewSet)
# router.register(r'manufacturer', views.ManufacturerViewSet)
# router.register(r'shoetype', views.ShoeTypeViewSet)
# router.register(r'shoecolor', views.ShoeColorViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
