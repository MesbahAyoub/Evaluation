# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 08:52:00 2023

@author: pc
"""

#Question 36

def string_to_matrix(matrix_string):
    matrix = []
    lines = matrix_string.strip().split('\n')
    for line in lines:
        row = [int(cell) for cell in line.split()]
        matrix.append(row)
    return matrix

#Question 37

def sorted_cell_list(matrix):
    
    cell_list = []

    for row in matrix:
        for cell in row:
            if cell not in cell_list: 
                cell_list.append(cell)

    cell_list.sort()  
    return cell_list

#Question 38

def spiral_filled_matrix(integer_list):
    n = int(len(integer_list) ** 0.5)  
    matrix = [[0] * n for _ in range(n)]  

    left, right, top, bottom = 0, n - 1, 0, n - 1
    current_index = 0  

    while left <= right and top <= bottom:
        
        for i in range(left, right + 1):
            matrix[top][i] = integer_list[current_index]
            current_index += 1

        for i in range(top + 1, bottom + 1):
            matrix[i][right] = integer_list[current_index]
            current_index += 1

        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                matrix[bottom][i] = integer_list[current_index]
                current_index += 1

        if left < right:
            for i in range(bottom - 1, top, -1):
                matrix[i][left] = integer_list[current_index]
                current_index += 1

        left += 1
        right -= 1
        top += 1
        bottom -= 1

    return matrix

#Question 39

def matrix_to_string(matrix):
    matrix_string = ""
    for row in matrix:
        matrix_string += " ".join(map(str, row)) + "\n"
    return matrix_string


#Question 40

with open("matrix_8_file.txt", "r") as file:
    matrix_string = file.read()

matrix = string_to_matrix(matrix_string)
sorted_cells = sorted_cell_list(matrix)
spiral_matrix = spiral_filled_matrix(sorted_cells)
sorted_matrix_string = matrix_to_string(spiral_matrix)

with open("matrix_8_spiral_file.txt", "w") as file:
    file.write(sorted_matrix_string)

print(f"matrix_8_file : {matrix}")
print(f"the spiral Matrix : {spiral_matrix}")