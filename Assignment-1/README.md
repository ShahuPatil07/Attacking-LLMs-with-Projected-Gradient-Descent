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

![Alt text]('https://github.com/ShahuPatil07/Attacking-LLMs-with-Projected-Gradient-Descent/blob/main/Assignment-1/Screenshot%20(87).png')


* To run the python script, just have Pandas and numpy installed in your local IDE.
