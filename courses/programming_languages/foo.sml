fun pow (x:int, y:int) = (* correct only for y >= 0 *)
  if y=0
  then 1
  else x * pow(x,y-1)

fun sway (pr: int*bool)=
  (#2 pr, #1 pr)

fun div_mod (x: int, y : int)=
  (x div y, x mod y)

fun sort_pair (pr: int*int)=
  if (#1 pr) > (#2 pr)
  then (#2 pr, #1 pr)
  else pr

fun sum_list (xs: int list)=
  if null xs
  then 0
  else hd xs + sum_list(tl xs)

fun list_product (xs: int list) = 
  if null xs
  then 1
  else hd xs * list_product(tl xs)

fun countdown(x: int) = 
  if x = 0
  then []
  else x::countdown(x-1)

fun append (xs: int list, ys: int list) =
  if null xs
  then ys
  else (hd xs) :: append(tl xs, ys)

fun factorial (n: int) = 
  if n = 0
  then 1
  else n*factorial(n-1)

fun factorial2 (n: int) = 
  list_product( countdown(n))

fun count_from1 (x: int) =
  let
    fun count(from: int) = 
      if from = x
      then x::[]
      else from :: count(from+1)
  in
    count(1)
  end




