import numpy as np

def get_matrix(prompt_name):
    while True:
        try:
            dimension_input = input(f"\nPlease enter the dimensions of the {prompt_name} (Example: 2 2 for a 2x2 matrix): ")
            rows, cols = map(int, dimension_input.split())

            elements_input = input(f"Enter {rows * cols} integers separated by spaces: ")
            elements = list(map(float, elements_input.split()))

            if len(elements) != rows * cols:
                print("\nI'm sorry, the number of elements you gave me does not match the dimensions. \nPlease try again.")
                continue

            matrix = np.array(elements).reshape((rows, cols))

            print(f"\nHere is your {prompt_name}:")
            print(matrix)

            confirmation = input("Does this look correct? Please type Yes or No: ").lower()
            if confirmation == 'yes':
                return matrix
            else:
                print("Let's try entering the matrix again.")

        except ValueError:
            print("Invalid input. Please enter integers only.")

def program():
    print("\nWelcome to the Matrix Inversion Checker!")
    print("I can tell you if two matrices are inverses of each other.")

    matrix1 = get_matrix("First Matrix")
    matrix2 = get_matrix("Second Matrix")

    try:
        product = np.dot(matrix1, matrix2)
        identity = np.eye(matrix1.shape[0])

        if np.allclose(product, identity):
            print("\nThe matrices are inverses to each other.")
        else:
            print("\nThe matrices are NOT inverses to each other.")

    except ValueError:
        print("Invalid matrix sizes. Please ensure the matrices are square and of the same size.")

   
# Function for multiple attempts and checking for valid response
def run_again():
    try_again = input("Would you like to try again? Please type Yes or No. ")
    if try_again.lower() == "yes":
        program()
        run_again()
    elif try_again.lower() == "no":
        print()
        print("Alright, see you next time!")
    else:
        wrong_response()

# Function for invalid response
def wrong_response():    
    print("Invalid Response. Please try again.")
    run_again()

# Run the program
program()
run_again()
