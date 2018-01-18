from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
	url(r'^log_in/$', views.login_view, name='log_in'),
	url(r'^profile/(?P<pk>\d+)$', views.ProfileDetailView.as_view(), name='profile')
]