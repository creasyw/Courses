package week6

object week6_collection {
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet

  def product1(xs: Vector[Double], ys: Vector[Double]): Double =
    (xs zip ys).map { case (x, y) => x * y }.sum  //> product1: (xs: Vector[Double], ys: Vector[Double])Double
    
    def product2 (xs: Vector[Double], ys: Vector[Double]): Double =
    (for ((x,y) <- xs zip ys) yield x*y).sum      //> product2: (xs: Vector[Double], ys: Vector[Double])Double

  def isPrime(n: Int): Boolean =
    (2 until (Math.sqrt(n)).toInt).forall(d => n % d == 0)
                                                  //> isPrime: (n: Int)Boolean

  isPrime(10)                                     //> res0: Boolean = true
  isPrime(23)                                     //> res1: Boolean = false
}