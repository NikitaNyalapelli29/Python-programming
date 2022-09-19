import math

print("Enter the first point A")
x1, y1 ,z1= map(int, input().split())

print("Enter the second point B")
x2, y2, z2= map(int, input().split())

print("Enter the third point C")
x3, y3, z3= map(int, input().split())

dist1 = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 )

print("The Euclidean Distance is " + str(dist1))

dist2 = math.sqrt((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2 )

print("The Euclidean Distance is " + str(dist2))

if dist1>dist2:
    print("Point A is closer to B")
elif dist1<dist2:
    print("Point A is closer to C")
else:
    print("Point B and C are in same distance to Point A")

