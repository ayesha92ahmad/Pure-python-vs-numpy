import numpy as np
import time
import random
# - Fill in the code below the comment Python and NumPy same as in example.
# - Follow instructions in document.
###################################################################
# Example: Create a zeros vector of size 10 and store variable tmp.
# Python
pythonStartTime = time.time()
tmp_1 = [0 for i in range(10)]
pythonEndTime = time.time()

# NumPy
numPyStartTime = time.time()
tmp_2 = np.zeros(10)
numPyEndTime = time.time()
print('Python time: {0} sec.'.format(pythonEndTime-pythonStartTime))
print('NumPy time: {0} sec.'.format(numPyEndTime-numPyStartTime))


z_1 = None
z_2 = None
################################################################
# 1. Create a zeros array of size (3,5) and store in variable z.
# Python
pythonStartTime = time.time()
z_1 = [0] * 3
for i in range(3):
    z_1[i] = [0] * 5
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
z_2 = np.zeros((3,5), dtype='int')
numPyEndTime = time.time()


#################################################
# 2. Set all the elements in first row of z to 7.
pythonStartTime = time.time()
z_1[0] = [7]*5
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
z_2[0] = 7
numPyEndTime = time.time()

#####################################################
# 3. Set all the elements in second column of z to 9.
# Python
pythonStartTime = time.time()
for i in range(3):
    z_1[i][1] = [9]
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
z_2[:,1] = 9
numPyEndTime = time.time()

#############################################################
# 4. Set the element at (second row, third column) of z to 5.
pythonStartTime = time.time()
z_1[1][2]=5
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
z_2[1,2] = 5
numPyEndTime = time.time()

##############
print(z_1)
print(z_2)
##############


x_1 = None
x_2 = None
##########################################################################################
# 5. Create a vector of size 50 with values ranging from 50 to 99 and store in variable x.
pythonStartTime = time.time()
x_1 = [i for i in range(50,100)]
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
x_2 =  np.arange(50,100)
numPyEndTime = time.time()

##############
print(x_1)
print(x_2)
##############


y_1 = None
y_2 = None
##################################################################################
# 6. Create a 4x4 matrix with values ranging from 0 to 15 and store in variable y.
pythonStartTime = time.time()
a = [i for i in range(16)]
y_1 = [[0] * 4 for i in range(4)]
k=0
for i in range(4):
    for j in range(4):
        y_1[i][j]=a[k]
        k=k+1
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
y_2 = np.arange(16)
y_2=y_2.reshape(4,4)
numPyEndTime = time.time()

##############
print(y_1)
print(y_2)
##############


tmp_1 = None
tmp_2 = None
####################################################################################
# 7. Create a 5x5 array with 1 on the border and 0 inside amd store in variable tmp.
#python
pythonStartTime = time.time()
tmp_1 = [0] * 5
for i in range(5):
    tmp_1[i] = [1] * 5
for i in range(1,4):
    for j in range(1,4):
        tmp_1[i][j]=0
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
tmp_2 = np.ones((5,5))
tmp_2[1:-1,1:-1]=0
numPyEndTime = time.time()


##############
print(tmp_1)
print(tmp_2)
##############


a_1 = None; a_2 = None
b_1 = None; b_2 = None
c_1 = None; c_2 = None
#############################################################################################
# 8. Generate a 50x100 array of integer between 0 and 5,000 and store in variable a.
#python
pythonStartTime = time.time()

a = [i for i in range(5000)]
a_1 = [[0] * 100 for i in range(50)]
k=0
for i in range(50):
    for j in range(100):
        a_1[i][j]=a[k]
        k=k+1
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
a_2 = np.arange(5000)
a_2 = a_2.reshape(50,100)
numPyEndTime = time.time()


###############################################################################################
# 9. Generate a 100x200 array of integer between 0 and 20,000 and store in variable b.
#python
pythonStartTime = time.time()

