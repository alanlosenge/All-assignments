import array

#create an array of integers

intarr = array.array('i', [1, 2, 3, 4, 5])

#accessing elements of array using index
print("First element:", intarr[0])

#add items to array to the end of the array
intarr.append(6)
print(intarr)

#remove items from array by speficying the index
intarr.remove(3)
print(intarr)
