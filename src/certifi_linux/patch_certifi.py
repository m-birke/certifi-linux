import wrapt

from certifi_linux.certifi_linux import contents, where


@wrapt.when_imported("certifi")
def patch_certifi(certifi):
    def wrapt_contents(_wrapped_func, _instance, _args, _kwargs):
        return contents()

    def wrapt_where(_wrapped_func, _instance, _args, _kwargs):
        return where()

    wrapt.wrap_function_wrapper(certifi, "contents", wrapt_contents)
    wrapt.wrap_function_wrapper(certifi, "where", wrapt_where)
