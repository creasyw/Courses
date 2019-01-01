package week5

object week5_list {
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet

  def last[T](xs: List[T]): T = xs match {
    case List() => throw new Error("Last of Empty List!")
    case List(x) => x
    case y :: ys => last(ys)
  }                                               //> last: [T](xs: List[T])T

  def init[T](xs: List[T]): List[T] = xs match {
    case List() => throw new Error("init of empty list!")
    case List(x) => List()
    case y :: ys => y :: init(ys)
  }                                               //> init: [T](xs: List[T])List[T]

  def concat[T](xs: List[T], ys: List[T]): List[T] = xs match {
    case List() => ys
    case z :: zs => z :: concat(zs, ys)
  }                                               //> concat: [T](xs: List[T], ys: List[T])List[T]

  def reverse[T](xs: List[T]): List[T] = xs match {
    case List() => xs
    case y :: ys => reverse(ys) ++ List(y)
  }                                               //> reverse: [T](xs: List[T])List[T]

  def removeAt[T](xs: List[T], n: Int): List[T] = (xs take n) ::: (xs drop n + 1)
                                                  //> removeAt: [T](xs: List[T], n: Int)List[T]

  removeAt(List(1, 2, 3, 4), 2)                   //> res0: List[Int] = List(1, 2, 4)

}