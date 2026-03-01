import numpy as np

def vector_sum(v1,v2):

    v1 = np.array(v1)
    v2 = np.array(v2)


    if v1.shape != v2.shape:
        raise ValueError("Vectors must be of the same length")
    

    return v1 + v2

vector_one = [1,2,4,5,6]
vector_two = [3,4,5]

result = vector_sum(vector_one,vector_two)

print("The sum of two vectors:",result)