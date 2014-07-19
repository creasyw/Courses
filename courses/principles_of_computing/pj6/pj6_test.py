import poc_simpletest
import user36_x8aXVLcG9A_3 as mycode

def test_remove_duplicates():
    suite = poc_simpletest.TestSuite()
    print("test_remove_duplicates():"),
    suite.run_test(mycode.remove_duplicates([]), [], "Test 0")
    suite.run_test(mycode.remove_duplicates([1]), [1], "Test 1")
    suite.run_test(mycode.remove_duplicates([1,1,1,1,2,3]), [1,2,3], "Test 2")
    suite.run_test(mycode.remove_duplicates([1,2,2,2,2,3,3]), [1,2,3], "Test 3")
    suite.report_results()

def test_intersect():
    suite = poc_simpletest.TestSuite()
    print("test_intersect():"),
    suite.run_test(mycode.intersect([],[]), [], "Test 0")
    suite.run_test(mycode.intersect([],[1,2,3]), [], "Test 1")
    suite.run_test(mycode.intersect([1,2,3],[]), [], "Test 2")
    suite.run_test(mycode.intersect([4,5,6],[1,2,3]), [], "Test 3")
    suite.run_test(mycode.intersect([1,1,1,1,1],[1,2,3]), [1], "Test 4")
    suite.run_test(mycode.intersect([1,1,2,2,4],[1,2,3]), [1,2], "Test 5")
    suite.run_test(mycode.intersect([1,1,1,1,1],[1,1,2,3]), [1,1], "Test 6")
    suite.report_results()

def test_merge():
    suite = poc_simpletest.TestSuite()
    print("test_merge():"),
    suite.run_test(mycode.merge([],[]), [], "Test 0")
    suite.run_test(mycode.merge([],[1,2,3]), [1,2,3], "Test 1")
    suite.run_test(mycode.merge([1,2,3], []), [1,2,3], "Test 2")
    suite.run_test(mycode.merge([1,2,3], [1,2,3]), [1,1,2,2,3,3], "Test 3")
    suite.run_test(mycode.merge([1,2,3], [0,4,5]), [0,1,2,3,4,5], "Test 4")
    suite.report_results()

def test_merge_sort():
    suite = poc_simpletest.TestSuite()
    print("test_merge_sorty():"),
    suite.run_test(mycode.merge_sort([]), [], "Test 0")
    suite.run_test(mycode.merge_sort([1]), [1], "Test 1")
    suite.run_test(mycode.merge_sort([1,2,3]), [1,2,3], "Test 2")
    suite.run_test(mycode.merge_sort([1,4,2,3]), [1,2,3,4], "Test 3")
    suite.run_test(mycode.merge_sort([38,27,43,3,9,82,10]), [3,9,10,27,38,43,82], "Test 4")
    suite.report_results()

test_remove_duplicates()
test_intersect()
test_merge()
test_merge_sort()
