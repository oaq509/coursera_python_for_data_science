File1 = open('text_files/info.txt','w')
File1.name # file name
File1.mode # 'r' ->  read , 'w' -> write
File1.close()

# Better practice to use with open()
# Because it automatically closes the file object

with open('text_files/data.txt','r') as File1:
    # file_stuff = File1.read()
    # file_stuff = File1.readlines() # readlines will split each line in a list ['owais ali\n', '+966590098626']
    # file_stuff = File1.readline() # readline it will read the first line only
    # file_stuff = File1.readline() # The second time it's called, it will save the second line
    file_stuff = File1.readlines(4) # The first four characters in the file.
    print(file_stuff)
    
# Write files
with open('text_files/write.txt','w') as File2:
    File2.write('Hello World!!\n') # \n add new line at the end
    
    lines = ['owais ali algarni\n','+966590098626\n','owais.garni.sa@gmail.com\n']
with open('text_files/loop.txt','w') as File3:
    for line in lines:
        File3.write(line)
        
# We can set the mode to appended using a lowercase a.
# This will not create a new file but just use the existing file.
# If we call the method write, it will just write to the existing file
with open('text_files/loop.txt','a') as File3:  
        File3.write('Computer Science')
        
# Copy Files
with open('text_files/write.txt','r') as readfile:  
    with open('text_files/copy.txt','w') as writefile:
        for line in readfile:
            writefile.write(line)
            
     
#--------------------------------------------------------------          
# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    
# Appending Files
# We can write to files without losing any of the existing data as follows by setting the mode argument to append: 
# a. you can append# Write a new line to text file
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n") a new line as follows:
        
        
        
# It's fairly ineffecient to open the file in or and then reopening it in to read any lines. 
# Luckily we can access the file in the following modes:
# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists.

with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())
    
