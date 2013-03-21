from BaseClient import BaseClient

class ClientEx(BaseClient):
    def _check_listTemplates(self, kwargs):
        if not 'templatefilter' in kwargs:
            raise RuntimeError("Missing required argument 'templatefilter'")

    def __getattr__(self, name):
        def _request(*args, **kwargs):
            api = _request._methodname
            checker = getattr(self, '_check_' + api)
            if not checker.__name__ != '_request_':
                checker(kwargs)
            return self.request(api, kwargs)
        ret = _request
        ret._methodname = name
        return ret

