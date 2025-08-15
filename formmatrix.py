def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} elements separated by spaces: ").split()))
        if len(row) != cols:
            print("Incorrect number of columns. Please re-enter this row.")
            return input_matrix()
        matrix.append(row)
    return matrix

# Example usage:
mat = input_matrix()
print("Matrix:")
for row in mat:
    print(row)
    #bls 