import poc_simpletest
import dummy_file_directory as mycode

def test_remove_duplicates():
    suite = poc_simpletest.TestSuite()
    suite.run_test(mycode.remove_duplicates([]), [], "Test 0")
    suite.run_test(mycode.remove_duplicates([1]), [1], "Test 1")
    suite.run_test(mycode.remove_duplicates([1,1,1,1,2,3]), [1,2,3], "Test 2")
    suite.run_test(mycode.remove_duplicates([1,2,2,2,2,3,3]), [1,2,3], "Test 3")

    suite.report_results()

test_remove_duplicates()
