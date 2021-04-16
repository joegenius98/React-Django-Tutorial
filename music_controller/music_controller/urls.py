"""music_controller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    # /admin/..../ sends /... -> admin.site.urls
    path('admin/', admin.site.urls),
    # whatever comes after api (after the slash) is dispatched to api folder --> urls.py
    path('api/', include('api.urls')),

    # dispatch to frontend folder --> urls.py
    path('', include('frontend.urls'))
]

'''
domain.com/hello
/hello will be sent to this file

This file with dispatch the URLs to the correct applications.
'''
