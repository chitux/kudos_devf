from django.conf.urls import url

urlpatterns = [
    url(r'^signup/$', 'company.views.signup', name='signup'),
    url(r'^home/$', 'company.views.home', name='home'),
]
