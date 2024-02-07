def determinant(matrix):
	if len(matrix)!=2 or len(matrix[1])!=2:
		raise ValueError("matrix should be in 2*2 matrix")
	return matrix[0][0]*matrix[1][1]-matrix[1][0]
matrix_1=[[3,4],[3,4]]
result=determinant(matrix_1)
print("Determinant of 2*2 matrix",result)
	
