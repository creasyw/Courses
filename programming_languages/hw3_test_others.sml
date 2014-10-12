fun t_responder s = if String.sub(s, 0) = #"t" then SOME s else NONE;
fun chars_responder s = if String.size s > 0 then SOME (explode s) else NONE;

val pat1 = TupleP([ConstP 12, Variable "var1", ConstructorP("constr1",
Wildcard)]);
val pat2 = TupleP([Variable "var", Wildcard, TupleP([Variable "var", Wildcard,
TupleP([Variable "var", Wildcard])])]);
val pat3 = TupleP([Variable "var1", Wildcard, TupleP([Variable "var2", Wildcard,
TupleP([Variable "var3", Wildcard])])]);
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

val _ = print "\nAssertions:\n";
val a0101 = only_capitals(["Cap","small"]) = ["Cap"];
val a0201 = longest_string1([]) = "";
val a0202 = longest_string1(["a","bb","cc"]) = "bb";
val a0301 = longest_string2(["a","bb","cc"]) = "cc";
val a0401 = longest_string3([]) = "";
val a0402 = longest_string3(["a","bb","cc"]) = "bb";
val a0403 = longest_string4(["a","bb","cc"]) = "cc";
val a0501 = longest_capitalized(["Short","longbutsmall","Longer"]) = "Longer";
val a0601 = rev_string("sdrawkcab") = "backwards";
val a0701 = first_answer t_responder ["one", "two", "three"] = "two";
val a0702 = (first_answer t_responder ["one", "other"] handle NoAnswer =>
"none") = "none";
val a0801 = all_answers chars_responder ["one", "two"] = SOME
[#"o",#"n",#"e",#"t",#"w",#"o"];
val a0802 = all_answers chars_responder ["one", "two", ""] = NONE;
val a09a1 = count_wildcards pat1 = 1;
val a09a2 = count_wildcards UnitP = 0;
val a09a3 = count_wildcards pat2 = 3;
val a09b1 = count_wild_and_variable_lengths pat1 = 5;
val a09b2 = count_wild_and_variable_lengths UnitP = 0;
val a09b3 = count_wild_and_variable_lengths pat2 = 12;
val a09c1 = count_some_var("var1", pat1) = 1;
val a09c2 = count_some_var("whatever", UnitP) = 0;
val a09c3 = count_some_var("var", pat2) = 3;
val a1001 = check_pat UnitP;
val a1002 = check_pat pat1;
val a1003 = check_pat pat3;
val a1004 = not (check_pat pat2);
val a1101 = match(Unit, UnitP) = SOME [];
val a1102 = match(val1ok1, pat1) = SOME [("var1", Constructor("blah", Unit))];
val a1103 = match(val1ok2, pat1) = SOME [("var1", Const 13)];
val a1104 = match(val1ko1, pat1) = NONE;
val a1105 = match(val1ko2, pat1) = NONE;
val a1106 = match(val1ko3, pat1) = NONE;
val a1107 = match(val3ok1, pat3) = SOME [("var1", Const 1), ("var2", Const 2),
("var3", Const 3)];
val a1108 = match(val3ok2, pat3) = SOME [("var1", Unit), ("var2", Unit),
("var3", Unit)];
val a1109 = match(val3ko1, pat3) = NONE;
val a1201 = first_match val1ok1 [pat2, pat1] = SOME [("var1",
Constructor("blah", Unit))];
val a1202 = first_match val1ok1 [Wildcard, pat1] = SOME [];
val a1203 = first_match val1ko1 [pat1, pat2, pat3, UnitP] = NONE; 
val a1204 = first_match val3ok1 [pat1, UnitP, pat3] = SOME [("var1", Const 1),
("var2", Const 2), ("var3", Const 3)]; 
