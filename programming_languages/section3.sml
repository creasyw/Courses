fun double x = 2*x
fun incr x = x+1
val a_touple = (double, incr, double(incr 7))
val eighteen = (#1 a_touple) 9

fun n_times(f, n, x) =
  if n=0
  then x
  else f(n_times(f, n-1, x))
fun addition(n, x) = n_times(fn x=>x+1, n, x)
fun double_n(n, x) = n_times((fn x=>x+x), n, x)

(* test *)
val x1 = n_times(double, 4, 7)
val x3 = n_times(tl, 2, [1,2,3,4])


fun map (f, xs) =
  case xs of
       [] => []
     | x::xs' => (f x)::map(f, xs')

val x1 = map((fn x=>x+1), [4,8,12,16])
val x2 = map(hd, [[1,2],[3,4],[5,6,7]])


fun filter (f, xs) =
  case xs of
       [] => []
     | x::xs' => if f x
                 then x :: (filter (f,xs'))
                 else filter(f, xs')

fun is_even v = (v mod 2 = 0)
fun all_even xs =filter(is_even, xs)
fun all_even_snd xs = filter((fn(_,v)=>is_even v), xs)


fun double_or_triple f =
  if f 7
  then fn x=>x*2
  else fn x=>x*3

val double = double_or_triple (fn x=>x-3=4)


fun all_shorter_than_1 (xs, s) =
  filter((fn x=> String.size x< (print "!\n"; String.size s)), xs)
fun all_shorter_than_2 (xs, s) =
  let val i = (print "!\n"; String.size s)
  in
    filter ((fn x => String.size x< i), xs)
  end


fun fold (f, acc, xs) =
  case xs of
       [] => acc
     | x::xs' => fold(f, f(acc, x), xs')

fun compose(f, g) = fn x => f(g x)

infix |>
fun x |> f = f x
fun sqrt_of_abs i =  i |> abs |> Real.fromInt |> Math.sqrt 

fun backup1 (f,g) = fn x => case f x of
                                 NONE => g x
                               | SOME y => y
fun backup2 (f,g) = fn x => f x handle _ => g x

fun sorted_nicer x y z = z>=y andalso y>=x


fun exists predicate xs =
  case xs of
       [] => false
     | x::xs' => predicate x orelse exists predicate xs'
val no = exists(fn x=> x=7) [4,5,6,9]
val haszero = exists (fn x=>x=0)
val incrementAll = List.map (fn x=>x+1)
val removeZero = List.filter (fn x => x<>0)

fun curry f x y = f(x,y)
fun uncurry f(x, y) = f x y
fun other_curry f x y = f y x

fun range (i,j) = if i>j then [] else i::range(i+1,j)
val countup = curry range 1
val xs = countup 7


datatype set = S of { insert: int->set, member: int->bool, size: unit->int}
val empty_set = 
  let 
    fun make_set xs =
      let
        fun contains i = List.exists (fn j=> i=j) xs
      in
        S { insert = fn i => if contains i
                             then make_set xs
                             else make_set (i::xs),
            member = contains,
            size = fn () => length xs
          }
      end
  in
    make_set []
  end

fun use_sets () =
  let
    val S s1 = empty_set
    val S s2 = (#insert s1) 34
    val S s3 = (#insert s2) 34
    val S s4 = #insert s3 19
  in
    if (#member s4) 42
    then 99
    else if (#member s4) 19
    then 17+(#size s3)()
    else 0
  end






