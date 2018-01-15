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
        url(r'^reset/$',
            auth_views.PasswordResetView.as_view(
                template_name='password_reset.html',
                email_template_name='password_reset_email.html',
                subject_template_name='password_reset_subject.txt'
            ),
            name='password_reset'),
        url(r'^reset/done/$',
            auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
            name='password_reset_done'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
            name='password_reset_confirm'),
        url(r'^reset/complete/$',
            auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
            name='password_reset_complete'),
]