b = [i for i in range(20000)]
b_1 = [[0] * 200 for i in range(100)]
k=0
for i in range(100):
    for j in range(200):
        b_1[i][j]=b[k]
        k=k+1
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
b_2 = np.arange(20000)
b_2 = b_2.reshape(100,200)
numPyEndTime = time.time()

#####################################################################################
# 10. Multiply matrix a and b together (real matrix product) and store to variable c.
pythonStartTime = time.time()
c_1 = [[0] * 200 for i in range(50)]
k=0
for i in range(50):
    for k in range(100):
        for j in range(200):
            c_1[i][j]=c_1[i][j]+ a_1[i][k]*b_1[k][j]

pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
c_2 = np.matmul(a_2,b_2)
numPyEndTime = time.time()

d_1 = None; d_2 = None
################################################################################
# 11. Normalize a 3x3 random matrix ((x-min)/(max-min)) and store to variable d.
# Python
pythonStartTime = time.time()
d_1 = [0] * 3
for i in range(3):
    d_1[i] = [0] * 5
for i in range(3):
    for j in range(3):
        d_1[i][j] = random.randint(1,100)
xmax = max(max(d_1))
xmin = min(min(d_1))
for i in range(3):
    for j in range(3):
        d_1[i][j] = (d_1[i][j]-xmin)/(xmax-xmin)
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
d_2 = np.random.randint(100, size=(3,3))
xmax, xmin = d_2.max(), d_2.min()
d_2 = (d_2 - xmin)/(xmax - xmin)
numPyEndTime = time.time()


##########
print(d_1)
print(d_2)
#########


################################################
# 12. Subtract the mean of each row of matrix a.
# Python
pythonStartTime = time.time()
def mean(l):
    return sum(l)/len(l)
for i in range(len(a_1)):
    m_1 =mean(a_1[i])
    for j in range(len(a_1[i])):
        a_1[i][j]= a_1[i][j]-m_1


pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
m_2 = np.mean(a_2, axis=1)
for i in range(len(m_2)):
    a_2[i] = a_2[i] - m_2[i]
numPyEndTime = time.time()

###################################################
# 13. Subtract the mean of each column of matrix b.
# Python
pythonStartTime = time.time()
def mean(l):
    return sum(l)/len(l)
for i in range(len(b_1)):
    m_1 =mean(b_1[i])
    for j in range(len(b_1[i])):
        b_1[i][j]= b_1[i][j]-m_1


pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
m_2 = np.mean(b_2, axis=1)
for i in range(len(m_2)):
    b_2[i] = b_2[i] - m_2[i]
numPyEndTime = time.time()



################
print(np.sum(a_1 == a_2))
print(np.sum(b_1 == b_2))
################

e_1 = None; e_2 = None
###################################################################################
# 14. Transpose matrix c, add 5 to all elements in matrix, and store to variable e.
# python

pythonStartTime = time.time()
e_1 = [0] * len(c_1[0])
for i in range(len(e_1)):
    e_1[i] = [0] * len(c_1)

for i in range(len(e_1)):
    for j in range(len(e_1[i])):
        e_1[i][j] = c_1[j][i] + 5

pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
e_2 = np.transpose(c_2)
e_2 = e_2 + 5

numPyEndTime = time.time()

##################
print (np.sum(e_1 == e_2))
##################


#####################################################################################
# 15. Reshape matrix e to 1d array, store to variable f, and print shape of f matrix.
#python
pythonStartTime = time.time()
f_1 = [0 for i in range(len(e_1)*len(e_1[0]))]
k=0
for i in range (len(e_1)):
    for j in range (len(e_1[0])):
        f_1[k]=e_1[i][j]
        k=k+1
pythonEndTime = time.time()
# NumPy
numPyStartTime = time.time()
f_2 = list(e_2.ravel())
numPyEndTime = time.time()
print(np.shape(f_1))
print(np.shape(f_2))