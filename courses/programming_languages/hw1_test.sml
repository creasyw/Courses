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
