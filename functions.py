
def squares(l):
    ret = []

    for v in l:
        new_value = v ** 2 
        ret.append(new_value)

    return ret

def doubles(l):
    ret = []

    for v in l:
        new_value = v * 2
        ret.append(new_value)

    return ret

list_of_number = [ 1, 2, 3, 4, 5 ]

sq = squares(list_of_number)
print(sq)

db = doubles(list_of_number)
print(db)

def get_double(v):
    return v * 2

def get_square(v):
    return v ** 2

def process(l, func):
    ret = []

    for v in l:
        new_value = func(v) 
        ret.append(new_value)

    return ret

p1 = process(list_of_number, get_square)
print(p1)

list_of_number = [ 1, 2, 3, 4, 5 ]
p2 = process(list_of_number, lambda x : -x)
print(p2)