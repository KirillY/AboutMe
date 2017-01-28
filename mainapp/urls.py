from django.conf.urls import url
from mainapp.views import edu, main, work, org

urlpatterns = [
	url(r'^$', main, name='main'),
	url(r'^edu/$', edu, name='edu'),
	url(r'^work/$', work, name='work'),
	url(r'^org/([0-9]+)/$', org, name='org')
	]