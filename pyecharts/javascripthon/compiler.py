import inspect

from metapensiero.pj.api import translates


class Python2Javascript:

    @staticmethod
    def translate(obj):
        source_lines, _ = inspect.getsourcelines(obj)
        javascript, _ = translates(source_lines)
        return javascript
