" Rajiv's MIT/GNU Scheme syntax highlighting rules
"
" Author: Rajiv Eranki <eranki@mit.edu>
" Date Created: 27-Feb-06

syn case ignore

syn region paren1 matchgroup=paren1 start="(" end=")" contains=paren2
syn region paren2 matchgroup=paren2 start="(" end=")" contains=paren3 contained
syn region paren3 matchgroup=paren3 start="(" end=")" contains=paren4 contained
syn region paren4 matchgroup=paren4 start="(" end=")" contains=paren5 contained
syn region paren5 matchgroup=paren5 start="(" end=")" contains=parenlast contained
syn region parenlast matchgroup=parenlast start="(" end=")" contains=paren1 contained

hi paren1 guifg=Firebrick3 ctermfg=red
hi paren2 guifg=Orange3 ctermfg=yellow
hi paren3 guifg=Yellow4 ctermfg=green
hi paren4 guifg=OliveDrab4 ctermfg=cyan
hi paren5 guifg=CadetBlue3 ctermfg=blue
hi parenlast guifg=Thistle4 ctermfg=magenta

syn region Comment start="#|" end="|#"
syn match Comment ";.*$"

syn sync fromstart

let b:current_syntax = "scheme"
