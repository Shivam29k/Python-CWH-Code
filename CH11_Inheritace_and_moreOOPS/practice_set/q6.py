# Write __str__() method to print the vector as follows:
# 7i + 8j + 10k
# Assume vector of dimension 3 for this problem.

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str = ""
        l = ["i", "j", "k"]
        for (i,j) in zip(self.vec, l):
            str += f"{i}{j} + "
        return str[:-2]

v1 = Vector([1, 2, 3])
print(v1)    