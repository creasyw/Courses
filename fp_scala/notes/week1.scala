package week1

object week1 {
  1 + 2                                           //> res0: Int(3) = 3
  def and(x: Boolean, y: => Boolean) = if (x) y else false
                                                  //> and: (x: Boolean, y: => Boolean)Boolean
  def loop: Boolean = loop                        //> loop: => Boolean

  def abs(x: Double) = if (x < 0) -x else x       //> abs: (x: Double)Double

  def sqrt(x: Double) = {

    def sqrtIter(guess: Double): Double =
      if (isGoodEnough(guess)) guess
      else sqrtIter(improve(guess))

    def isGoodEnough(guess: Double) =
      abs(guess * guess - x) / x < 0.001

    def improve(guess: Double) =
      (guess + x / guess) / 2

    sqrtIter(1.0)
  }                                               //> sqrt: (x: Double)Double

  // testing
  sqrt(2)                                         //> res1: Double = 1.4142156862745097
  sqrt(4)                                         //> res2: Double = 2.000609756097561
  // very small number
  sqrt(1e-6)                                      //> res3: Double = 0.0010000001533016628
  // very large number
  sqrt(1e60)                                      //> res4: Double = 1.0000788456669446E30

  def gcd(a: Int, b: Int): Int =
    if (b == 0) a else gcd(b, a % b)              //> gcd: (a: Int, b: Int)Int
  // testing
  gcd(14, 21)                                     //> res5: Int = 7

  def factorial(n: Int): Int = {
    def helper(n: Int, acc: Int): Int =
      if (n == 0) acc else helper(n - 1, n * acc)
    helper(n, 1)
  }                                               //> factorial: (n: Int)Int
  // testing
  factorial(10)                                   //> res6: Int = 3628800
}
