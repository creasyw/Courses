import sys
w = sys.stdout.write

#class Node:
#    def __init__(self, cargo=None, next=None):
#        self.car = cargo
#        self.cdr = next
#    def __str__(self):
#        return str(self.car)
#
#def printlst(lst):
#    if lst:
#        w("%s " %lst)
#        printlst(lst.cdr)
#    else:
#        w("nil\n")

cons = lambda el, lst: (el, lst)
mklist = lambda *args: reduce(lambda lst, el: cons(el, lst), reversed(args), None)
mklist1 = lambda pylist: reduce(lambda lst, el: cons(el, lst), pylist[::-1], None)
car = lambda lst: lst[0] if lst else lst
cdr = lambda lst: lst[1] if lst else lst
cadr = lambda lst: lst[1][0] if lst and lst[1] else lst
cddr = lambda lst: lst[1][1] if lst and lst[1] else lst
nth = lambda n, lst: nth(n-1, cdr(lst)) if n > 0 else car(lst)
length  = lambda lst, count=0: length(cdr(lst), count+1) if lst else count
begin   = lambda *args: args[-1]
display = lambda lst: begin(w("%s " % car(lst)), display(cdr(lst))) if lst else w("nil\n")

# Question:
# Write a function that takes in an arbitrary length singly-linked list and
# returns the pairwise reverse of that list. In other words, if I pass in the
# list A->B->C->D->E->F the function should return the list B->A->D->C->F->E


def make_list(lst):
    return mklist1(lst)



