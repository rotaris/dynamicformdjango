from django.conf.urls.defaults import *
from views import index, edit_items_in_list

urlpatterns = patterns('',
    url(r'^$', index, name="index"),
    url(r'^edit/(?P<pk>\d+)$', edit_items_in_list, name="edit_items_in_list"),
    (r'thanks$', 'django.views.generic.simple.direct_to_template', {'template': 'thanks.html'}),
)
