#lang racket
(provide (all-defined-out)) ;; so we can put tests in a second file

;; definition of structures for MUPL programs - Do NOT change
(struct var  (string) #:transparent)  ;; a variable, e.g., (var "foo")
(struct int  (num)    #:transparent)  ;; a constant number, e.g., (int 17)
(struct add  (e1 e2)  #:transparent)  ;; add two expressions
(struct ifgreater (e1 e2 e3 e4)    #:transparent) ;; if e1 > e2 then e3 else e4
(struct fun  (nameopt formal body) #:transparent) ;; a recursive(?) 1-argument function
(struct call (funexp actual)       #:transparent) ;; function call
(struct mlet (var e body) #:transparent) ;; a local binding (let var = e in body) 
(struct apair (e1 e2)     #:transparent) ;; make a new pair
(struct fst  (e)    #:transparent) ;; get first part of a pair
(struct snd  (e)    #:transparent) ;; get second part of a pair
(struct aunit ()    #:transparent) ;; unit value -- good for ending a list
(struct isaunit (e) #:transparent) ;; evaluate to 1 if e is unit else 0

;; a closure is not in "source" programs; it is what functions evaluate to
(struct closure (env fun) #:transparent) 

;; Problem 1

(define (racketlist->mupllist  list)
          (if (null? list) 
               (aunit)
               (apair  (car list) (racketlist->mupllist (cdr list)))))

(define (mupllist->racketlist  mupllist)
          (if (aunit? mupllist) 
                null
               (cons  (apair-e1 mupllist) (mupllist->racketlist (apair-e2 mupllist)))))

;; Problem 2

;; lookup a variable in an environment
;; Do NOT change this function
(define (envlookup env str)
  (cond [(null? env) (error "unbound variable during evaluation" str)]
        [(equal? (car (car env)) str) (cdr (car env))]
        [#t (envlookup (cdr env) str)]))

;; Do NOT change the two cases given to you.  
;; DO add more cases for other kinds of MUPL expressions.
;; We will test eval-under-env by calling it directly even though
;; "in real life" it would be a helper function of eval-exp.
(define (eval-under-env e env)
  (cond 
        [(var? e) 
             (envlookup env (var-string e))]
        
        [(add? e) 
         (let ([v1 (eval-under-env (add-e1 e) env)]
               [v2 (eval-under-env (add-e2 e) env)])
           (if (and (int? v1)
                    (int? v2))
               (int (+ (int-num v1) 
                       (int-num v2)))
               (error "MUPL addition applied to non-number")))]
    
        [(isaunit? e) 
          (if(aunit? (eval-under-env (isaunit-e e) env)) (int 1) (int 0))]
                
        [(int? e) e]
        
        [(aunit? e) e]
        
        [(closure? e) e]
        
         [(ifgreater? e)
           (let ([v1 (eval-under-env (ifgreater-e1 e) env)]
                 [v2 (eval-under-env (ifgreater-e2 e) env)])
             (if (and (int? v1) 
                      (int? v2))
                    (if (> (int-num v1) (int-num v2)) 
                        (eval-under-env (ifgreater-e3 e) env)  
                        (eval-under-env (ifgreater-e4 e) env))   
                    (error "MUPL ifgreater applied to non-numbers")))]
        
        [(apair? e) 
          (let ([v1 (eval-under-env (apair-e1 e) env)]
                [v2 (eval-under-env (apair-e2 e) env)])
           (apair v1 v2))]
        
        [(fst?  e)
         (let([temp (eval-under-env (fst-e e) env)])
         (if (apair? temp) 
              (apair-e1 temp)
              (error "MUPL fst applied to non-apair")))]
        
        [(snd?  e)
         (let([temp (eval-under-env (snd-e e) env)]) 
         (if (apair? temp) 
              (apair-e2 temp)
              (error "MUPL fst applied to non-apair")))]
        
        [(mlet? e)  
           (let* ([exp (eval-under-env (mlet-e e) env)] 
                  [env (append (list (cons (mlet-var e) exp)) env)])
                 (eval-under-env (mlet-body e) env))]
        
        [(fun? e) (closure env  e)]
              
        [(call? e)
         (let*([cls (eval-under-env (call-funexp e) env)])
             (if (closure? cls)
               (let*([fname  (fun-nameopt (closure-fun cls))]
                     [cls_env (closure-env cls)]
                     [cls_env (if fname (append cls_env (list (cons fname cls))) cls_env)]
                     [act_param (eval-under-env (call-actual e) env)]
                     [form_param (fun-formal (closure-fun cls))]
                     [cls_env (append (list (cons form_param act_param)) cls_env)]
                     [f (closure-fun cls)]
                     [body (fun-body f)])
             (eval-under-env body cls_env))
             (error "not a MUPL closure")))]))

;; Do NOT change
(define (eval-exp e)
  (eval-under-env e null))
        
;; Problem 3

(define (ifaunit e1 e2 e3) (ifgreater (isaunit e1) (int 0) e2 e3))
                            
(define (mlet* lstlst e2) 
         (if (null? lstlst) 
          e2 
         (mlet (car (car lstlst)) (cdr (car lstlst)) (mlet* (cdr lstlst) e2))))

(define (ifeq e1 e2 e3 e4) 
  (mlet "_x" e1 (mlet "_y" e2  
                (ifgreater (add (ifgreater  (var "_x") (var "_y") (int 1) (int 0)) 
                                (ifgreater  (var "_y") (var "_x") (int 1) (int 0)))
                                (int 0)
                                 e4 
                                 e3))))

;; Problem 4

(define mupl-map 
      (fun "fname" "fpar" 
           (fun "m" "lst" (ifaunit(var "lst")
                                  (aunit)
                                  (apair (call (var "fpar") (fst (var "lst")))
                                         (call (var "m") (snd (var "lst"))))))))

(define mupl-mapAddN 
  (mlet "map" mupl-map
         (fun #f "x" (call (var "map") (fun #f "z" (add (var "x") (var "z"))))))) 



;; Challenge Problem

(struct fun-challenge (nameopt formal body freevars) #:transparent) ;; a recursive(?) 1-argument function

;; We will test this function directly, so it must do
;; as described in the assignment
(define (compute-free-vars e) "CHANGE")

;; Do NOT share code with eval-under-env because that will make
;; auto-grading and peer assessment more difficult, so
;; copy most of your interpreter here and make minor changes
(define (eval-under-env-c e env) "CHANGE")

;; Do NOT change this
(define (eval-exp-c e)
  (eval-under-env-c (compute-free-vars e) null))
