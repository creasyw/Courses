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


