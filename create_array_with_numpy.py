import numpy as np

#creating array using numpy
aklist=[[1,2,3],[4,5,1],[5,5,6]]
ARRAY=np.array(aklist)
print("ARRAY=\n",ARRAY)


#find the dimension of array
print("THE DIMEMSION OF ARRAY IS ",ARRAY.shape)


#create number list from 0 to 30(excluding 30) with a gap of 2
n=np.arange(0,30,2)
print("LIST FROM 0 to 30 with gap of two",n)

#reshape your generated array
n=n.reshape(5,3)
print("reshaped array is \n",n)


#resize array
a = np.arange(6)
a = np.resize(a, (2,3))
print("resized array is \n",a)


#create 9 numbers from 0 to 4 keeping equal gaps between numbers
o=np.linspace(0,4,9)
print("creating 9 numbers from 0 to 4 keeping equal gaps between numbers\n",o)

print("2_D array with ones on the diagnol and zeros elsewhere\n",np.eye(3))
print("find the diagnol ",np.diag(ARRAY))
print(" Repeat elements of an array using repeat.",np.array([1,2,3,4]*4))

#Combining Arrays
arr=np.ones([5,3],int)
print("array of size 5x3 with ones as element\n",arr)
#Use vstack to stack arrays in sequence vertically (row wise).
print("Use vstack to stack arrays in sequence vertically (row wise)\n"
,np.vstack([arr,5*arr]))
print("Use hstack to stack arrays in sequence horizontally (column wise)\n",np.hstack([arr,3*arr]))
