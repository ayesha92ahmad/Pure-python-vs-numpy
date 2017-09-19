# Pure-python-vs-numpy
15 steps are performed on Matrices using both Pure python and numpy and their speeds are compared

1. Create a zeros array of size (3,5) and store in variable z.
2. Set all the elements in first row of z to 7.
3. Set all the elements in second column of z to 9.
4. Set the element at (second row, third column) of z to 5.
5. Create a vector of size 50 with values ranging from 50 to 99 and store in variable x.
6. Create a 4x4 matrix with values ranging from 0 to 15 and store in variable y.
7. Create a 5x5 array with 1 on the border and 0 inside.
8. Generate a 50x100 array of integer between 0 and 5,000 and store in variable a.
9. Generate a 100x200 array of integer between 0 and 20,000 and store in variable b.
10. Multiply matrix a and b together (real matrix product) and store to variable c.
11. Normalize a 3x3 random matrix ((x-min)/(max-min)) and store to variable d.
12. Subtract the mean of each row of matrix a.
13. Subtract the mean of each column of matrix b.
14. Transpose matrix c, add 5 to all elements in matrix, and store to variable e.
15. Reshape matrix e to 1d array, store to variable f, and print shape of f matrix.

We compare the execution time of various methods written in pure python and Numpy. 
We see that initially, when the data is small, ie when the matrix has fewer elements Python performs nearly as well or better than Numpy. 

However, as the data gets larger, **Numpy** performs extremely well compared to **Python**. We do this to emphasize on why Numpy is good Linear Algebra operations. Not only is it easier to code because of its expansive library for handling of matrices and vectors but also due to the fact the Numpy uses processor’s full capability to perform these calculations fast.
