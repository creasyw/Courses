(require 'package)
(add-to-list 'package-archives
             '("marmalade" . "http://marmalade-repo.org/packages/") t)
(add-to-list 'package-archives
             '("melpa" . "http://melpa.milkbox.net/packages/") t)
;; ruby-mode
(add-to-list 'auto-mode-alist
               '("\\.\\(?:gemspec\\|irbrc\\|gemrc\\|rake\\|rb\\|ru\\|thor\\)\\'" . ruby-mode))
(add-to-list 'auto-mode-alist
               '("\\(Capfile\\|Gemfile\\(?:\\.[a-zA-Z0-9._-]+\\)?\\|[rR]akefile\\)\\'" . ruby-mode))
(package-initialize)

;; this is for standard ml
;;(setenv "PATH" (concat "/usr/local/smlnj-110.75/bin:" (getenv "PATH")))
;;(setq exec-path (cons "/usr/local/smlnj-110.75/bin" exec-path))

;; use alt as meta key
(set-keyboard-coding-system nil)

(add-hook 'haskell-mode-hook 'turn-on-haskell-doc-mode)

;; hslint on the command line only likes this indentation mode;
;; alternatives commented out below.
(add-hook 'haskell-mode-hook 'turn-on-haskell-indentation)
;;(add-hook 'haskell-mode-hook 'turn-on-haskell-indent)
;;(add-hook 'haskell-mode-hook 'turn-on-haskell-simple-indent)

;; Ignore compiled Haskell files in filename completions
(add-to-list 'completion-ignored-extensions ".hi")

;; show line number
(global-linum-mode t)

;; for pop-up list auto-completion
;; can be exchangeably used with built-in completion M-/
(add-hook 'after-init-hook 'global-company-mode)


;; add for racket-mode
(add-hook 'racket-mode-hook
          '(lambda ()
             (define-key racket-mode-map (kbd "C-c r") 'racket-run)))

;; use RET for auto-indentation for racket-mode and geiser-mode
(add-hook 'racket-mode-hook '(lambda ()
                               (local-set-key (kbd "RET") 'newline-and-indent)))
(add-hook 'geiser-mode-hook '(lambda ()
                               (local-set-key (kbd "RET") 'newline-and-indent)))
;;
;; default running racket rather than guile REPL when M-x run-geiser
(setq geiser-active-implementations '(racket))
;; automatically call the repl for .rkt file
(setq geiser-mode-start-repl-p t)
