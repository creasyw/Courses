import poc_simpletest
import user36_hBwuxoc1Pr_17 as mycode
##### please insert your code url in blahblahblah place ####
##### ex) import user35_SASUUfXXET_28 as mycode  ####

OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"

def Zombie_Appocalypse_test():
    """
    Test code for Zombie Appocalypse (BFS)
    """

    # Create a Testsuite object
    suite = poc_simpletest.TestSuite()

    # Test 1.0 : Basic Zombie class test
    zombie = mycode.Zombie(3,3)
    cells = [0, 0, 0]
    suite.run_test(zombie._cells[0], cells, "Test 1.0 : Zombie._cells")

    # Test 1.1 - 1.2 : Zombie class, clear method
    zombie = mycode.Zombie(3, 3, obstacle_list = [(1, 1), (2, 2)])
    zombie.clear()
    cells = [0, 0, 0]
    suite.run_test(zombie._cells[1], cells, "Test 1.1 : Zombie.clear")
    suite.run_test(zombie._cells[2], cells, "Test 1.2 : Zombie.clear")

    # Test 2.0 : Zombie class, add_zombie method
    zombie.add_zombie(0, 0)
    zombies = [(0, 0)]
    suite.run_test(zombie._zombie_list, zombies, "Test 2.0 : Zombie.add_zombie")

    # Test 3.0 : Zombie class, num_zombies method
    suite.run_test(zombie.num_zombies(), 1, "Test 3.0, Zombie.num_zombies")

    # Test 4.0 :Zombie class, zombies method
    zombie.add_zombie(0, 1)
    zomb = ""
    for zom in zombie.zombies():
        zomb += str(zom)
    suite.run_test(zomb, "(0, 0)(0, 1)", "Test 4.0, Zombie class, zombies method")

    # Test 5.0 : Zombie class, add_human method
    zombie.add_human(0,2)
    humans = [(0, 2)]
    suite.run_test(zombie._human_list, humans, "Test 5.0, Zombie class, add_human method")

    # Test 6.0 Zombie class, num_human method
    suite.run_test(zombie.num_humans(), 1, "Test 6.0, Zombie class, num_human method")

    # Test 7.0 Zombie class, humans method
    hums = ""
    for hum in zombie.humans():
        hums += str(hum)
    suite.run_test(hums, "(0, 2)", "Test 7.0, Zombie class, human method")

    # Test 8.0 - 8.1 Zombie class, compute_distance_field method
    a = mycode.Zombie(5, 5, obstacle_list = [(2,1), (2,3), (3,3)])
    a.add_zombie(2,2)
    row2 = [3, 2, 1, 2, 3]
    suite.run_test(a.compute_distance_field(ZOMBIE)[1], row2, "Test 8.0, Zombie class, compute_distance_field")

    # Test 8.1 Zombie class, compute_distance_field method
    a.add_zombie(0,0)
    row2 = [1, 2, 1, 2, 3]
    suite.run_test(a.compute_distance_field(ZOMBIE)[1], row2, "Test 8.1, Zombie class, compute_distance_field")

    # Test 9.0 Zombie class, move_humans
    a = mycode.Zombie(5, 5, obstacle_list = [(1,1), (2,2)])
    a.add_zombie(0,0)
    a.add_zombie(4,4)
    a.add_human(0,1)
    a.add_human(3,2)
    #a.move_humans(a.compute_distance_field(ZOMBIE))
    #suite.run_test(a._human_list, [(1, 2), (3, 1)], "Test 9.0 Zombie class, move_humans")

    # Test 10.0 Zombie class, move_zombie
    #a.move_zombies(a.compute_distance_field(HUMAN))
    #suite.run_test(a._zombie_list[0], (0, 1), "Test 10.0 Zombie class, move_zombie")

    suite.report_results()

Zombie_Appocalypse_test()
