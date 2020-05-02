import os
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
    
