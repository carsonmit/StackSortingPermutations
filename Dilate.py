def dilateP(vertices, factor):  # Takes vertices v_1,...,v_n and factor c to return cv_1,...,cv_n
    for vertex in vertices:
        for i in range(len(vertex)):
            vertex[i] = vertex[i] * factor
    return vertices
