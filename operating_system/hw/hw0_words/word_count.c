/*

Copyright © 2019 University of California, Berkeley

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

word_count provides lists of words and associated count

Functional methods take the head of a list as first arg.
Mutators take a reference to a list as first arg.
*/

#include "word_count.h"

/* Basic utililties */

char *new_string(char *str) {
	return strcpy((char *)malloc(strlen(str)+1), str);
}

void init_words(WordCount **wclist) {
	/* Initialize word count.  */
	*wclist = NULL;
}

size_t len_words(WordCount *wchead) {
	/* Length of a word count list */
	size_t len = 0;
	WordCount *wc = wchead;
	while (wc) {
		len++;
		wc = wc->next;
	}
	return len;
}

// return either the node with the matched word or the last word if the search
// fails
WordCount *find_word(WordCount *wchead, char *word) {
	/* Return count for word, if it exists */
	WordCount *wc = wchead;

	if (!wchead) {
		printf("Empty wchead\n");
		return wc;
	}

	while (wc->next) {
		if (strcmp(wc->word, word) == 0)
			return wc;
		wc = wc->next;
	}
	return wc;
}

void add_word(WordCount **wclist, char *word) {
	/* If word is present in word_counts list, increment the count, otw
	insert with count 1. */
	WordCount *wc = find_word(*wclist, word);
	WordCount *new_word;
	// wc is the start of the wclist in this case
	if (!wc) {
		// wc points to a new place as the newly allocated WordCount
		wc = (WordCount *) malloc(sizeof(WordCount));
		wc->word = word;
		wc->count = 1;
		// put it back to the wclist
		*wclist = wc;
	} else if (strcmp(word, wc->word)) {
		printf("Find a new words\n");
		new_word = (WordCount *) malloc(sizeof(WordCount));
		new_word->word = word;
		new_word->count = 1;
		wc->next = new_word;
	} else {
		wc->count++;
	}
}

void fprint_words(WordCount *wchead, FILE *ofile) {
	/* print word counts to a file */
	WordCount *wc;
	for (wc = wchead; wc; wc = wc->next) {
		fprintf(ofile, "%i\t%s\n", wc->count, wc->word);
	}
}

void print_words(WordCount *wchead) {
	/* print word counts to a file */
	WordCount *wc;
	for (wc = wchead; wc; wc = wc->next) {
		printf("%i\t%s\n", wc->count, wc->word);
	}
}
