#include<iostream>
#include<fstream>
#include<thread>
#include<sys/stat.h>
#include<sys/types.h>
#include<string>
#include<string.h>
#include<stdlib.h>
#include<sstream>

using namespace std;

// No. of threads that your system can support
#define NUM_THREADS 4

// Function to display console messages
void show_msg(string msg){
	cout << msg << endl;
}

// Function to create an empty matrix
float** create_matrix(int rows, int cols){
	float** m = (float**)malloc(rows * sizeof(float*));
	for(int row=0; row<rows; row++){
		m[row] = (float*)malloc(cols * sizeof(float));
	}
	return m;
}

// Function to free a matrix from memory
void free_matrix(float** m, int rows){
	for(int row=0; row<rows; row++){
		free(m[row]);
	}
	free(m);
}

// Function to read a matrix from a file 
float** read_matrix(ifstream& input_file, int rows, int cols){
	// Pointer for the matrix
	float** m;
	try{
		// Allocating space for storing the matrix
		m = (float**)malloc(rows * sizeof(float*));
		for(int row=0; row<rows; row++){
			m[row] = (float*)malloc(cols * sizeof(float));
		}
		int col;
		string ele;
		for(int row=0; row<rows; row++){
			col = 0;
			getline(input_file, ele);
			// Validating if the specific row is provided or not
			if(ele == ""){
				throw "Elements for the matrix should be of numeric values and comma separated. Please check the input file and format.";
			}
			stringstream linestream(ele);
			// Reading elements for the specific row one at a time
			while(getline(linestream, ele, ',')){
				// Validating no. of elements provided for a particular row
				if(col > cols || ele == ""){ 
					throw "Extra elements provided for row " + to_string(row) + ". There should be " + to_string(cols) + " elements.";
				}
				m[row][col] = stof(ele);
				col++;
			}
		}
		getline(input_file, ele);
		return m;
	}
	catch(const string exception){
		// Releasing resources
		free_matrix(m, rows);
		throw exception;
	}
	catch(...){
		throw "Elements for the matrix should be of numeric values and comma separated. Please check the input file and format.";
	}
}

// Function to complete all remaining threads
void complete_all_threads(thread* thread_arr, int n_threads ){
	for(int i=0; i<n_threads; i++){
		if(thread_arr[i].joinable()){
			thread_arr[i].join();
		}
	}
}

// Function to create a directory
int create_directory(char* path){
	int success = mkdir(path, S_IRUSR | S_IWUSR | S_IXUSR);
	if(success == 0){
		show_msg("Output directory created successfully!");
	}
	else{
		show_msg("Output directory is already present.");
	}
	return success;
}

// Function to write/append the final result to a file
void save_result(char* output_file_path, int mode, float** result, int rows, int cols){
	ofstream output_file;
	if(mode == 1){
		output_file.open(output_file_path, ios::out);
	}
	else{
		output_file.open(output_file_path, ios::app);
	}
	// Writing the resultant matrix to the output file
	for(int row=0; row<rows; row++){
		for(int col=0; col<cols; col++){
			output_file << result[row][col] << " , ";
		}
		output_file << "\n";
	}
	output_file << "\n";
	output_file.close();
	show_msg("Result has been saved to a file named output.txt inside an output sub-folder under your test case folder.");
}

// Class for performing matrix multiplication
class MM{
	public:
		// Call this method to perform matrix multiplication
		void multiply(ifstream&, char*);
	private:
		// This method will perform matrix multiplication using threads for faster performance
		float** _multiply(float**, float**, int, int, int);
		// This method will perform dot product between 2 vectors
		void dot_product(float**, float**, float**, int, int,int);
};

// Class for performing transpose of a matrix
class T{
	public:
		// Call this method to perform transpose
		void transpose(ifstream&, char*);
	private:
		// This method will perform transpose for a non square matrix 
		void transpose_non_square(float**, int, int, float***, int);
		// This method will perform in-place transpose for a square matrix
		void transpose_square(float**, int, float***, int);
};

void MM::dot_product(float** m1, float** m2, float** result, int row, int col, int m2_rows){
	/*
		m1: Pointer to the first matrix
		m2: Pointer to the second matrix
		row: A particular row of the first matrix
		col: A particular column of the second matrix
		m2_rows: No. of rows of the second matrix which is same as no. of columns of the first matrix
	*/

	float sum = 0.0;
	for(int i=0; i<m2_rows; i++){
		sum += m1[row][i] * m2[i][col];
	}
	result[row][col] = sum;
}

