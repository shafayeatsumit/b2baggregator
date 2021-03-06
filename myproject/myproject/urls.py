from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'products',views.scraped_item_viewset)



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
