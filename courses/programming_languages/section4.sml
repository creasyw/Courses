(* general func for finite state machine *)
fun match xs =
  let fun s_need_one xs =
        case xs of
             [] => true
           | 1::xs' => s_need_two xs'
           | _ => false
    and s_need_two xs =
        case xs of
             [] => false
           | 2::xs' => s_need_one xs'
           | _ => false
  in
    s_need_one xs
  end

(* mutual recursion *)
datatype t1 = Foo of int | Bar of t2
and t2 = Baz of string | Quux of t1

fun no_zeros_or_empty_strings_t1 x =
  case x of
       Foo i => i<>0
     | Bar y => no_zeros_or_empty_strings_t2 y
and no_zeros_or_empty_strings_t2 x =
  case x of
       Baz s => size s <> 0
     | Quux y => no_zeros_or_empty_strings_t1 y

fun no_zeros_or_empty_strings_t1_alternate (f,x) =
  case x of
       Foo i => i<>0
     | Bar y => f y
fun no_zeros_or_empty_strings_t2_alternate x =
  case x of
       Baz s => size s <> 0
     | Quux y => no_zeros_or_empty_strings_t1_alternate
     (no_zeros_or_empty_strings_t2_alternate, y)


(* Module *)
structure Rational1 =
struct
  datatype rational1 = Whole of int | Frac of int*int
  exception BadFrac

  fun gcd (x,y) =
    if x=y
    then x
    else if x<y
         then gcd(x, y-x)
         else gcd(y, x)

  fun reduce r =
    case r of
         Whole _ => r
       | Frac(x,y)=> if x=0
                     then Whole 0
                     else let val d=gcd(abs x, y)
                          in if d=y
                             then Whole(x div d)
                             else Frac(x div d, y div d)
                          end
  fun make_frac (x,y) =
    if y=0
    then raise BadFrac
    else if y<0
         then reduce(Frac (~x, ~y))
         else reduce(Frac (x,y))

  fun add (r1, r2) =
    case (r1, r2) of
         (Whole(i), Whole(j)) => Whole(i+j)
       | (Whole(i), Frac(j,k)) => Frac(j+k*i, k)
       | (Frac(j,k), Whole(i)) => Frac(j+k*i, k)
       | (Frac(a,b), Frac(c,d)) => reduce(Frac(a*d+b*c, b*d))

  fun toString r =
    case r of
         Whole i => Int.toString i
       | Frac(a,b) => (Int.toString a) ^ "/" ^ (Int.toString b)
end



