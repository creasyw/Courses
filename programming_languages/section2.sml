
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


fun sum_triple1 triple =
  case triple of
       (x, y, z) => x+y+z
fun sum_triple2 triple = 
  let val (x, y, z) = triple
  in x+y+z
  end
fun sum_triple3 (x,y,z) =
  x+y+z

fun same_thing (x,y) =
  if x = y then "yes" else "no"

exception ListLengthMismatch
fun zip3 list_triple = 
  case list_triple of
       ([],[],[]) => []
     | (hd1::tl1,hd2::tl2,hd3::tl3) => (hd1,hd2,hd3)::zip3(tl1,tl2,tl3)
     | _ => raise ListLengthMismatch

fun unzip3 lst =
  case lst of
       [] =>([],[],[])
     | (a,b,c)::tl => let val (l1,l2,l3) = unzip3 tl
                      in (a::l1, b::l2, c::l3)
                      end


fun nondecreasing lst =
  case lst of
       [] => true
     | _ ::[] => true
     | head::(neck::rest) => head<=neck andalso nondecreasing(neck::rest)

fun tail_sum xs =
  let fun aux (xs, acc) =
        case xs of
             [] => acc
           | x:: xs' => aux(xs', x+acc)
  in
    aux(xs, 0)
  end

fun rev xs =
  let fun aux(xs, acc) =
        case xs of
             [] => acc
           | x::xs' => aux(xs', x::acc)
  in aux(xs,[])
  end


