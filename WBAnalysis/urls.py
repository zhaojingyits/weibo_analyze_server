"""WBAnalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import *
from django.urls import path
# from . import weibo_spider
from . import analysis_summary
from . import login_or_register
from . import feedback_handler

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^testdb$', weibo_spider.testdb),
    url(r'^summary$', analysis_summary.get_summary),
    url(r'^login$', login_or_register.login),
    url(r'^register$', login_or_register.register),
    url(r'^change_passwd$', login_or_register.change_password),
    url(r'^feedback$', feedback_handler.do_feedback),
]
