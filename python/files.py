# pythn has functions for creating,reading, updating and deleting files
# open a file
myFile=open('myfile.txt','w')
# print (myFile.name,myFile.closed,myFile.mode)
# write to file
myFile.write('I love python')
myFile.write('and JavaScript')
myFile.close()

# append to file
myFile=open('myFile.txt','a')
myFile.write('I also like mimosas')

# read from file
myFile=open('myFile.txt','r+')
text=myFile.read(10)
print(text)