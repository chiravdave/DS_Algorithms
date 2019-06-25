# Table of Contents
1. [Introduction](README.md#introduction)
2. [Project structure](README.md#project-structure)
3. [Input file and format](README.md#input-file-format)
4. [Instructions to run the script](README.md#instructions-to-run-the-script)

# Introduction
This project contains a script that will perform transpose and multiplication of MXN matrices. The input to the script is a path to a directory containing the input file. It will store the final result to the same directory and under an **output** folder. In order to have a high-performance, portable linear algebra library for the client, I have used the power of threads. Both of the matrix multiplication and transpose operations can be broken down into independent sub problems which can then be solved in parallel using threads. Let me explain how I have implemented these operations:

* Matrix Multiplication
	* Let us consider 2 matrices with (m1_rows, m1_cols) and (m2_rows, m2_cols). Now, in order to compute the first row of the resultant matrix, we would be taking dot products between the first row of the first matrix and all the column vectors of the second matrix. We can perform these individual dot products in parallel using threads. Ex:

		Thread 1 : M1_Row_1[........] *  M2_Col_1[.........]
		Thread 2 : M1_Row_1[........] *  M2_Col_2[.........]
.
.
.
		Thread n : M1_Row_1[........] *  M2_Col_m[.........]

	Hence, if your system can support large number of threads then you can get the results very quickly. However, if you try to use very large number of threads then things might not help you much because the speed also depends on the number of processors the system has. So, it is always crucial to first see how many processors your system has and then accordingly you should specify the number of threads to use. 

* Transpose
	* Similarly, we can perform transpose of multiple matrices in parallel using threads. In addition to that, I am performing in-place transpose for a square matrix thereby, saving space and time from creating a new matrix.  

# Project structure
	.
    ├── test_cases              	# Test Cases folder
    │   ├── case1			# Test case 1
    │	│	├── input.txt       	# Input file
    │	│	│── output          	# Output folder
    │	│		│── output.txt  # Output file
    │   └── ....			# More test cases
    ├── src                     	# Source files
    │	├── matrix_ops.cpp      	# File containing main code 
    └── README.md
    
# Input file and format
We need to create a folder for every test case inside the **test_cases** directory. Inside that folder we will create the input file with the name as **input.txt**. Now, we will see the format required for the input file:

	Line 1: 1 - for multiplication,
	        2 - for transpose
	Line 2: n - no. of matrices
	Line 3:   - blank
	Line 4: m1_rows - no. of rows for first matrix
	Line 5: m1_cols - no. of columns for first matrix
	Line 6: 2,3,..,5 - first row elements of the first matrix (elements should be separated by comma)
	Line 7: 3,2,...,6 - second row elements of the first matrix (elements should be separated by comma)
	  .
	  .
	Line 10: 4,5,...,10 - last row elements of the first matrix (elements should be separated by comma)
	Line 11:  - blank
	Line 12: m2_rows - no. of rows for second matrix
	Line 13: m2_cols - no. of columns for second matrix
	Line 14: 12,13,..,15 - first row elements of the second matrix (elements should be separated by comma)
	  .
	  .
	Line 25: 22,23,..,25 - last row elements of the final matrix (elements should be separated by comma)

Example of two 2X2 matrix multiplication:
	
	1
	2

	2
	2
	1,2
	3,4

	2
	2
	4,3
	2,1

Example of two 1X3 and 2X2 matrix transpose:
	
	2
	2

	1
	3
	1,2,3

	2
	2
	1,2
	3,4

# Instructions to run the script
Step 1. Prepare the input file.

Step 2. Navigate to the **src** folder.

Step 3. Open **matrix_ops.cpp** and update no. of threads (default=4) at line no. 15 if needed by changing the value for the **NUM_THREADS** preprocessor macro.

Step 3. Compile the script if you have made some changes to it by running the command **clang++ -std=c++11 matrix_ops.cpp -o matrix_ops**.

Step 4. Run the executable with the path for the test case folder as argument. Ex: **./matrix_ops ../test_cases/case2/**. <font color="red">Do not forget to add the last forward slash.</font>

**NOTE:** Please follow the exact naming conventions and for your reference, some test case examples are provided so that you can have a look at it and understand how to write the input file.
