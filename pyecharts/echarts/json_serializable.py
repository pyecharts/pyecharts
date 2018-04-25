class JsonSerializable(object):

    def __init__(self):
        self.config = {}

    def __setitem__(self, key, value):
        self.config[key] = value

    def __getitem__(self, key):
        return self.config.get(key)

    def update(self, **kwargs):
        self.config.update(**kwargs)
