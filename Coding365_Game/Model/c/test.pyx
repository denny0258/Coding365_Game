
cdef extern from "../test.c":
    cpdef char suit;
    cpdef int number;
    cpdef int next();
    cpdef int main();

def shuffle():
    main()

def get():
    ok = next()
    if ok==0:
        return None
    return {
        "suit": chr(suit),
        "number": number
    }
