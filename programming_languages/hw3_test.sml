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
val a0801 = all_answers (fn x=>if x>5 then SOME([x]) else NONE) [1,2,3,4,5,6,7]
= NONE;
val a0802 = all_answers (fn x=>if x>5 then SOME([x]) else NONE) [8,7,3,4] = NONE;
val a0803 = all_answers (fn x=>if x>5 then SOME([x]) else NONE) [8,7,9,10] =
  SOME [10,9,7,8];
val a0804 = all_answers (fn x=>if x>5 then SOME([x]) else NONE) [] = SOME [];

(* 9 *)
val a = TupleP [Wildcard, Wildcard, UnitP, Wildcard, Variable "qwerty",
Wildcard];
count_wildcards a; (* returns  4 *)
count_wild_and_variable_lengths a;
val pat1 = TupleP([ConstP 12, Variable "var1", ConstructorP("constr1",
Wildcard)]);
val pat2 = TupleP([Variable "var", Wildcard, TupleP([Variable "var", Wildcard,
TupleP([Variable "var", Wildcard])])]);
val pat3 = TupleP([Variable "var1", Wildcard, TupleP([Variable "var2", Wildcard,
TupleP([Variable "var3", Wildcard])])]);
val a09c1 = count_some_var("var1", pat1) = 1;
val a09c2 = count_some_var("whatever", UnitP) = 0;
val a09c3 = count_some_var("var", pat2) = 3;

(* 10 *)
(* unit test for helper function 1 *)
(*
val pat3 = [Variable "var", Wildcard, TupleP([Variable "var", Wildcard,
TupleP([Variable "var", Wildcard])])];
disassemble (Variable "var");
disassemble (TupleP([Variable "var", Wildcard,TupleP([Variable "var",
Wildcard])]));
disassemble (Wildcard);
*)
(* unit test for helper function 2 *)
(*
duplicated ["Acs", "aBc", "kaka", "Why me ", "so What"];
duplicated ["Acs", "aBc", "kaka", "Why me ", "kaka", "so What"];
*)
val a1001 = check_pat UnitP;
val a1002 = check_pat pat1;
val a1003 = check_pat pat3;
val a1004 = not (check_pat pat2);

val val1ok1 = Tuple([Const 12, Constructor("blah", Unit), Constructor("constr1",
Tuple([]))]);
val val1ok2 = Tuple([Const 12, Const 13, Constructor("constr1", Const 14)]);
val val1ko1 = Tuple([Const 12, Constructor("blah", Unit), Constructor("constr2",
Tuple([]))]);
val val1ko2 = Tuple([Const 13, Constructor("blah", Unit), Constructor("constr1",
Tuple([]))]);
val val1ko3 = Tuple([Const 13, Constructor("blah", Unit), Unit]);
val val3ok1 = Tuple([Const 1, Unit, Tuple([Const 2, Unit, Tuple([Const 3,
Unit])])]);
val val3ok2 = Tuple([Unit, Const 1, Tuple([Unit, Const 2, Tuple([Unit, Const
3])])]);
val val3ko1 = Tuple([Const 1, Unit, Tuple([Const 2, Unit, Tuple([Const 3])])]); 
val a1101 = match(Unit, UnitP) = SOME [];
val a1102 = match(val1ok1, pat1) = SOME [("var1", Constructor("blah", Unit))];
val a1103 = match(val1ok2, pat1) = SOME [("var1", Const 13)];
val a1104 = match(val1ko1, pat1) = NONE;
val a1105 = match(val1ko2, pat1) = NONE;
val a1106 = match(val1ko3, pat1) = NONE;
val a1107 = match(val3ok1, pat3) = SOME [("var3",Const 3),("var2",Const
2),("var1",Const 1)];
val a1108 = match(val3ok2, pat3) = SOME
[("var3",Unit),("var2",Unit),("var1",Unit)];
val a1109 = match(val3ko1, pat3) = NONE;


val a1201 = first_match val1ok1 [pat2, pat1] = SOME [("var1",
Constructor("blah", Unit))];
val a1202 = first_match val1ok1 [Wildcard, pat1] = SOME [];
val a1203 = first_match val1ko1 [pat1, pat2, pat3, UnitP] = NONE; 
val a1204 = first_match val3ok1 [pat1, UnitP, pat3] = SOME [("var3",Const
3),("var2",Const 2),("var1",Const 1)]; 




