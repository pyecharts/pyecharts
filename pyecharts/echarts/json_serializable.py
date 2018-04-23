class JsonSerializable(object):

    def __init__(self):
        self.config = {}

    def __setitem__(self, key, value):
        self.config[key] = value
