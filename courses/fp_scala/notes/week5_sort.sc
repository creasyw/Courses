package week5

object week5_sort {
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet

  def merge(xs: List[Int], ys: List[Int]): List[Int] = (xs, ys) match {
    case (Nil, ys) => ys
    case (xs, Nil) => xs
    case (x :: xx, y :: yy) => if (x < y) x :: merge(xx, ys) else y :: merge(xs, yy)
  }                                               //> merge: (xs: List[Int], ys: List[Int])List[Int]

  def msort(xs: List[Int]): List[Int] = {
    val n = xs.length / 2
    if (n == 0) xs
    else {
      val (fst, snd) = xs splitAt n
      merge(msort(fst), msort(snd))
    }
  }                                               //> msort: (xs: List[Int])List[Int]

  val nums = List(2, 3, 4, 9, -5, 6)              //> nums  : List[Int] = List(2, 3, 4, 9, -5, 6)
  msort(nums)                                     //> res0: List[Int] = List(-5, 2, 3, 4, 6, 9)

}