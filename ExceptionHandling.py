try:
    getfile = open('myfile', 'r')
    getfile.write('test')
except IOError:
    print('Unable to open or read the data in the file.')

else:
    print('The file was written successfully')
finally:
    getfile.close()
    print('File is now closed.')
    
# finally allows us to always execute something even if there is an exception or not. This is usually used to signify the end of the try except.
