This is README file for MFDS assignments

The references take for this work are from:
1. https://www.codesansar.com/numerical-methods/gauss-elimination-method-python-program.htm
2. https://www.codesansar.com/numerical-methods/python-program-gauss-seidel-iteration-method.htm
3. https://www.codesansar.com/numerical-methods/python-program-jacobi-iteration-method.htm

As a part of Assignment 1, we are given task to implement 3 methods of solving linear systems of equations. They are:
1. Gauss Elimination
2. Gauss Seidel Method
3. Gauss Jacobi Method

In file gauss_elim.py, the Gaussian Elimination method is showcased. It takes randomly generated input matrices of size [n x (n+1)] in the form of augmented matrix. Then Forward elminiation and back substituion is applied as a part of Gauss elimination method. The solution of the system is obtained via both Pivoting and Non-Pivoting way. The user can provide the significant digits required for the whole process.

In file g_jac_sei.py, the Gauss Seidel and Jaobi methods are showcased. This takes randomly generated diagonally dominant matrices of size [3 x 4] in the form of augmented marix. Then the converegence criteria is used to arrive at the soultion obtained from the two methods.
