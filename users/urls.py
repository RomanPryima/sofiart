from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
        url(r'^signup/$', signup, name='signup'),
        url(r'^login/$', auth_views.login, {
                'template_name': 'login.html',
                'authentication_form': LoginForm,
                'redirect_authenticated_user': True},
            name='login'),
        url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
