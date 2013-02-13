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

