cdef extern from '../shuffle.c':
    cpdef int suit
    cpdef int number
    cpdef void do_init()
    cpdef void do_shuffle()
    cpdef int do_next()

do_init()

def Take_Card(shuffle):
    if shuffle:
        do_shuffle()
    
    if do_next() == 1:
        return ("shdc"[suit-1], number)
    return None

