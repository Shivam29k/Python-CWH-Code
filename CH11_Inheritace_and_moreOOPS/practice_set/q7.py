# Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} + "
            index += 1
        return str1[:-2]

    def __add__(self, vec2):
        if len(self.vec)!=len(vec2.vec):
            return "Addition failed as th length of both vectors not equal"
        newList = []
        for (i, j) in zip(self.vec, vec2.vec):
            newList.append(i + j)
        return Vector(newList)

    def __mul__(self, vec2):
        if len(self.vec)!=len(vec2.vec):
            return "Multiplicaction failed as th length of both vectors not equal"
        sum = 0
        for i, j in zip(self.vec, vec2.vec):
            sum += i*j
        return sum
    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6])
print(len(v1))
print(len(v2))
print(v1+v2)
print(v1*v2)