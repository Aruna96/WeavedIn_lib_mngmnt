from django.conf.urls import include, url
from django.contrib import admin
from librarymgmt import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'weavedin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/add', views.addBook),
    url(r'^books/$', views.listBooks),
    url(r'^author/$', views.see_author),
    url(r'^authors/add/$', views.addAuthor),
    url(r'^authors/$', views.listAuthors),
]
