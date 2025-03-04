# Enter the number of rows for Pascal's Triangle: 5
#                         1                         
#                        1 1                        
#                       1 2 1                       
#                      1 3 3 1                      
#                     1 4 6 4 1  

def generate_pascals_triangle(n):
    triangle = []  # This will store the rows of Pascal's Triangle
    
    for row in range(n):  # Loop through each row
        current_row = [1]  # The first element in a row is always 1
        
        if row > 0:
            prev_row = triangle[row - 1]  # Get the previous row
            
            for col in range(1, row):  # Compute values using the sum of two above
                current_row.append(prev_row[col - 1] + prev_row[col])
            
            current_row.append(1)  # The last element in a row is always 1
        
        triangle.append(current_row)  # Add the row to the triangle
    
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(50))  # Center align for better visualization

# Get input from the user
n = int(input("Enter the number of rows for Pascal's Triangle: "))

# Generate and print Pascal's Triangle
pascals_triangle = generate_pascals_triangle(n)
print_pascals_triangle(pascals_triangle)
