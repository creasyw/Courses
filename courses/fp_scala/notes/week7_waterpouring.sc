package week7

object week7_waterpouring {
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet

  val problem = new Pouring(Vector(4, 7))         //> problem  : week7.Pouring = week7.Pouring@2adb1d4
	problem.moves                             //> res0: scala.collection.immutable.IndexedSeq[Product with Serializable with w
                                                  //| eek7.week7_waterpouring.problem.Move] = Vector(Empty(0), Empty(1), Fill(0), 
                                                  //| Fill(1), Pour(0,1), Pour(1,0))

}