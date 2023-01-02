# Create a class C-2d vector and use it to create another class representing a 3-d vector.

class C2dvec:
    def __init__(self,i,j) -> int:
        self.icap = i
        self.jcap = j
    
    def __str__(self) -> str:
        return f"{self.icap}i + {self.jcap}j"

class C3dvec(C2dvec):
    def __init__(self, i, j, k) -> int:
        super().__init__(i, j)
        self.kcap = k

    def __str__(self) -> str:
        return f"{super().__str__()} + {self.kcap}k"

v2d = C2dvec(1, 3)
v3d = C3dvec(1, 9, 7)

print(v2d)
print(v3d)