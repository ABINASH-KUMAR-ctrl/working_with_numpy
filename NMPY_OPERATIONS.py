import numpy as np
n=np.arange(0,40,5)

a=n.reshape(4,2)
print("this array of size 4x2\n",a)

m=np.arange(0,8,1)
b=m.reshape(4,2)
print("another array of size 4x2\n",b)

 #elementwise addition ,substraction , multiplication ,division
print("sum=\n",a+b)
print("diffennce\n",a-b)
print("product\n",a*b)
print("division\n",a/b)
print("element_wise power\n",a**2)

#dot product applicabe for row vector
print("dot product is ",n.dot(m))

#transpose
print("transposed array\n",a.T)

#check the data types of elements of array
print("array 'a' data type is \n",a.dtype)
#Use .astype to cast to a specific type.
print("changed a is \n",a.astype('f'))
