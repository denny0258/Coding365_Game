
cdef extern from '../test2.c':
    cpdef int main()
    cpdef int get(int x, int y)
    cpdef int a[20][20]

def geta():
    return a