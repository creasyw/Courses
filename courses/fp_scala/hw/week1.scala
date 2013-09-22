package recfun
import common._

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int =
    if (c <= 0 || c >= r) 1 else pascal(c - 1, r - 1) + pascal(c, r - 1)

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = {
    def helper(left: Int, right: Int, rest: List[Char]): Boolean =
      if (left < right) false
      else if (rest.length == 0) (left == right)
      else if (rest.head == '(') helper(left + 1, right, rest.tail)
      else if (rest.head == ')') helper(left, right + 1, rest.tail)
      else helper(left, right, rest.tail)

    helper(0, 0, chars)
  }

  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = {
    def helper(left: Int, rest: List[Int]): Int =
      if (rest.isEmpty) 0
      else if (rest.head == left) 1
      else if (rest.head > left) helper(left, rest.tail)
      else helper(left - rest.head, rest) + helper(left, rest.tail)
    helper(money, coins.sorted)
  }
}
