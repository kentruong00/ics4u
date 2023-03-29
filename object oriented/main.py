from point import Point

test = Point(2,6)
test2 = Point(-1,5)
print(test)
print(test2)

test3 = test * 3
print(test3)

origin = Point(0,0)
test4 = Point(5,0)
print(test4.distance(origin))