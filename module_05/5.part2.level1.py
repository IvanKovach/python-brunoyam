import json


class Model:
    def __init__(self, title, text, author):
        self.title, self.text, self.author = title, text, author

    def _save_(self):
        result = {}
        for n in list(filter(lambda x: not x.startswith('_'), dir(example))):
            result[n] = eval('self.' + n)
        print(result)
        with open('model.json', 'w') as file:
            json.dump(result, file)


example = Model('Brunoyam', 'My text', 'IKovach')
example._save_()
