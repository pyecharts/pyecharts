from ..render import engine


class ChartMixin:
    def add_js_funcs(self, *fns):
        for fn in fns:
            self.js_functions.add(fn)
        return self

    def load_javascript(self):
        return engine.load_javascript(self)


class CompositeMixin(ChartMixin):
    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)
