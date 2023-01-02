def increment(num):
    try:
        return int(num) + 1
    except: 
        raise ValueError("This is not good - Shivam")
a = increment(5)
print(a)
a = increment('er')
print(a)