package week5

object week5_higher_order_list {
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet

  def squareList1(xs: List[Int]): List[Int] = xs match {
    case Nil => Nil
    case y :: ys => y * y :: squareList1(ys)
  }                                               //> squareList1: (xs: List[Int])List[Int]

  def squareList(xs: List[Int]): List[Int] =
    xs map (x => x * x)                           //> squareList: (xs: List[Int])List[Int]

  def nums = List(2, -4, 5, 7, 1)                 //> nums: => List[Int]
  nums partition (x => x > 0)                     //> res0: (List[Int], List[Int]) = (List(2, 5, 7, 1),List(-4))
  nums dropWhile (x => x > 0)                     //> res1: List[Int] = List(-4, 5, 7, 1)

  def data = List("a", "a", "a", "b", "c", "c", "a")
                                                  //> data: => List[String]

  def pack[T](xs: List[T]): List[List[T]] = xs match {
    case Nil => Nil
    case x :: xx =>
      val (first, rest) = xs span (y => y == x)
      first :: pack(rest)
  }                                               //> pack: [T](xs: List[T])List[List[T]]

  pack(data)                                      //> res2: List[List[String]] = List(List(a, a, a), List(b), List(c, c), List(a))
                                                  //| 
  def encode[T](xs: List[T]): List[(T, Int)] =
    pack(xs) map (x => (x.head, x.length))        //> encode: [T](xs: List[T])List[(T, Int)]

  encode(data)                                    //> res3: List[(String, Int)] = List((a,3), (b,1), (c,2), (a,1))
}