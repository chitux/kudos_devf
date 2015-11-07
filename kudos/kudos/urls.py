"""kudos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from company.views import CompanySignup, CompanyHome
from employee.views import EmployeeSignup, EmployeeHome
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Company
    url(r'^company/signup/', CompanySignup.as_view(), name='company_signup'),
    url(r'^company/home', CompanyHome.as_view(), name='company_home'),

    # Employee
    url(r'^employee/signup/(?P<company_id>\d+)/(?P<invitation_code>\w+)', 
                            EmployeeSignup.as_view(), name='employee_signup'),
    url(r'^employee/home/', EmployeeHome.as_view(), name='employee_home'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
