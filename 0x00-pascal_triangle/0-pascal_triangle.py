#!/usr/bin/python3
'''pascal triangle'''


def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list when n is less than or equal to 0
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
