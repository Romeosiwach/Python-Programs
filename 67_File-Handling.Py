'File Handling in Python ---> '
'The main advantage of implementing file is in order to store the output'
'Definition of file :- A file is a collection of data stored in an external memeory like hard disk'

'Type of files :-'
'Text File {Readable files}'
'Binary File {Not readable files}'

'Rules for handling files:-'

'RULE1- To perform read or write operations first we have to create a file'
'Syntax - filepointer=open(newfile,accessmode)'

'RULE2 - Close every file using the file'
'Syntax - filepointer.close()'

'File Creating :-'
'to create a file we have to use a built in function called [ open() ]' 
'now we have to create one file pointer called file object in python and in C language we call it as pointer'
'Syntax - file_object=open("filename.txt","access_mode")'

'Access modes :- '
'r=read mode'
'Syntax - file_object=open("newfile.txt","r")'

'w=write mode'
'Syntax - file_object=open("filename.txt","w")'

'a=append mode'
'Syntax - file_object=open("filename.txt","a")'