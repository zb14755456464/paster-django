from django.conf.urls import url
from lico.job.test_app.views import DogView

urlpatterns = [
    url(r'^index/', DogView.as_view()),
]
