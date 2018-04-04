"""
Definition of urls for MLB_Player_API.
"""

from django.conf.urls import include, url
import app.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', MLB_Player_API.views.home, name='home'),
    # url(r'^MLB_Player_API/', include('MLB_Player_API.MLB_Player_API.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', app.views.home, name = "home")


]
