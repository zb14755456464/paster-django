from django.conf.urls import url
from lico.job.test_app.views import index

urlpatterns = [
    url(r'^index/', index),
]
