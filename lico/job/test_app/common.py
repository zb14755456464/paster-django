from rest_framework.views import exception_handler as old_exception_handler


def exception_handler(exc, context):
    return old_exception_handler(
        exc, context
    )
