from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('Blog.urls')),
]
admin.site.site_header = 'MyPr Blog Admin'
