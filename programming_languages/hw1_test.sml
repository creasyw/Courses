(* test the 1st question *)
is_older((1988,6,28), (1988,6,28)) = false;
is_older((1988,6,28), (~1988,6,28)) = false;
is_older((1988,6,28), (1988,6,29)) = true;
is_older((1988,6,28), (1988,6,27)) = false;
is_older((1,2,98), (1,17,83)) = true;
is_older((1,2,98), (6,7,8)) = true;

(* test the 2nd question *)
number_in_month([(1965,10,1),(1949,9,1),(1983,10,25)],10) = 2;

(* test the 3rd question *)
number_in_months([(1965,10,1),(1949,9,1),(1983,10,25)],[9,10]) = 3;
number_in_months([(1965,10,1),(1949,9,1),(1983,10,25)],[1,2,3]) = 0;

(* test the 4th question *)
dates_in_month([(1965,10,1),(1949,9,1),(1983,10,25)],10) =
[(1965,10,1),(1983,10,25)];
dates_in_month([(1965,10,1),(1949,9,1),(1983,10,25)],1) = [];

(* test the 5th question *)
dates_in_months([(1965,10,1),(1949,9,1),(1983,10,25)],[9,10]) =
[(1949,9,1),(1965,10,1),(1983,10,25)];
dates_in_months([(1965,10,1),(1949,9,1),(1983,10,25)],[1,2,3]) = [];

(* test the 6th question *)
get_nth(["a","b","c","d"],1) = "a";
get_nth(["a","b","c","d"],2) = "b";
(* get_nth(["a","b","c","d"],10);  ==> this would get exception *)

(* test the 7th question *)
date_to_string((1988,6,28)) = "June 28, 1988";

(* 8th *)
number_before_reaching_sum(10, [1,2,3,4,5,6,7]) = 3;
number_before_reaching_sum(1, [1,2,3,4,5,6,7]) = 0;
(* number_before_reaching_sum(30, [1,2,3,4,5,6,7]); ==> exception *)

(* 9th *)
what_month(32) = 2;

(* 10th *)
month_range(28, 32) = [1,1,1,1,2];

(* 11th *)
oldest([]) = NONE;
oldest([(1988,6,28)]) = SOME (1988,6,28);
oldest([(1988,6,28), (1988,6,29)]) = SOME (1988,6,28);
oldest([(5,5,2),(5,10,2),(5,2,2),(5,12,2)]) = SOME (5,2,2);
(* 12th *)
number_in_months_challenge([(1965,10,1),(1949,9,1),(1983,10,25)],[9,10,10,10]) = 3;
dates_in_months_challenge([(1965,10,1),(1949,9,1),(1983,10,25)],[9,10,10,10,10])
= [(1949,9,1),(1965,10,1),(1983,10,25)];




