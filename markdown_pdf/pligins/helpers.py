"""Plugin helper functions."""


def get_key(params_dict, key, default):
    """Return value for key from given dict."""
    if params_dict and (key in params_dict):
        return params_dict.get(key)

    return default
