from derivide.middleware.flatfile import DerivideFlatFile

modes = dict()
modes["flatfile"] = DerivideFlatFile

class Derivide:
    def __init__(self, mode, *args, **kwargs):
        middleware = modes.get(mode)
        assert middleware is not None, f"Invalid mode: {mode}"
        self.middleware = middleware(*args, **kwargs)

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_value, traceback):
        self.save()

    def _check(self, func):
        mw_func = getattr(self.middleware, func, None)
        assert callable(mw_func), f"Expected function: {mw_func}"
        return mw_func

    def start(self):
        mw_start = self._check("start")
        return mw_start()

    def save(self):
        mw_save = self._check("save")
        return mw_save()

    def all(self):
        mw_all = self._check("all")
        return mw_all()

    def get(self, *entry_path):
        mw_get = self._check("get")
        return mw_get(*entry_path)

    def put(self, *entry_path, value):
        mw_put = self._check("put")
        return mw_put(*entry_path, value=value)

    def drop(self, *entry_path):
        mw_drop = self._check("drop")
        return mw_drop(*entry_path)
