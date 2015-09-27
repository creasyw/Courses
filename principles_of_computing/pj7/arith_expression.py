"""
Python class definition for creation and 
evaluation of arithmetic expressions
"""

# import Tree class definition
import poc_tree

# Use dictionary of lambdas to abstract function definitions

OPERATORS = {"+": (lambda x, y: x + y),
             "-": (lambda x, y: x - y),
             "*": (lambda x, y: x * y),
             "/": (lambda x, y: x / y),
             "//": (lambda x, y: x // y),
             "%": (lambda x, y: x % y)}


class ArithmeticExpression(poc_tree.Tree):
    """
    Basic operations on arithmetic expressions
    """

    def __init__(self, value, children, parent=None):
        """
        Create an arithmetic expression as a tree
        """
        poc_tree.Tree.__init__(self, value, children)

    def __str__(self):
        """
        Generate a string representation for an arithmetic expression
        """

        if len(self._children) == 0:
            return str(self._value)
        ans = "("
        ans += str(self._children[0])
        ans += str(self._value)
        ans += str(self._children[1])
        ans += ")"
        return ans

    def evaluate(self):
        """
        Evaluate the arithmetic expression
        """

        if len(self._children) == 0:
            if "." in self._value:
                return float(self._value)
            else:
                return int(self._value)
        else:
            function = OPERATORS[self._value]
            left_value = self._children[0].evaluate()
            right_value = self._children[1].evaluate()
            return function(left_value, right_value)


def run_example():
    """
    Create and evaluate some examples of arithmetic expressions
    """

    one = ArithmeticExpression("1", [])
    two = ArithmeticExpression("2", [])
    three = ArithmeticExpression("3", [])
    print one
    print one.evaluate()

    one_plus_two = ArithmeticExpression("+", [one, two])
    print one_plus_two
    print one_plus_two.evaluate()

    one_plus_two_times_three = ArithmeticExpression("*", [one_plus_two, three])
    print one_plus_two_times_three

    import poc_draw_tree
    poc_draw_tree.TreeDisplay(one_plus_two_times_three)
    print one_plus_two_times_three.evaluate()


run_example()
