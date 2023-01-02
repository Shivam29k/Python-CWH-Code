# Write a class vector representing a vector of n dimension. Overload the + and * operator which calculates the sum and the dot product of them.
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
        newList = []
        for (i, j) in zip(self.vec, vec2.vec):
            newList.append(i + j)
        return Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i, j in zip(self.vec, vec2.vec):
            sum += i*j
        return sum


v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 5])
print(v1+v2)
print(v1*v2)
