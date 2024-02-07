#perform dot product of two vectors
vec1=[1,2]
vec2=[4,5]
def dot(a,b):
	dp=0
	for i in range(0,len(vec1)):
		for j in range(0,len(b)):
			if i==j:
				dp=dp+a[i]*b[j]
		return dp
print(dot(a,b))


