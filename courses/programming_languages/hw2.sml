(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)
(* 1-a *)
fun all_except_option (y, ys) =
  let fun iterate_list (head, tail) =
        case tail of
             [] => NONE
           | x::xs' => if same_string(x, y) then SOME(head@xs')
                        else iterate_list(head@[x], xs')
  in
    iterate_list([], ys)
  end

(* 1-b *)
fun get_substitutions1 (lst:string list list, s:string) =
  case lst of
       [] => []
     | x::xs => case all_except_option(s, x) of
                     NONE => get_substitutions1(xs, s)
                   | SOME(x) => x @ get_substitutions1(xs, s)

(* 1-c *)
fun get_substitutions2 (lst:string list list, s:string) =
  let fun find_lst (xs:string list list, result:string list) =
        case xs of
             [] => result
           | head::tail => case all_except_option(s, head) of
                                NONE => find_lst(tail, result)
                              | SOME(x) => find_lst(tail, x@result)
  in
    find_lst(lst, [])
  end

(* 1-d *)
fun similar_names (lst:string list list, {first:string, middle:string,
  last:string}) =
  let val candidates = get_substitutions2(lst, first)
      fun assemble_name (cand:string list) =
        case cand of
             [] => [{first=first, last=last, middle=middle}]
           | x::xs => assemble_name(xs)@[{first=x, last=last, middle=middle}]
  in
    assemble_name(candidates)
  end


(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)
(* 2-a *)
fun card_color c =
  case c of
       (Spades, _) => Black
     | (Clubs, _) => Black
     | _ => Red

(* 2-b *)
fun card_value c =
  case c of
       (_, Ace) => 11
     | (_, Num i) => i
     | _ => 10

(* 2-c *)
fun remove_card (cs, c, ex) =
  let fun iterate_list (head, tail) =
        case tail of
             [] => raise ex
           | x::xs' => if x = c then head@xs'
                        else iterate_list(head@[x], xs')
  in
    iterate_list([], cs)
  end

(* 2-d *)
fun all_same_color cs =
  case cs of
       [] => true
     | _::[] => true
     | head::(neck::tail) => card_color(head)=card_color(neck) andalso
       all_same_color(tail)




