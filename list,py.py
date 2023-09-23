# From a list of numbers, move zero to the end of the list.
list = [1,0,2,0,4,6,9,8]

for item in list:

     if item ==0:

         list.remove(item)
         list.append(item)

print(list)