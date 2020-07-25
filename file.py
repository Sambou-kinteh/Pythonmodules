my_file = open('file.txt',"w")
my_file.write('Hi opener\n\t\t\tMy name is sam \n\t\tand i usually call myself the \n\t\t\t   programmer')
my_file.writable()

file = open('file.txt',"r")
r = file.read()
print(r)
print(len(r), 'characters')
file.close()
counter = 1
n = len(r)
for count in my_file:
    if (chr("") and (count > 0)):
        n += counter
print("counts of characters = ",n )
    

my_file.close()
         
file = open('file.txt',"r")
r = file.read()
print(r1)
print(len(r1), 'characters')
file.close()
    