float** MM::_multiply(float** m1, float** m2, int m1_rows, int m2_rows, int m2_cols){
	/*
		m1: Pointer to the first matrix
		m2: Pointer to the second matrix
		m1_rows: No. of rows of the first matrix
		m2_rows: No. of rows of the second matrix which is same as no. of columns of the first matrix
		m2_cols: No. of columns of the second matrix
	*/

	int col, cur_thread = 1;
	// Creating empty matrix to store the product
	float** result = create_matrix(m1_rows, m2_cols);
	// List to store threads
	thread MM_threads[NUM_THREADS];

	for(int row=0; row<m1_rows; row++){
		col = 0;
		while(col<m2_cols){
			// Checking if we have some threads available
			if(cur_thread <= NUM_THREADS){
				MM_threads[cur_thread-1] = thread(&MM::dot_product, this, m1, m2, result, row, col, m2_rows);
				cur_thread++;
				col++;
			}
			else{
				// Waiting for all the running threads to complete so that we can reuse them 
				complete_all_threads(MM_threads, cur_thread-1);
				cur_thread = 1;
			}
		}
	}
	if(cur_thread > NUM_THREADS){
		cur_thread--;
	}
	// Waiting for all the running threads to complete so that we can have the final result
	complete_all_threads(MM_threads, cur_thread);
	// Releasing resources
	free_matrix(m1, m1_rows);
	free_matrix(m2, m2_rows);
	return result;
}

void MM::multiply(ifstream& input_file, char* output_dir_path){
	int count = 1;
	try{
		string data;
		getline(input_file, data);
		// Reading the no. of matrices
		int n_matrices = stoi(data);
		if(n_matrices <= 1){
			show_msg("There should be at least 2 matrices for multiplication.");
			return;
		}

		// last_col will be used to validate multiplication by checking if the rows of the second matrix matches with the columns of the first matrix 
		int m1_rows, m1_cols, m2_rows, m2_cols, last_col;
		//Calling getline() to avoid one blank line in the input file
		getline(input_file, data); 
		getline(input_file, data);
		m1_rows = stoi(data);
		getline(input_file, data);
		m1_cols = last_col = stoi(data);
		// Pointing to the first matrix
		float** m1 = read_matrix(input_file, m1_rows, m1_cols);
		// For poinitng rest of the matrices in the input file 
		float** m2;
		
		count++;
		while(count <= n_matrices){
			getline(input_file, data);
			m2_rows = stoi(data);
			if(last_col != m2_rows){
				show_msg("Matrix "+to_string(count)+" is incompatible. No. of rows should be "+to_string(last_col));
				return;
			}
			getline(input_file, data);
			m2_cols = last_col = stoi(data);
			m2 = read_matrix(input_file, m2_rows, m2_cols);
			m1 = _multiply(m1, m2, m1_rows, m2_rows, m2_cols);
			last_col = m2_cols;
			count++; 	
		}

		// Creating output folder to store the final result
		create_directory(output_dir_path);
		// Saving the final result to an output file inside the output folder
		strcat(output_dir_path, "/output.txt");
		save_result(output_dir_path, 1, m1, m1_rows, last_col);
		free_matrix(m1, m1_rows);
	}
	catch(const string exception){
		show_msg("Problem with matrix " + to_string(count) + ". " + exception);
	}
	catch(...){
		show_msg("Problem with input format. Please check the inputs for the matrix " + to_string(count));
	}
}

void T::transpose_non_square(float** m, int rows, int cols, float*** transpose_matrices, int index){
	// Creating empty matrix to store the transpose
	float** transpose_matrix = create_matrix(cols, rows);
	for(int row=0; row<cols; row++){
		for(int col=0; col<rows; col++){
			transpose_matrix[row][col] = m[col][row];
		}
	}

	free_matrix(m, rows);
	transpose_matrices[index] = transpose_matrix;
}

void T::transpose_square(float** m, int n, float*** transpose_matrices, int index){
	int temp;
	for(int row=0; row<n-1; row++){
		for(int col=row+1; col<n; col++){
			temp = m[col][row];
			m[col][row] = m[row][col];
			m[row][col] = temp;
		}
	}
	transpose_matrices[index] = m;
}

