class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        if isinstance(other, int):
            return [self for i in range(other)]
        return "Cant Multiply"


j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
# print(j)
# print(len(j))

# print(j + k)
# print(j * 2)


class Train():
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __repr__(self):
        return "{} car train".format(self.num_cars)

    def __len__(self):
        return self.num_cars


a_train = Train(4)
# print(a_train)
len(a_train)
