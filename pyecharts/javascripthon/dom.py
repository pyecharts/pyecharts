# Dummy functions, classes to make python compiler blind


def Date(*_):
    pass


class Document:
    pass


class window:
    pass


class Math:
    pass


class JSON:
    pass


class console:
    pass


class screen:
    pass


def alert(msg):
    pass


class JsValue(object):
    def __init__(self, value=None):
        self.value = value

    def __json__(self):
        return self.value


NULL = JsValue()
