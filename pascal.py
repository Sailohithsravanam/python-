def generate(numRows):
    triangle = []
    for i in range(numRows):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
numRows = 5
output1 = generate(numRows)
print(output1)
numRows = 1
output2 = generate(numRows)
print(output2)
