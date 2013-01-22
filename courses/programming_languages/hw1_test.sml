(* test the 1st question *)
is_older((1988,6,28), (1988,6,28)) = false;
is_older((1988,6,28), (~1988,6,28)) = false;
is_older((1988,6,28), (1988,6,29)) = true;
is_older((1988,6,28), (1988,6,27)) = false;

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



