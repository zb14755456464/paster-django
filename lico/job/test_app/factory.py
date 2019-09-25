# Copyright 2018-present Lenovo
# Confidential and Proprietary

from django_pastedeploy_settings import get_configured_django_wsgi_app


def make_application(global_config, **local_conf):

    # print(global_config)
    # print(local_conf)

    app = get_configured_django_wsgi_app(global_config, **local_conf)

    return app
