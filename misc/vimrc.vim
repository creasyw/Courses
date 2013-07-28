

" syntax highlighting
syntax on
" automatic indentation
"set autoindent
" specifically c/c++ indentation
"set cindent
" to show the line number for each line
set nu

set showmatch
filetype plugin on
filetype indent on

" For racket
au BufRead,BufNewFile *.rkt set filetype=racket

" vim -b : edit binary using xxd-format!
augroup Binary
  au!
  au BufReadPre  *.bin let &bin=1
  au BufReadPost *.bin if &bin | %!xxd
  au BufReadPost *.bin set ft=xxd | endif
  au BufWritePre *.bin if &bin | %!xxd -r
  au BufWritePre *.bin endif
  au BufWritePost *.bin if &bin | %!xxd
  au BufWritePost *.bin set nomod | endif
augroup END


" add java
set sm
set ai
let java_highlight_all=1
let java_highlight_functions="style"
let java_allow_cpp_keywords=1


" add for python
"set smartindent
"set tabstop=4
"set shiftwidth=4
"set expandtab

"For screen.vim send block
"to SendScreen function
"(eg Scheme interpreter)
vmap <C-c><C-c> :ScreenSend<CR>
nmap <C-c><C-c> vip<C-c><C-c>



" For LATEX:
" REQUIRED. This makes vim invoke Latex-Suite when you open a tex file.
filetype plugin on
"
" " IMPORTANT: win32 users will need to have 'shellslash' set so that latex
" " can be called correctly.
set shellslash
"
" " IMPORTANT: grep will sometimes skip displaying the file name if you
" " search in a singe file. This will confuse Latex-Suite. Set your grep
" " program to always generate a file-name.
set grepprg=grep\ -nH\ $*
"
" " OPTIONAL: This enables automatic indentation as you type.
filetype indent on
"
" " OPTIONAL: Starting with Vim 7, the filetype of empty .tex files defaults to
" " 'plaintex' instead of 'tex', which results in vim-latex not being loaded.
" " The following changes the default filetype back to 'tex':
let g:tex_flavor='latex'
" this is mostly a matter of taste. but LaTeX looks good with just a bit
" " of indentation.
set sw=2
" " TIP: if you write your \label's as \label{fig:something}, then if you
" " type in \ref{fig: and press <C-n> you will automatically cycle through
" " all the figure labels. Very useful!
" CANNOT USE -- it will generate annoying highligh in Python...
" set iskeyword+=:
