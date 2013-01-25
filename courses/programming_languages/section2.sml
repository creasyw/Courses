
datatype mytype = TwoInts of int*int
                | Str of string
                | Pizza

fun f x =
  case x of
       Pizza => 3
     | Str s => String.size s
     | TwoInts(i1, i2) => i1+i2


datatype exp = Constant of int
           | Negate of exp
           | Add of exp*exp
           | Multiply of exp*exp

fun eval e = 
  case e of
       Constant i       => i
     | Negate e2        => ~(eval e2)
     | Add (e1, e2)     => (eval e1) + (eval e2)
     | Multiply(e1, e2) => (eval e1) * (eval e2)

fun max_constant e = 
  case e of
       Constant i       => i
     | Negate e2        => max_constant(e2)
     | Add(e1,e2)       => Int.max(max_constant(e1), max_constant(e2))
     | Multiply(e1,e2)  => Int.max(max_constant(e1), max_constant(e2))
val x = Add(Constant 19, Negate(Constant 4));
max_constant(x);

datatype rank = Jack | Queen | King | Ace | Num of int
datatype suit = Club | Diamond | Heart | Spade
type card = suit*rank

fun is_queen_of_spades (c:card) = 
  #1 c = Spade andalso #2 c = Queen

val c1: card = (Diamond, Ace)
val c2: suit*rank = (Heart, Ace)
val c3 = (Spade, Ace)

datatype my_int_list = Empty | Cons of int*my_int_list
val x = Cons(4,Cons(23,Cons(2008,Empty)))
fun append_my_list (xs, ys) =
  case xs of
       Empty    => ys
     | Cons(x, xs')     => Cons(x, append_my_list(xs', ys))

fun sum_list xs =
  case xs of
       []       => 0
     | x::xs'   => x+sum_list(xs')






