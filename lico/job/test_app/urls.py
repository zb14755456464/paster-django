from django.conf.urls import url

from lico.job.test_app.views import DogView, HuamanCreate

urlpatterns = [
    url(r'^index/$', DogView.as_view()),
    url(r'^human/$', HuamanCreate.as_view()),
]
