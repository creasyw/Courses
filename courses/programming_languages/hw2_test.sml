(* Dan Grossman, Coursera PL, HW2 Provided Tests *)

(* These are just two tests for problem 2; you will want more.

   Naturally these tests and your tests will use bindings defined 
   in your solution, in particular the officiate function, 
   so they will not type-check if officiate is not defined.
 *)

(* testing question 1 *)
all_except_option("he", ["he", "she", "it"]);
all_except_option("I", ["he", "she", "it"]);

get_substitutions1([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]],
"Fred");
get_substitutions2([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]],
"Fred");
get_substitutions1([["Fred","Fredrick"],["Jeff","Jeffrey"],["Geoff","Jeff","Jeffrey"]],
"Jeff");
get_substitutions2([["Fred","Fredrick"],["Jeff","Jeffrey"],["Geoff","Jeff","Jeffrey"]],
"Jeff");

similar_names([["Fred","Fredrick"],["Elizabeth","Betty"],["Freddie","Fred","F"]],{first="Fred",
middle="W", last="Smith"});


(* testing question 2 *)
card_color(Clubs, Jack);
card_color(Hearts, Num 10);
card_value(Clubs, Jack);
card_value(Hearts, Ace);
card_value(Diamonds, Num 3);

remove_card([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num 3)],
(Diamonds, Num 3), IllegalMove);
(* the following will generate exception *)
(* remove_card([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num 3)],
(Diamonds, Num 5), IllegalMove);
*)
all_same_color([(Clubs, Jack)]);
all_same_color([(Clubs, Jack),(Clubs, Num 10),(Clubs, Ace),(Clubs, Num
3)]);
all_same_color([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num
3)]);
sum_cards([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num 3)]);
sum_cards([(Clubs, Jack)]);
score([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num 3)], 30);
score([(Clubs, Jack),(Spades, Num 10),(Clubs, Ace),(Clubs, Num 3)], 30);
score([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num 3)], 40);
score([(Clubs, Jack),(Clubs, Num 10),(Clubs, Ace),(Clubs, Num 3)], 40);

(* test move is empty *)
officiate([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num 3),
(Diamonds, Num 3)], [Draw, Draw, Draw, Draw], 40) = 6;
(* test card is empty *)
officiate([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num 3),
(Diamonds, Num 3)], [Draw, Draw, Draw, Draw, Draw, Draw, Draw], 40) = 3;

(* test over-draw *)
officiate([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num 3)],
[Draw, Draw, Draw, Draw], 30) = 3;

score_challenge([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num 3)],
30) = 6;
score_challenge([(Clubs, Jack),(Hearts, Num 10),(Hearts, Ace),(Diamonds, Num 3)],
40) = 6;
score_challenge([(Clubs, Jack),(Hearts, Num 10),(Hearts, Jack),(Diamonds, Num 3)],
30) = 9;


fun provided_test1 () = (* correct behavior: raise IllegalMove *)
    let val cards = [(Clubs,Jack),(Spades,Num(8))]
	val moves = [Draw,Discard(Hearts,Jack)]
    in
	officiate(cards,moves,42)
    end

fun provided_test2 () = (* correct behavior: return 3 *)
    let val cards = [(Clubs,Ace),(Spades,Ace),(Clubs,Ace),(Spades,Ace)]
	val moves = [Draw,Draw,Draw,Draw,Draw]
    in
 	officiate(cards,moves,42)
    end


(* testing file written by Wan Kong Yew *)
fun oc_test1 () =
      let val cards = [(Spades, Ace), (Diamonds, Num(10)), (Clubs, Queen),
      (Hearts, Num(9)), (Spades, Num(5)), (Diamonds, Num(3))]
              val moves = [Draw, Draw, Draw, Draw, Draw, Draw]
                  in
                            officiate_challenge(cards, moves, 42)
                                end

fun oc_test2 () =
      let val cards = [(Spades, Ace), (Diamonds, Num(10)), (Clubs, Queen),
      (Hearts, Num(9)), (Spades, Num(5)), (Diamonds, Num(3)), (Hearts, Ace),
      (Hearts, Jack), (Diamonds, Ace), (Clubs, Num(8))]
              val moves = [Draw, Draw, Draw, Draw, Draw, Draw, Discard(Spades,
              Ace), Draw, Draw, Draw]
                  in
                            officiate_challenge(cards, moves, 42)
                                end

fun oc_test3 () =
      let val cards = [(Spades, Ace), (Diamonds, Num(10)), (Clubs, Queen),
      (Hearts, Num(9)), (Spades, Num(5)), (Diamonds, Num(3)), (Hearts, Ace),
      (Hearts, Jack), (Diamonds, Ace), (Clubs, Num(8))]
              val moves = [Draw, Draw, Draw, Draw, Draw, Draw, Discard(Diamonds,
              Num(10)), Discard(Clubs, Queen), Draw, Draw, Draw]
                  in
                            officiate_challenge(cards, moves, 42)
                                end

fun oc_test4 () =
      let val cards = [(Spades, Ace), (Diamonds, Num(10)), (Clubs, Queen),
      (Hearts, Num(9)), (Spades, Num(5)), (Diamonds, Num(3)), (Hearts, Ace),
      (Hearts, Jack), (Diamonds, Ace), (Clubs, Num(8))]
              val moves = [Draw, Draw, Draw, Draw, Draw, Draw, Discard(Spades,
              Ace), Discard(Spades, Num(5)), Draw, Draw, Draw, Draw]
                  in
                            officiate_challenge(cards, moves, 42)
                                end

val officiate_challenge_test1 = oc_test1() = 4;
val officiate_challenge_test2 = oc_test2() = 18;
val officiate_challenge_test3 = oc_test3() = 2;
val officiate_challenge_test4 = oc_test4() = 3;
