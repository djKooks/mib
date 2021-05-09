import pickle


class Storage:
    def __init__(self, id):
        self.id = id
        self.kv = dict()

    def update(self, key, value):
        new_kv = self.kv
        new_kv[key] = value
        self.kv = new_kv

    def get(self, key) -> str:
        return self.kv[key]

    def list(self):
        for key, value in self.kv.items():
            print(f'{key} -> {value}')