void T::transpose(ifstream& input_file, char* output_dir_path){
	int count = 1;
	try{
		// Creating output folder to store the final results
		create_directory(output_dir_path);
		// Path for the output file inside which the results will be written out
		strcat(output_dir_path, "/output.txt");
		string data;
		getline(input_file, data);
		// Reading the no. of matrices specified
		int n_matrices = stoi(data);
		if(n_matrices < 1){
			show_msg("There should be at least one matrix for performing transpose.");
			return;
		}

		int rows, cols, cur_thread=1;
		// For matrices in the input file 
		float** m;
		// List for storing threads
		thread MM_threads[NUM_THREADS];
		// List of pointers for the transposed matrices
		float*** transpose_matrices=(float***)malloc(n_matrices * sizeof(float**));
		// Book keeping for releasing resources
		int transpose_matrices_rows[n_matrices], transpose_matrices_cols[n_matrices];
		// Calling getline to avoid the blank line
		getline(input_file, data);

		while(count<=n_matrices){
			// Checking if we have some threads available
			if(cur_thread <= NUM_THREADS){
				getline(input_file, data);
				rows = stoi(data);
				getline(input_file, data);
				cols = stoi(data);
				m = read_matrix(input_file, rows, cols);
				// Checking if the matrix is square or not
				if(rows == cols){
					transpose_matrices_rows[count-1] = transpose_matrices_cols[count-1] = rows;
					MM_threads[cur_thread-1] = thread(&T::transpose_square, this, m, rows, transpose_matrices, count-1);
				}
				else{
					transpose_matrices_rows[count-1] = cols;
					transpose_matrices_cols[count-1] = rows;
					MM_threads[cur_thread-1] = thread(&T::transpose_non_square, this, m, rows, cols, transpose_matrices, count-1);
				}
				cur_thread++;
				count++;
			}
			else{
				// Waiting for all the running threads to complete so that we can reuse them 
				complete_all_threads(MM_threads, cur_thread-1);
				cur_thread = 1;
			}
		}
		if(cur_thread > NUM_THREADS){
			cur_thread--;
		}

		// Waiting for all the running threads to complete so that we can have the final result
		complete_all_threads(MM_threads, cur_thread);
		// Write all the transposes to the output file in order
		for(int i=0; i<n_matrices; i++){
			if(i==0){
				save_result(output_dir_path, 1, transpose_matrices[i], transpose_matrices_rows[i], transpose_matrices_cols[i]);
			}
			else{
				save_result(output_dir_path, 2, transpose_matrices[i], transpose_matrices_rows[i], transpose_matrices_cols[i]);	
			}
			free_matrix(transpose_matrices[i], transpose_matrices_rows[i]);
		}
		free(transpose_matrices);
	}
	catch(const string exception){
		show_msg("Problem with matrix " + to_string(count) + ". " + exception);
	}
	catch(...){
		show_msg("Problem with input format. Please check the inputs for the matrix " + to_string(count));
	}
}

int main(int argc, char** argv)
{
	if(argc != 2){
		show_msg("Invalid no. of arguments passed. Please pass the path of your test case folder only.");
		return 0;
	}

	// Creating path for input file and output directory
	char* directory = argv[1];
	char input_file_path[strlen(directory)+10], output_dir_path[strlen(directory)+7];
	strcpy(input_file_path, directory); strcpy(output_dir_path, directory); 
	strcat(input_file_path, "input.txt"); strcat(output_dir_path, "output");

	//Checking if the path provided for the input file is valid or not
	ifstream input_file(input_file_path, ios::in);
	if(!input_file.is_open()){
		show_msg("Error in opening the input file. Please check if the path is correct and there exists an input file.");
	}
	else{
		try{
			string data;
			int choice;
			getline(input_file, data);
			// Reading the specified matrix operation choice 
			choice = stoi(data);
			switch(choice){
			case 1: MM matrix_mul;
					matrix_mul.multiply(input_file, output_dir_path);	
					break;
			case 2: T transpose_matrix;
					transpose_matrix.transpose(input_file, output_dir_path);
					break;
			default: show_msg("Invalid operation specified.\n 1:Multiplication\n 2:Transpose");
			}
	        input_file.close();
		}
		catch(...){
			show_msg("The first line of the input should specify the matrix operation to be performed.\n 1:Multiplication\n 2:Transpose");
		}
	}
		return 0;
}