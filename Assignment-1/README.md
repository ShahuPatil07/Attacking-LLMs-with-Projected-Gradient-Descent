### This Code implements Simplex method for optimization. This is particularly for a maximization problem with 3 in initial variables and 3 constraints (<=).
### Input format-
If its a minimization problem, please input the Z coefficients with an opposite sign. Similarily if constraint uses (>=), use opposte signs to input values.
By default, you' ll inputing 3 values for to be maximized expression, 4 for every constraint- 3 for its coefficiants and 1 for the RHS constnt value.
Code introduces 3 slack variables and performs optimization. Approach used is looping through the tabelue and checking if all values of Cj-Zj are negetive (which is the optimized condition). A boolean variable optimized is maintained to check this. DataFrame is iteratively modified using concept of Simplex method till we get the optimized values.

### example input- 
for the problem statement-
Maximize 3x1+ 2x2+ 5x3 with constaints of 
x1+ x2+ x3 <= 9
2x1+ 3x2+ 5x3 <= 30
2x1 - x2- x3 <=8
with x1,x2,x3>=0

Run the pyhton script and it will ask for inputs-
Input should look like
please enter coefficients for expression to be maximized seperated by spaces 3 2 5
please enter constraint 1 coefficients seperated by spaces 1 1 1 9
please enter constraint 2 coefficients seperated by spaces 2 3 5 30
please enter constraint 3 coefficients seperated by spaces 2 -1 -1 8

Output is maximized value of Z and tables after every iteration-

### In this case the output looks like-
   Cb  Xb  x1  x2  x3  x4  x5  x6   b  ratio
0   0   4   1   1   1   1   0   0   9      0
1   0   5   2   3   5   0   1   0  30      0
2   0   6   2  -1  -1   0   0   1   8      0
   Cb  Xb    x1    x2   x3  x4     x5  x6     b  ratio
0   0   4  0.60  0.40  0.0   1  0.000   0  9.00      9
1   5   3  0.40  0.60  1.0   0  0.200   0  6.00      6
2   0   6  2.08 -0.88 -0.8   0  0.032   1  8.96     -8
   Cb  Xb   x1        x2        x3  x4        x5        x6         b  \
0   0   4  0.0  0.400000  0.000000   1  0.000000  0.000000  9.000000   
1   5   3  0.0  0.600000  1.000000   0  0.200000  0.000000  6.000000   
2   3   1  1.0 -0.423077 -0.384615   0  0.015385  0.480769  4.307692 

Maximum value of Input expresion is 34

To run the python script, just have Pandas and numpy installed in your local IDE.
