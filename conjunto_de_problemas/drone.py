#  area total paralelepipado ((2*(a*b))+(2*(a*c))+(2*(b*c)))
a = int(input())
b = int(input())
c = int(input())
h = int(input())
l = int(input())

if (a*b) or (a*c) or (b*c) <= (h*l):
    print("S")
else:
    print("N")
