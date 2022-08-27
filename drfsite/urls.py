from django.urls import path, include, re_path

from drfsite.views import Listrest
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'data',Listrest,basename='Products')
print(router.urls)
appname='drfsite'
urlpatterns=[
   path("v1/",include(router.urls)),
   path('v1/drf_login/',include('rest_framework.urls')),
   path('v1/drf_auth/',include('djoser.urls')),
   re_path(r'^auth/',include('djoser.urls.authtoken')),
]