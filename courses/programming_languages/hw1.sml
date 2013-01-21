fun is_legal (y:int, m:int, d:int) =
  (* Test if the input date is legal *)
  if y>0 then 1
  else if m>0 then 1
  else if m<13 then 1
  else if d>0 then 1
  else if d<32 then 1
  else 0

fun is_reasonable(m:int, d:int) =
  case m of
       1 => d<31
     | 2 => d<28
       EQUALOP false


