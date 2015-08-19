;; General Usage Cases

; Disable welcom page
(setq inhibit-startup-message t)

; Centralize backup files
(setq backup-directory-alist '(("." . "~/.emacsaves")))

; Hide Tool bar for larger editing area
(tool-bar-mode -1)

; Make TAB in C mode insert a tab if point is in the middle of a line.
(setq c-tab-always-indent nil)

; Make searches case SENSITIVE by default (unless override in buffer)
(setq-default case-fold-search nil)

; Replace list-buffers with ibuffer
(global-set-key (kbd "C-x C-b") 'ibuffer)
