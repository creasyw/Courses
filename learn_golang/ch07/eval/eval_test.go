package eval

import (
	"fmt"
	"math"
	"testing"

	"./eval"
)

// this is much better than writing a main package and test =))
// The name of the test file has to be something_test.go
// Running in the same directory can be done via =go test -v .=
func TestEval(t *testing.T) {
	tests := []struct {
		expr string
		env  Env
		want string
	}{
		{"sqrt(A / pi)", Env{"A": 87616, "pi": math.Pi}, "167"},
		{"pow(x, 3) + pow(y, 3)", Env{"x": 12, "y": 1}, "1729"},
		{"pow(x, 3) + pow(y, 3)", Env{"x": 9, "y": 10}, "1729"},
		{"5 / 9 * (F - 32)", Env{"F": -40}, "-40"},
		{"5 / 9 * (F - 32)", Env{"F": 32}, "0"},
		{"5 / 9 * (F - 32)", Env{"F": 212}, "100"},
		//!-Eval
		// additional tests that don't appear in the book
		{"-1 + -x", Env{"x": 1}, "-2"},
		{"-1 - x", Env{"x": 1}, "-2"},
		//!+Eval
	}

	var prevExpr string
	for _, test := range tests {
		if test.expr != prevExpr {
			// This message goes into the =-v= part
			fmt.Printf("\n%s\n", test.expr)
			prevExpr = test.expr
		}
		expr, err := Parse(test.expr)
		if err != nil {
			t.Error(err)
			continue
		}
		// Get the result via formatting the string from expression
		got := fmt.Sprintf("%.6g", expr.Eval(test.env))
		// This message goes into the =-v= part
		// OR print everything if the test fails -- this is neat
		fmt.Printf("\t%v ==> %s\n", test.env, got)
		if got != test.want {
			t.Errorf("%s.Eval() in %v = %q, want %q",
				test.expr, test.env, got, test.want)
		}
	}
}
