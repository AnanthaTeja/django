"""
URL configuration for demo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from DemoApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("s/", views.sample),
    path("t/<str:y>/", views.demo),
    path("stt/<str:sn>/<str:rol>/<int:ag>/", views.st_det),
    path("fst/", views.frst),
    path("fst/<str:jk>/<str:a>/", views.dsply),
    path("studG/", views.studG),
    path("stdP/", views.studP),
    path("bt", views.boot),
    path("re/", views.regform),
    path("stat/", views.static),
    path("boot/", views.boots),
    path("st", views.crud, name="cru"),
    path("stupd/<int:k>/", views.stupdate, name="stupd"),
    path("stdel/<int:k>/", views.stde, name="stdel"),
    path("em/", views.employee, name="em"),
    path("empup/<int:k>/", views.empupdate, name="empup"),
]
