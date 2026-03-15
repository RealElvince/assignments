
import numpy as np

# Given vectors
vectors = np.array([
    [1,0,1],
    [1,1,0],
    [0,1,0]
], dtype=float)

def gram_schmidt(vectors):
    ortho_basis = []

    for v in vectors:
        w = v.copy()

        for u in ortho_basis:
            # subtract projection of v onto u
            projection = (np.dot(v, u) / np.dot(u, u)) * u
            w = w - projection

        norm_w = np.linalg.norm(w)

        if norm_w > 1e-10:
            ortho_basis.append(w / norm_w)

    return np.array(ortho_basis)


result = gram_schmidt(vectors)

print("Orthonormal basis:")
for vec in result:
    print(vec)
