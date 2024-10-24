"""
URL configuration for BimsCharity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path,include
from django.views.generic import TemplateView
from BimsCharity.userApp.views import SignUpView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings
from BimsCharity.causesApp.views import allcauseView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', allcauseView, name= 'home' ),
    path('donate/', TemplateView.as_view(template_name = 'donate.html'), name= 'donate' ),
    path('news-detail/', TemplateView.as_view(template_name = 'news-detail.html'), name= 'news-detail' ),
    path('news/', TemplateView.as_view(template_name = 'news.html'), name= 'news' ),
    re_path(r'^account/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name='signup'),
    re_path(r'^userApp/', include('BimsCharity.userApp.urls')),
    re_path(r'^causesApp/', include('BimsCharity.causesApp.urls')),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
