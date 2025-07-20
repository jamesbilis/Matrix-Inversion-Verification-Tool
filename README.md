# Matrix Inversion Checker

This command-line Python tool checks whether two user-provided square matrices are mathematical inverses of each other. It uses NumPy for matrix operations and includes validation for matrix dimensions and numerical precision.

## Technologies

- Python
- NumPy

## Features

- Accepts custom matrix inputs from the user or predefined arrays
- Validates matrix shape and dimensions (square matrices only)
- Performs dot product multiplication and checks for identity matrix
- Includes error tolerance for floating-point precision
- Clean CLI prompts and result feedback

## ▶How to Run

```bash
python matrix_checker.py
```

Enter matrices when prompted, or edit the script to include predefined values.

## Files

```
matrix-checker/
│
├── matrix_checker.py      # Main logic
└── README.md              # Instructions and project description
```

## Example Output

```
Matrix A:
[[1, 2],
 [3, 4]]

Matrix B:
[[-2, 1],
 [1.5, -0.5]]

Result: These matrices are inverses of each other 
```

## License

MIT License
