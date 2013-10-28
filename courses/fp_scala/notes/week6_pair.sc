package week6

object week6_pair {
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet
  val n = 7                                       //> n  : Int = 7

  ((1 until n) map (i =>
    (1 until i) map (j => (i, j)))).flatten       //> res0: scala.collection.immutable.IndexedSeq[(Int, Int)] = Vector((2,1), (3,1
                                                  //| ), (3,2), (4,1), (4,2), (4,3), (5,1), (5,2), (5,3), (5,4), (6,1), (6,2), (6,
                                                  //| 3), (6,4), (6,5))

  (1 until n) flatMap (i =>
    (1 until i) map (j => (i, j)))                //> res1: scala.collection.immutable.IndexedSeq[(Int, Int)] = Vector((2,1), (3,1
                                                  //| ), (3,2), (4,1), (4,2), (4,3), (5,1), (5,2), (5,3), (5,4), (6,1), (6,2), (6,
                                                  //| 3), (6,4), (6,5))


}