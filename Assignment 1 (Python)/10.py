#Program to display numbers in a Geometric Series
a = int(input('Enter the first element : '))
r = int(input('Enter the common ratio : '))

print('First 10 numbers in the Geometric Series are :')
for i in range(10):
    print(a * (r**i))