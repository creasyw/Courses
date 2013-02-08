(* 1 *)
only_capitals ["Acs", "aBc", "kaka", "Why me", "so What"];

(* 2 *)
longest_string1 ["Acs", "aBc", "kaka", "Why me ", "so What"];

(* 3 *)
longest_string2 ["Acs", "aBc", "kaka", "Why me ", "so What"];

(* 4 *)
longest_string3 ["Acs", "aBc", "kaka", "Why me ", "so What"];
longest_string4 ["Acs", "aBc", "kaka", "Why me ", "so What"];

(* 5 *)
longest_capitalized ["Acs", "aBc", "kaka", "Why me", "so What"];

(* 6 *)
rev_string "How are you";

(* 7 *) 
first_answer (fn x=>if x>5 then SOME([x]) else NONE) [1,2,3,4,5,6,7];
(*first_answer (fn x=>if x>5 then SOME([x]) else NONE) [1,2,3,4];*)

(* 8 *) 
all_answers (fn x=>if x>5 then SOME([x]) else NONE) [1,2,3,4,5,6,7];
all_answers (fn x=>if x>5 then SOME([x]) else NONE) [1,2,3,4];
all_answers (fn x=>if x>5 then SOME([x]) else NONE) [];

(* 9 *)
val a = TupleP [Wildcard, Wildcard, UnitP, Wildcard, Variable "qwerty",
Wildcard];
count_wildcards a; (* returns  4 *)
count_wild_and_variable_lengths a;
val pat1 = TupleP([ConstP 12, Variable "var1", ConstructorP("constr1",
Wildcard)]);
val pat2 = TupleP([Variable "var", Wildcard, TupleP([Variable "var", Wildcard,
TupleP([Variable "var", Wildcard])])]);
val a09c1 = count_some_var("var1", pat1) = 1;
val a09c2 = count_some_var("whatever", UnitP) = 0;
val a09c3 = count_some_var("var", pat2) = 3;

