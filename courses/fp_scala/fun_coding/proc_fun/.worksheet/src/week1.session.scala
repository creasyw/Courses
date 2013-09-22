package week1

object session {;import org.scalaide.worksheet.runtime.library.WorksheetSupport._; def main(args: Array[String])=$execute{;$skip(39); val res$0 = 
  1 + 2;System.out.println("""res0: Int(3) = """ + $show(res$0));$skip(59); 
  def and(x: Boolean, y: => Boolean) = if (x) y else false;System.out.println("""and: (x: Boolean, y: => Boolean)Boolean""");$skip(27); 
  def loop: Boolean = loop;System.out.println("""loop: => Boolean""");$skip(45); 

  def abs(x: Double) = if (x < 0) -x else x;System.out.println("""abs: (x: Double)Double""");$skip(310); 

  def sqrt(x: Double) = {

    def sqrtIter(guess: Double): Double =
      if (isGoodEnough(guess)) guess
      else sqrtIter(improve(guess))

    def isGoodEnough(guess: Double) =
      abs(guess * guess - x) / x < 0.001

    def improve(guess: Double) =
      (guess + x / guess) / 2

    sqrtIter(1.0)
  };System.out.println("""sqrt: (x: Double)Double""");$skip(24); val res$1 = 

  // testing
  sqrt(2);System.out.println("""res1: Double = """ + $show(res$1));$skip(10); val res$2 = 
  sqrt(4);System.out.println("""res2: Double = """ + $show(res$2));$skip(36); val res$3 = 
  // very small number
  sqrt(1e-6);System.out.println("""res3: Double = """ + $show(res$3));$skip(36); val res$4 = 
  // very large number
  sqrt(1e60);System.out.println("""res4: Double = """ + $show(res$4));$skip(71); 

  def gcd(a: Int, b: Int): Int =
    if (b == 0) a else gcd(b, a % b);System.out.println("""gcd: (a: Int, b: Int)Int""");$skip(27); val res$5 = 
  // testing
  gcd(14, 21);System.out.println("""res5: Int = """ + $show(res$5));$skip(145); 

  def factorial(n: Int): Int = {
    def helper(n: Int, acc: Int): Int =
      if (n == 0) acc else helper(n - 1, n * acc)
    helper(n, 1)
  };System.out.println("""factorial: (n: Int)Int""");$skip(29); val res$6 = 
  // testing
  factorial(10);System.out.println("""res6: Int = """ + $show(res$6))}
}
