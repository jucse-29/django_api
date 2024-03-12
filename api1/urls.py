
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api1.views import CompanyViewsSet,EmployeeViewsSet

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewsSet)
router.register(r'employee',EmployeeViewsSet)

urlpatterns = [
    path('',include(router.urls))
]
