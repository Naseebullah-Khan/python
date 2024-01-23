class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Underwater")

    def swim(self):
        print("Swimming")


nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breath()

list_1 = ["a", "b", "c", "d", "f", "g", "h"]
tuple_1 = ["do", "re", "mi", "fa", "so", "la", "ti"]
print(list_1[3:6])
print(list_1[3:])
print(list_1[:6])
print(list_1[::3])
print(list_1[::-1])

print(tuple_1[3:6])
print(tuple_1[3:])
print(tuple_1[:6])
print(tuple_1[::3])
print(tuple_1[::-1])