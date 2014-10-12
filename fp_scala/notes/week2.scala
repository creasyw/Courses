object week2 {
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet

  def sum(f: Int => Int)(a: Int, b: Int): Int =
    if (a > b) 0 else f(a) + sum(f)(a + 1, b)     //> sum: (f: Int => Int)(a: Int, b: Int)Int

  def cube(x: Int): Int = x * x * x               //> cube: (x: Int)Int
  def fact(x: Int): Int =
    if (x == 0) 1 else x * fact(x - 1)            //> fact: (x: Int)Int

  def mapreduce(f: Int => Int, combine: (Int, Int) => Int, zero: Int)(a: Int, b: Int): Int =
    if (a > b) zero else combine(f(a), mapreduce(f, combine, zero)(a+1, b))
                                                  //> mapreduce: (f: Int => Int, combine: (Int, Int) => Int, zero: Int)(a: Int, b:
                                                  //|  Int)Int
  def product_old(f: Int => Int)(a: Int, b: Int): Int =
    if (a > b) 1 else f(a) * product_old(f)(a + 1, b)
                                                  //> product_old: (f: Int => Int)(a: Int, b: Int)Int
  def product(f:Int=>Int)(a:Int, b:Int): Int=
  mapreduce(f, (x,y)=>x*y, 1)(a, b)               //> product: (f: Int => Int)(a: Int, b: Int)Int
  
  def factorial(n: Int) = product(x => x)(1, n)   //> factorial: (n: Int)Int

  // testing
  product(x => x * x)(3, 4)                       //> res0: Int = 144
  factorial(5)                                    //> res1: Int = 120

}