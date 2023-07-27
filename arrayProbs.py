prob. 1

from array import*

vals=array('i',[5,9,8,4,2])
print(vals)

output 
array('i',[5,9,8,4,2]


prob.2 

from array import*

vals=array('i',[5,9,8,4,2])
for i in range(5):
    print(vals[i])

  output 
5
9
8
4
2

prob. 3 

from array import*

vals = array('i',[5,9,8,4,2])

newArr=array(vals.typecode,(a*a for a in vals))
i=0
while i<len(newArr):
      print(newArr[i])
      i+=1

// output

25
81
64
16
4

prob. 4 

from array import*

arr=array('i',[])
n=int(input("Enter the length of the array"))
for i in range(n):
    x=int(input("Enter the next value"))
    arr.append(x)
    print(arr)

  /// output 
Enter the length of array 3
Enter the next value 20 
array('i',[20])
Enter the next value 45
array('i',[20,45]
Enter the next value 60 
array('i',[20,45,60]


prob. 5 

from numpy import*

arr1=array([
    [1,2,3,6,2,9],
    [4,5,6,7,5,3]])
    
arr2=arr1.flatten()
arr3=arr2.reshape(3,4)
print(arr3)

output 

[1,2,3,6]
[2,9,4,5]
[6,7,5,3]

      
