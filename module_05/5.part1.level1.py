class StringVar:
    def __init__(self, new_string):
        self.s = new_string

    def set(self, new_string):
        self.s = new_string

    def get(self):
        return self.s


var = StringVar("My string")
print(var.s)
var.set("My new string!")
print(var.get())
