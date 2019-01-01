package week3

trait week3_List[T] {
  def isEmpty: Boolean
  def head: T
  def tail: List[T]
}

class Cons[T](val head:T, val tail:List[T]) extends week3_List[T]{
  def isEmpty = false
}

class Nil[T] extends week3_List[T]{
  def isEmpty = true
  def head = throw new NoSuchElementException("Nil.head")
  def tail = throw new NoSuchElementException("Nil.tail")
}

