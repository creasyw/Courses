package funsets

import org.scalatest.FunSuite

import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner

/**
 * This class is a test suite for the methods in object FunSets. To run
 * the test suite, you can either:
 *  - run the "test" command in the SBT console
 *  - right-click the file in eclipse and chose "Run As" - "JUnit Test"
 */
@RunWith(classOf[JUnitRunner])
class FunSetSuite extends FunSuite {

  /**
   * Link to the scaladoc - very clear and detailed tutorial of FunSuite
   *
   * http://doc.scalatest.org/1.9.1/index.html#org.scalatest.FunSuite
   *
   * Operators
   *  - test
   *  - ignore
   *  - pending
   */

  /**
   * Tests are written using the "test" operator and the "assert" method.
   */
  test("string take") {
    val message = "hello, world"
    assert(message.take(5) == "hello")
  }

  /**
   * For ScalaTest tests, there exists a special equality operator "===" that
   * can be used inside "assert". If the assertion fails, the two values will
   * be printed in the error message. Otherwise, when using "==", the test
   * error message will only say "assertion failed", without showing the values.
   *
   * Try it out! Change the values so that the assertion fails, and look at the
   * error message.
   */
  test("adding ints") {
    assert(1 + 2 === 3)
  }

  import FunSets._

  test("contains is implemented") {
    assert(contains(x => true, 100))
  }

  /**
   * When writing tests, one would often like to re-use certain values for multiple
   * tests. For instance, we would like to create an Int-set and have multiple test
   * about it.
   *
   * Instead of copy-pasting the code for creating the set into every test, we can
   * store it in the test class using a val:
   *
   *   val s1 = singletonSet(1)
   *
   * However, what happens if the method "singletonSet" has a bug and crashes? Then
   * the test methods are not even executed, because creating an instance of the
   * test class fails!
   *
   * Therefore, we put the shared values into a separate trait (traits are like
   * abstract classes), and create an instance inside each test method.
   *
   */

  trait TestSets {
    val s1 = singletonSet(1)
    val s2 = singletonSet(2)
    val s3 = singletonSet(3)

  }

  /**
   * This test is currently disabled (by using "ignore") because the method
   * "singletonSet" is not yet implemented and the test would fail.
   *
   * Once you finish your implementation of "singletonSet", exchange the
   * function "ignore" by "test".
   */
  test("singletonSet(1) contains 1") {

    /**
     * We create a new instance of the "TestSets" trait, this gives us access
     * to the values "s1" to "s3".
     */
    new TestSets {
      /**
       * The string argument of "assert" is a message that is printed in case
       * the test fails. This helps identifying which assertion failed.
       */
      assert(contains(s1, 1), "Singleton")
      assert(contains(s2, 2), "Singleton")
      assert(!contains(s1, 2), "Singleton")
    }
  }

  test("union contains all elements") {
    new TestSets {
      val s = union(s1, s2)
      assert(contains(s, 1), "Union 1")
      assert(contains(s, 2), "Union 2")
      assert(!contains(s, 3), "Union 3")
    }
  }

  test("intersect test") {
    new TestSets {
      val x1 = union(s1, s2)
      val x2 = union(s2, s3)
      val x3 = intersect(x1, x2)
      assert(contains(x3, 2), "Intersect contains 2")
      assert(!contains(x3, 1), "Intersect does not contain 1")
      assert(!contains(x3, 3), "Intersect does not contain 3")
    }
  }

  test("diff test") {
    new TestSets {
      val x1 = union(s1, s2)
      val x2 = union(s2, s3)
      val x3 = diff(x1, x2)
      assert(contains(x3, 1), "diff contains 1")
      assert(!contains(x3, 2), "diff does not contain 2")
      assert(!contains(x3, 3), "diff does not contain 3")
    }
  }

  test("filter test") {
    new TestSets {
      val x1 = union(union(s1, s2), s3)
      val x2 = filter(x1, (x: Int) => x >= 2)
      assert(!contains(x2, 1), "filter does not contain 1")
      assert(contains(x2, 2), "filter contains 2")
      assert(contains(x2, 3), "filter contains 3")
    }
  }

  test("farall test") {
    def s: Set = (x: Int) => x < 0
    assert(forall(s, (x: Int) => x + 3 < 4), "this should be fine...")
    assert(!forall(s, (x: Int) => x * 2 > 0), "this should not be fine....")
  }

  test("exists test") {
    def s: Set = (x: Int) => x < 0
    def p1: Set = (x: Int) => x + 5 > 0
    def p2: Set = (x: Int) => x - 5 > 0
    assert(exists(s, p1), "this should be fine...")
    assert(!exists(s, p2), "this should not be fine....")
  }

  test("map test") {
    def ss: Set = (x: Int) => x < 10
    def p: Set = map(ss, (x: Int) => x * 2)
    assert(contains(p, -6), "this should be fine 1...")
    assert(contains(p, 16), "this should be fine 2...")
    assert(!contains(p, 30), "this should not be fine....")

    new TestSets {
      val s = union(union(s1, s2), s3)
      printSet(s) // {1, 2, 3}      
      val t = map(s, (x: Int) => x * x)
      printSet(t) // {1, 4, 9}      
      assert(contains(t, 9))
    }
  }
}
