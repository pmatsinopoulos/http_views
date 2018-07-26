from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.current_datetime),
    url(r'^not_found/$', views.not_found),
]
