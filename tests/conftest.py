# Copyright 2019-present Lenovo
# Confidential and Proprietary

from pytest import fixture


@fixture(autouse=True)
def settings(settings):
    settings.ROOT_URLCONF = 'lico.job.test_app.urls'
    return settings
