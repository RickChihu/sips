"""sips URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from blog.views import blog_view
from landing.views import landing_view, login_view, logout_view, home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', landing_view, name='landing'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^home/', home, name='home'),
    url(r'^blog/', blog_view, name='blog'),
    url(r'^blog-admin/', include('blog.urls')),
    url(r'^asuntos/', include('asuntos.urls')),
    url(r'^reportes/', include('reportes.urls')),
    url(r'^agentes/', include('agentes.urls')),
    url(r'^subprocuraduria/', include('subprocuraduria.urls')),
]
