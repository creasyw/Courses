(* Coursera Programming Languages, Homework 3, Provided Code *)

exception NoAnswer

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let 
	val r = g f1 f2 
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x  (* x is a string *)
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end

(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

(**** you can put all your code here ****)

(* 1 *)
fun only_capitals xs =
  List.filter (fn x=> Char.isUpper(String.sub(x,0))) xs

(* 2 *)
fun longest_string1 xs =
  foldl (fn (x,y)=> if (String.size x) > (String.size y) then x else y) "" xs

(* 3 *)
fun longest_string2 xs =
  foldl (fn (x,y)=> if (String.size x) >= (String.size y) then x else y) "" xs

(* 4 *)
fun longest_string_helper f xs =
  foldl (fn (x,y)=> if f(String.size x, String.size y) then x else y) "" xs

fun longest_string3 xs =
  let val tester = longest_string_helper (fn (x,y)=> x>y)
  in tester xs
  end

fun longest_string4 xs =
  let val tester = longest_string_helper (fn (x,y)=> x>=y)
  in tester xs
  end

(* 5 *)
(* Once I use "o" REPL shows "illegal token", so I define infix instead *)
infix |>
fun x |> f = f x
fun longest_capitalized xs =  xs |> only_capitals |> longest_string1

(* 6 *)
fun rev_string x = String.implode(rev (String.explode x))

(* 7 *)
fun first_answer f xs =
    case xs of
         [] => raise NoAnswer
       | x ::xs'=> case f(x) of
                        NONE => first_answer f xs'
                      | SOME v => v

(* 8 *)
fun all_answers f xs =
  let
    fun local_helper(acc,ys) =
      case ys of
           [] => acc
         | y::ys' => case f(y) of
                          NONE => local_helper(acc,ys')
                        | SOME v => case acc of
                                         NONE => local_helper(SOME v, ys')
                                       | _ => local_helper(SOME(v@(valOf acc)), ys')
  in 
    case xs of
         [] => SOME []
       | _ => local_helper(NONE, xs)
  end


(* 9 *)
fun count_wildcards p = g (fn()=>1) (fn x=>0) p
fun count_wild_and_variable_lengths p = g (fn()=>1) (fn x=>String.size x) p
fun count_some_var (s, p) = g (fn()=>0) (fn x=> if x=s then 1 else 0) p

(* 10 *)
fun check_pat p =
  let
    fun disassemble pt =
      case pt of
           Variable x => [x]
         | ConstructorP(_, pl) => disassemble pl
         | TupleP ps => List.foldl (fn (x, y) => (disassemble x)@y) [] ps
         | _ => []
            
    fun duplicated sl =
      case sl of
           [] => true
         | x::xs => if not (List.exists (fn y=> y=x) xs)
                    then duplicated xs
                    else false
  in duplicated(disassemble p)
  end















