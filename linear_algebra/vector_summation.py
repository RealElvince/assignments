import numpy as np

def vector_sum(v1,v2):

    v1 = np.array(v1)
    v2 = np.array(v2)


    if v1.shape != v2.shape:
        raise ValueError("Vectors must be of the same length")
    

    return v1 + v2

vector_one = [1,2,4,5,6]
vector_two = [3,4,5,6,2]

result = vector_sum(vector_one,vector_two)

print("The sum of two vectors:",result)


# dot product of two vectors

def dot_product(vector1,vector2):

    first_vector = np.array(vector1)
    second_vector = np.array(vector2)


    if first_vector.shape != second_vector.shape:
        raise ValueError("Vectors must be of the same length")
    

    return np.dot(first_vector,second_vector)




product = dot_product(vector_one,vector_one)

print("The dot product is:",product)