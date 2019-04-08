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


urlpatterns = [
   url(r'^$', views.home, name='home'),
   url(r'^signup/$', accounts_views.signup, name='signup'),

   url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

   url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name ='board_topics'),
   url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),


   url(r'^aarya/$', views.aarya, name='aarya'),
   url(r'^options/$', views.options, name='options'),
   url(r'^associate/$', views.associate, name='associate'),
   url(r'^associate/new/$', views.associate_new, name='associate_new'),
   url(r'^associate/(?P<pk>\d+)/$', views.associate_details.as_view(), name='associate_details'),

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


   url(r'^admin/', admin.site.urls),
]
