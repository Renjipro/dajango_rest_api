# from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('languages', views.LanguageView)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('addnewtask/', views.TaskView),
]