def percent(marks):
    return((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/5)

marks1 = [55, 56, 89, 90, 83]
print(percent(marks1))

marks2 = [56, 89, 89, 90, 83]
print(percent(marks2))

marks3 = [55, 56, 89, 99, 83]
print(percent(marks3))

marks4 = [100, 56, 89, 90, 83]
print(percent(marks4))


def fun():
    print("hello hie bye")

fun()

def greet(name):
    print(f"Good Day, {name}")

greet("Shivam")

def add(n1, n2):
    return n1 + n2

s = add(2,3)    
print(s)

# setting a default parameter value
def greet(name = "stranger"):
    print(f"Good Day, {name}")

greet()
