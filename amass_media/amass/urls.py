from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

from amass.common.views import Login, OrgListView
from amass.videos.views import ProjectCreate, ProjectUpdate, ProjectList, ProjectDetail
from longerusername.forms import AuthenticationForm

urlpatterns = patterns('',
    (r'^$', 'amass.videos.views.home'),
    (r'^home/', 'amass.videos.views.home'),
    (r'^admin/lookups/', include('ajax_select.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'^press/$', TemplateView.as_view(template_name='press.html')),
    url(r'^support/$', TemplateView.as_view(template_name='support.html')),
    url(r'^terms/$', TemplateView.as_view(template_name='terms.html')),
    url(r'^privacy/$', TemplateView.as_view(template_name='privacy.html')),

    (r'^login/$', Login.as_view(), { 'authentication_form': AuthenticationForm }),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change'),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset'),
    url(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    url(r'^password_reset_complete/$', 'django.contrib.auth.views.password_reset_complete'),
)

urlpatterns += patterns('',
    url(r'^organizations/$', OrgListView.as_view()),
    #url(r'^users/$', VideographerListView.as_view()),
    url(r'^projects/$', 'amass.videos.views.ProjectListView'),
    #url(r'^projects/$', ProjectList.as_view(), name="project_list"),
    url(r'^projects/create/$', ProjectCreate.as_view(), name="project_create"),
    url(r'^projects/edit/(?P<pk>\d+)/$', ProjectUpdate.as_view(), name="project_edit"),
    url(r'^follow/$', 'amass.videos.views.Follow'),
    (r'^messages/', include('postman.urls')),

    url(r'^messages/', include('postman.urls')),
    #url(r'^organizations/(\w+)/$', OrgDetailView.as_view()),
    #url(r'^users/(\w+)/$', VideographerDetailView.as_view()),
    url(r'^projects/detail/(?P<pk>\d+)/$', ProjectDetail.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)