from django.conf.urls import include, url
from django.contrib import admin

# admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cereal_list_view/$', 'main.views.cereal_list_view'),
    url(r'^cereal_list_template/$', 'main.views.cereal_list_template'),
    url(r'^cereal_list_template2/$', 'main.views.cereal_list_template2'),
    url(r'^cereal_search/(?P<cereal>\w+)/$', 'main.views.cereal_search'),
    url(r'^get_cereal_search/$', 'main.views.get_cereal_search'),
    url(r'^manufacturer_list_view/$', 'main.views.manufacturer_list_view'),
    url(r'^manufacturer_search/(?P<manufacturer>\w+)/$', 'main.views.manufacturer_search'),
    url(r'^get_manufacturer_search/$', 'main.views.get_manufacturer_search'),
    url(r'^cereal_detail/(?P<pk>\d+)/$', 'main.views.cereal_detail'),
    url(r'^form_view/$', 'main.views.form_view'),
    url(r'^form_view2/$', 'main.views.form_view2'),
    url(r'^cereal_create/$', 'main.views.cereal_create'),
    url(r'^signup/$', 'main.views.signup'),
    url(r'^home/$', 'main.views.home'),
    url(r'^login_view/$', 'main.views.login_view'),
    url(r'^logout_view/$', 'main.views.logout_view'),
]

