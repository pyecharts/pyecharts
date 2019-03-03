# coding=utf-8


class OrderedSet:
    def __init__(self, *args):
        self._values = dict()
        self.items = []
        for a in args:
            self.add(a)

    def add(self, item):
        if not self._values.get(item, False):
            self._values.update(item=True)
            self.items.append(item)
