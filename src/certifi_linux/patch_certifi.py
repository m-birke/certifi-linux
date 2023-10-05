import wrapt

from .certifi_linux import contents, where


@wrapt.when_imported("certifi")
def patch_certifi(certifi):

    def wrapt_contents(_wrapped_func, _instance, args, kwargs):
        return contents()

    def wrapt_where(_wrapped_func, _instance, args, kwargs):
        return where()

    wrapt.wrap_function_wrapper(certifi, "contents", wrapt_contents)
    wrapt.wrap_function_wrapper(certifi, "where", wrapt_where)
