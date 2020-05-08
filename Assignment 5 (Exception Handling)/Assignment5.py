import os
print('\n\nFile Handling exceptions')
fname = str(input('Enter the file name : '))
mode = str(input('Specify mode of opening(r/w) : '))
end = 0
if(mode == 'r'):
    try:
        f = open(fname,mode)
    except IOError:
        print('File does not exist.')
        print('Do you want to create a file ?')
        c = str(input())
        if(c == 'yes' or c== 'Yes'):
            f = open(fname,'w')
            f.close()
            print('{} created'.format(fname))
        else:
            print('Exiting...')
            end = 1
    finally:
        if(end):
            f.close()
            quit()
        else:
            print('File opened in Read Mode')

    if(not(end)):
        print('Contents of file are:')
        f = open(fname,mode)
        text = f.read()
        print(text)

else:
    f = open(fname,mode)
    s = str(input('Enter the text to be written into the file:'))
    f.write(s)
    
#Zero Divison Exception
print('\n\nZero Division exceptions')

a = 0
try:
    c = 10 / a
except ZeroDivisionError:
    print("Sorry cannot divide by 0")

#Index out of range exceptions
print('\n\nIndex range exceptions')

l = [1,2,3,4]
try:
    for i in range(5):
        print(l[i],end = " ")
except IndexError:
    print("\nSorry Index out of range")

#Importing module not found exception
print('\n\nImporting modules exceptions')

try:
    import PIL
except ImportError:
    print("Sorry Module does not exist")


# Demonstration of try except finally clause
print('\n\nExample of try except finally')

d = {'a' : 1 , 'b': 2 , 'c': 3}
p = ['a','b','c','d']
try:
    for i in range(len(p)):
        print(d[p[i]])
except KeyError as k:
    print('Sorry key {} was not found'.format(k))
finally:
    print('Valid Dictionary is : ',d)
