
datatype mytype = TwoInts of int*int
                | Str of string
                | Pizza

fun f x =
  case x of
       Pizza => 3
     | Str s => String.size s
     | TwoInts(i1, i2) => i1+i2


datatype rank = Jack | Queen | King | Ace | Num of int
datatype suit = Club | Diamond | Heart | Spade

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
max_constant(x)



