package main

import (
	"fmt"
	"html/template"
	"log"
	"os"
	"time"

	"./github"
)

const templ = `{{.TotalCount}} issues:
{{range .Items}}-------------------------------------
Number:    {{.Number}}
User:      {{.User.Login}}
Title:     {{.Title | printf "%.64s"}}
Age:       {{.CreatedAt | daysAgo}} days
{{end}}`

func daysAgo(t time.Time) int {
	return int(time.Since(t).Hours() / 24)
}

func main() {
	// Get the report from Github API
	result, err := github.SearchIssues(os.Args[1:])
	if err != nil {
		log.Fatal(err)
	}

	var report = template.Must(template.New("report").
		Funcs(template.FuncMap{"daysAgo": daysAgo}).Parse(templ))
	if err := report.Execute(os.Stdout, result); err != nil {
		log.Fatal(err)
	}

}

// The native method of printing results in the 1st iteration
func normalPrint(result *github.IssuesSearchResult) {
	fmt.Printf("%d issues:\n", result.TotalCount)
	for _, item := range result.Items {
		fmt.Printf("#%-5d %9.9s %.55s\n", item.Number, item.User.Login, item.Title)
	}
}
