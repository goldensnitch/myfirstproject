"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from boards import views
from accounts import views as accounts_views

from boards.views import GeneratePDF

from django.urls import include
from rest_framework import routers
from boards.boards_api import AssociateViewSet, UserViewSet, GroupViewSet, TimesheetViewSet, UserDetailsViewSet
from rest_framework.authtoken.views import obtain_auth_token
from tinymce import urls
from avatar import urls
from django.conf import settings
from django.conf.urls.static import static


router=routers.DefaultRouter()
router.register(r'v1/associates', AssociateViewSet)
router.register(r'v1/userdetails', UserDetailsViewSet)
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/users', UserViewSet)
router.register(r'v1/timesheets', TimesheetViewSet)



urlpatterns = [

   path('api/', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('api-authtoken/', obtain_auth_token),

   path('tinymce/', include('tinymce.urls')),
   path('avatar/', include('avatar.urls')),
   url(r'^media/avatars/', include('avatar.urls')),

   url(r'^$', auth_views.LoginView.as_view(template_name='blog-login.html'), name='bloglogin'),
   url(r'^signup/$', accounts_views.signup, name='signup'),

   url(r'^login/$', auth_views.LoginView.as_view(template_name='blog-login.html'), name='login'),
   url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

   url(r'^reset/$', auth_views.PasswordResetView.as_view(template_name='password_reset.html',
         email_template_name='password_reset_email.html',
         subject_template_name='password_reset_subject.txt'), name='password_reset'),
   url(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
      name='password_reset_done'),
   url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
      auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
      name='password_reset_confirm'),
   url(r'^reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
      name='password_reset_complete'),
   url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
       name='password_change'),
   url(r'^settings/password/done/$',
       auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
       name='password_change_done'),

   url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name ='board_topics'),
   url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),


   url(r'^aarya/$', views.aarya, name='aarya'),
   url(r'^options/$', views.options, name='options'),
   url(r'^associate/$', views.associate, name='associate'),
   url(r'^associate/new/$', views.associate_new, name='associate_new'),
   url(r'^associate/(?P<pk>\d+)/$', views.associate_details.as_view(), name='associate_details'),
   url(r'^associate/delete/(?P<pk>\d+)/$', views.AssociateDelete.as_view(), name='associate_delete'),

   url(r'^client/$', views.client, name='client'),
   url(r'^client/new/$', views.client_new, name='client_new'),
   url(r'^client/(?P<pk>\d+)/$', views.client_details.as_view(), name='client_details'),


   url(r'^associate/personal/(?P<pk>\d+)/$', views.eh_personal_info.as_view(), name='eh_personal_info'),
   url(r'^associate/contact/(?P<pk>\d+)/$', views.eh_contact_info.as_view(), name='eh_contact_info'),
   url(r'^associate/id/(?P<pk>\d+)/$', views.eh_idproof_info.as_view(), name='eh_idproof_info'),
   url(r'^associate/(?P<pk>\d+)/dependant/$', views.eh_dependant_list, name='eh_dependant_list'),
   url(r'^associate/(?P<pk>\d+)/dependant/new/$', views.eh_dependant_new, name='eh_dependant_new'),
#  url(r'^associate/(\d+)/dependant/(?P<pk>\d+)$', views.eh_dependant_info.as_view(), name='eh_dependant_info'),
   url(r'^associate/(?P<pk>\d+)/dependant/(?P<dependant_pk>\d+)/$',views.eh_dependant_info.as_view(), name='eh_dependant_info'),


   url(r'^export/AssociateExport_csv/$', views.AssociateExport_csv, name='AssociateExport_csv'),
   url(r'^export/AssociateExport_xls/$', views.AssociateExport_xls, name='AssociateExport_xls'),


   url(r'^pdf/IDCardhtml/$', views.idcard_html, name='idcard_html'),
   url(r'^pdf/IDCard/$', GeneratePDF.as_view(), name='IDcard'),


   url(r'^newlogin/$', auth_views.LoginView.as_view(template_name='newlogin.html'), name='newlogin'),
   url(r'^newsignup/$', accounts_views.newsignup, name='newsignup'),
   url(r'^newsafesignup/$', accounts_views.newsafesignup, name='newsafesignup'),

   url(r'^charts/$', views.charts, name='charts'),
   url(r'^forms/$', views.forms, name='forms'),
   url(r'^index/$', views.index, name='index'),
   url(r'^fancylogin/$', auth_views.LoginView.as_view(template_name='fancylogin.html'), name='fancylogin'),
   url(r'^tables/$', views.tables, name='tables'),
   url(r'^register/$', views.register, name='register'),

   url(r'^tables/associate/(?P<pk>\d+)/$', views.tables_associate.as_view(), name='tables_associate'),


   url(r'^admin/', admin.site.urls),

   url(r'^blog/login/$', auth_views.LoginView.as_view(template_name='blog-login.html'), name='bloglogin'),
   url(r'^blog/registration/$', accounts_views.blogregistration, name='blogregistration'),
   url(r'^blog/$', views.blogpostlist, name='blogpostlist'),
   url(r'^blog/my-posts/$', views.blogmypostlist, name='blogmypostlist'),
   url(r'^blog/create-post/$', views.blogcreatepost, name='blogcreatepost'),
   url(r'^blog/edit-post/(?P<slug>[-\w]+)/$', views.blogeditpost.as_view(), name='blogeditpost'),
   url(r'^blog/delete-post/(?P<slug>[-\w]+)/$', views.blogdeletepost.as_view(), name='blogdeletepost'),
   url(r'^blog/post/(?P<slug>[-\w]+)/$', views.blogpost, name='blogpost'),
   url(r'^blog/profile/(?P<slug>[-\w]+)/$', accounts_views.blogupdateprofile.as_view(), name='blogupdateprofile'),



]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
