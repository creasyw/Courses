package week5
import math.Ordering
object week5_sort {
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet

  def msort[T](xs: List[T])(implicit ord: Ordering[T]): List[T] = {
    val n = xs.length / 2
    if (n == 0) xs
    else {

      def merge(xs: List[T], ys: List[T]): List[T] = (xs, ys) match {
        case (Nil, ys) => ys
        case (xs, Nil) => xs
        case (x :: xx, y :: yy) => if (ord.lt(x, y)) x :: merge(xx, ys) else y :: merge(xs, yy)
      }

      val (fst, snd) = xs splitAt n
      merge(msort(fst), msort(snd))
    }
  }                                               //> msort: [T](xs: List[T])(implicit ord: scala.math.Ordering[T])List[T]

  val nums = List(2, 3, 4, 9, -5, 6)              //> nums  : List[Int] = List(2, 3, 4, 9, -5, 6)
  msort(nums)                                     //> res0: List[Int] = List(-5, 2, 3, 4, 6, 9)

}