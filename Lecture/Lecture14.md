# Functional Programming
## Topics to be covered
- [Introduction](#introduction)
- [Mathematical Functions](#mathematical-functions)
- [Fundamentals of Functional Programming Languages](#fundamentals-of-functional-programming-languages)
- The First Functional Programming Language: LISP
- Introduction to Scheme
- ML
- Haskell
- Support for Functional Programming in Primarily Imperative Languages
- Comparison of Functional and Imperative Languages

## Introduction
- The design of the imperative languages is based directly on the *von Neumann architecture*
    - Efficiency is the primarily concern, rather than the suitability of the language for software development
- The design of the functional languages is based on *mathematical functions*
    - A solid theoretical basis that is also closer to the user, but relatively unconcerned with the architecture of the machines on which programs will run

### Programming without State
- **Imperative style**
    ```pascal
    n := x;
    a := 1;
    while n > 0 do
    begin a := a * n;
        n := n-1;
    end;
    ```
- Declarative (functional) style
    ```haskell
    fac n =
        if n == 0
        then 1
        else n * fac(n - 1)
    ```
- Programs in pure functional languages have no exlpicit state
- Programs are constructed entirely by composing expressions

### Pure Functional Programming Languages
- **Imperative Programming**
    - Program = Algorithms + Data
- **Functional Programming**
    - Program = Functions $\circ$ Functions
- What is a Program?
    - A program (computation) is a **transformation** from input data to output data

### Key features of **PURE** functional languages
1. All programs and procedures are **functions**
2. There are **no variables or assignments** - only input parameters
3. There are **no loops** - only recursive functions
4. The values returned by a function **depends only on the values of its parameters**
5. Functions are **first-class values**

## Mathematical Functions
- A mathematical function is a *mapping* of members of one set, called the *domain set*, to another set, called the *range set*
- A *lambda expression* specifies the parameter(s) and the mapping of a function in the following form
$$\lambda(x) x * x * x$$
for the function `cube(x) = x * x * x`
- A mathematical function maps its parameter(s) to a value (or values), rather than specifying a sequence of operations on values in memory to produce a value

### Functional Forms
- A higher-order function, or *functional form*, is one that either takes functions as parameters or yields a function as its result, or both
- **Do not implement function from scratch**
```py
def square(x):
    return x * x
def cube(x):
    return x * x * x
def Dotwice(function, x):
    return function(function(x))
print("data {0} has square {1} and double square {2}".format(5, square(5), Dotwice(square, 5)))
print("data {0} has cube {1} and double cube {2}".format(5, cube(5), Dotwice(cube, 5)))

def doTwiceMaker(f): # make a function
    def twoF(x):
        return f(f(x))
    return twoF
twoSquare = doTwiceMaker(square)
twoSquare(2) # 8
```

### Higher-order function Example
- Suppose we would like to evaluate summation
- Can we create a High order procedure in Python that allows us to compute any of them

```py
def summation(low, high, f, next):
    s = 0
    x = low
    while x <= high:
        s = s + f(x)
        x = next(x)
    return s

def sumint(low, high):
    return summation(low, high, lambda x: x, lambda x: x+1)
def sumsquares(low, high):
    return summation(low, high, lambda x: x **2, lambda x: x+1)
def piSum(low, high):
    return summation(low, high, lambda x: 1.0/x**2, lambda x: x+2)
```

### Function Composition
- A functional form that takes two functions as parameters and yields a function whose value is the first actual parameter function applied to the application of the second

- Form: $h = f\circ g$
    - which means `h(x) = f(g(x))`
- For $f(x) = x + 2$ and $g(x) = 3 * x$, $h = f \circ g$ yields $(3 * x) + 2$

### Apply-to-all
- A functional form that takes a single function as a parameter and yields a list of values obtained by applying the given function to each element of a list of parameters
- Form: $\alpha$
- For $h(x) = x * x$
- $\alpha(h, (2, 3, 4))$ yields (4, 9, 16)

### Apply-to-all: filter, reduce and map
- `m = map(func, seq)`
    ```py
    def add100(x):
        return x + 100
    m = map(add100, [44, 22, 66])

    l = list(m) # convert map object to list
    print(l) # [144, 122, 166]
    ```
- `filter(function, sequence)`
    ```py
    def even(x):
        if x % 2 == 0:
            return True
        return False
    f = filter(even, [1, 5, 44, 27, 22, 66])

    l = list(f) # convert fliter object to list
    print(l) # [44, 22, 66]
    ```
- `r = reduce(func, seq)`
    ```py
    import functools
    def sum(x, y):
        return x + y
    value = functools.reduce(sum, [1,2,3,4])
    print(value) # 10
    ```

## Fundamentals of Functional Programming Languages
- The objective of the design of a FPL is to mimic mathematical functions to the greatest extent possible
- The basic process of computation is fundamentally different in a FPL than in an imperative language
    - Imperative language: operations are done and the results are stored in variables for later use
    - Management of variables is a constant concern and source of complexity for imperative programming
- In an FPL, variables are not necessary, as is the case in mathematics
- *Referential Transparency*: in an FPL, the evaluation of a function always produces the same result given the same parameters

### Referentially Transparent
- the value of a function depends only on the value of its parameters
- No state
- Question: Which of these functions are referentially transparent?
    - C: `int c = getchar();`
        - No
    - Java: `int c = System.in.read();`
        - No
    - Java: `double y = Math.sqrt(7.5);`
        - Yes
    - Java: `double r = Math.random();`
        - No

### Notes and Examples
- Any referentially transparent function with no parameters must always return the same value!
- not referentially transparent:
    - `random()`
    - `getchar()`

### Replacing Loops with Recursion
- Mathematical functions use recursion for iterative def'n
    - `Factorial(n) := n * Factorial (n - 1)` for n > 0
- Functional programming uses recursion instead of loops
- C example:
    ```c
    long factorial (long n)
    {
        int k; long result = 1;
        for(k = 1; k <=n; k++) result = k * result;
        return result;
    }
    ```
- same function using recursion:
    ```c
    long factorial(long n)
    {
        if(n <= 1) return 1;
        else return n * factorial(n - 1);
    }
    ```

# Functional Programming with Scheme
## DrScheme and MzScheme
- We'll use the PLT Scheme (Racket) system developed by a group of academics (Brown, Northeastern, Chicago, Utah)
- Scheme started in the 1970s
- MzScheme is the Basic scheme engine and can be called from the command line and assumes a terminal style interface
- **DrRacket** is a graphical programmic environment for Scheme

### Primitive Function Evaluation
- Parameters are evaluated, in no particular order
- The values of the parameters are substituted into the function body
- The function body is evaluated
- The value fo the last expression in the body is the value of the function

### Primitive Functions & Lambda Expressions
- Primitive Arithmetic Functions: +, -, *, /, ABS, SQRT, REMAINDER, MIN, MAX
    - e.g., `(+ 5 2)` yields 7
- Lambda Expressions
    - Form is based on $\lambda$ notation
    - e.g., `(lambda (x) (* x x))`
    - x is called a bound variable
- Lambda expressions can be applied to parameters
    - e.g., `(lambda (x) (* x x)) 7`
- LAMBDA expressions can have any number of parameters
    - `(lambda (a b x) (+ (* a x x) (* b x)))`

### Special Form Function: DEFINE
- `DEFINE`- Two forms:
    1. To bind a symbol to an expression
        - e.g. `(DEFINE pi 3.141593)`
        - Example use: `(DEFINE two_pi (* 2 pi))`
        - These symbols are not vairables: they are like the names bound by Java's `final` declarations
    2. TO bind names to lambda expressions (`LAMBDA` is implicit)
        - e.g. `(DEFINE (square x) (* x x))`
        - `(square 5)`

- The evaluation process for `DEFINE` is different. The first parameter is never evaluated. The second parameter is evaluated and bound to the first parameter

### Output Functions
- Usually not needed, because the interpreter always displays the result of a function evaluated at the top level (not nested)
- Scheme has `PRINTF`, which is similar to the `printf` function of C
- Note: explicit input and output are not part of the pure functional programming model, because input operations change the state of the program and output operations are side effects

### Numeric Predicate Functions
- `#T` (or `#t`) is true and `#F` (or `#f`) is false (sometimes `()` is used for false)
- =, <>, >, <, >=, <=
- `EVEN?`, `ODD?`, `ZERO?`, `NEGATIVE?`
- The `NOT` function inverts the logic of a Boolean expression

### Control Flow
- Selection- the special form, `IF`
```scheme
(if predicate then_exp else_exp)
    (if (<> count 0)
        (/ sum count)
    )
```
- `COND` function:
```scheme
(define (leap? year)
    (cond
        ((zero? (modulo year 400)) #T)
        ((zero? (modulo year 100)) #F)
        (else (zero? (modulo year 4)))
    )
)
```

### List Functions
- `QUOTE`: takes one parameter; returns the parameter without evaluation   
    - `QUOTE` is required because the Scheme interpreter, named `EVAL`, always evaluates parameters to function applications before applying the function. `QUOTE` is used to avoid parameter evaluation when it is not appropriate
    - `QUOTE` can be abbreviated with the apostrophe prefix operator
        - `'(A B)` is equivalent to `(QUOTE (A B))`

- Examples:
```scheme
(car '((A B) C D)) ; returns (A B)
(car 'A) ;is an error
(cdr '((A B) C D)) ;returns (C D)
(cdr 'A) ;is an error
(cdr '(A)) ;returns ()
(cons '() '(A B)) ;returns (() A B)
(cons '(A B) '(C D)) ;returns ((A B) C D)
(cons 'A 'B) ;returns (A . B) (dotted pair)
```

- `LIST` is a function for building a list from any number of parameters
    - `(LIST 'apple 'orange 'grape)`
    - returns `(apple orange grape)`

### Predicate Function: `EQ?`
- `EQ?`: takes two expressions as parameters (usually two atoms); it returns `#T` if both parameters have the same pointer value; otherwise `#F`
- `(EQ? 'A 'A)` yields `#T`
- `(EQ? 'A 'B)` yields `#F`
- `(EQ? 'A '(A B))` yields `#F`
- `(EQ? '(A B) '(A B))` yields `#T` or `#F`
- `(EQ? 3.4 (+ 3 (0.4)))` yields `#T` or `#F`

### Predicate Function: `EQV?`
- `EQV?` is like `EQ?`, except that it works for both symbolic and numeric atoms; it is a value comparison, not a pointer comparison
- `(EQV? 3 3)` yields `#T`
- `(EQV? 'A 3)` yields `#F`
- `(EQV 3.4 (+ 3 0.4))` yields `#T`
- `(EQV? 3.0 3)` yields `#F` (floats and integers are different)

### Predicate Functions: `LIST?` and `NULL?`
- `LIST?` takes one parameter; it returns `#T` if the parameter is a list; otherwise `#F`
    - `(LIST? '())` yields `#T`
- `NULL?` takes one parameter; it returns `#T` if the parameter is the empty list; otherwise `#F`
    - `(NULL? '(()))` yields `#F`

## Example Scheme Function: 
### `member`
- `member` takes an atom and a simple list; returns `#T` if the atom is in the list; `#F` otherwise
    ```scheme
    (define (member atm a_list)
    (cond
        ((null? a_list) #F)
        ((eq? atm (car a_list)) #T)
        ((else (member atm (cdr a_list))))
    ))
    ```
### `equalsimp`
- `equalsimp` takes two simple lists as parameters; returns `#T` if the two simple lists are equal; `#F` otherwise
    ```scheme
    (define (equalsimp list1 list2)
        (cond
            ((null? list1) (null? list2))
            ((null? list2) #F)
            ((eq? (car list1) (car list2))
                (equalsimp (cdr list1) (cdr list2)))
            (else #F)
        )
    )
    ```

### `equal`
- `equal` takes two general lists as parameters; return `#T` if the two lists are equal; `#F` otherwise
    ```scheme
    (define (equal list1 list2)
        (cond
            ((not (list? list1)) (eq? list1 list2))
            ((not (list? list2)) #F)
            ((null? list1) (null? list2))
            ((null? list2) #F)
            ((equal (car list1) (car list2))
                (equal (cdr list1) (cdr list2))
            )
            (else #F)
        )
    )
    ```

### `append`
- `append` takes two lists as parameters; returns the first parameter list with the elements of the second parameter list appended at the end
    ```scheme
    (define (append list1 list2)
        (cond
            ((null? list1) list2)
            (else (cons (car list1)
                (append (cdr list1) list2)))
        )
    )
    ```

### `let`
- `let` is actually shortand for a `LAMBDA` expression applied to a parameter
    - `(LET ((alpha 7)) (* 5 alpha))`
    - is the same as:
    - `((LAMBDA (alpha) (* 5 alpha)) 7)`

#### Example
```scheme
(define (quadratic_roots a b c)
    (let (
        (root_part_over_2a (
            / (sqrt (- (* b b) (* 4 a c))) (* 2 a)))
        (minus_b_ver_2a(/ (- 0 b) (* 2 a)))
        (list (+ minus_b_over_2a root_part_over_2a))
            (- minus_b_over_2a root_part_over_2a))
))
```

## Tail Recursion in Scheme
- Definition: A function is tail recursive if its recursive call is the last operation in the function
- A tail recursive function can be automatically converted by a compiler to use iteration, making it faster
- Scheme language definition requires that Scheme language systems convert all tail recursive functions to use iteration
- Example of rewriting a function to make it tail recursive, using helper a function
```scheme
; original
(define (factorial n)
    (if (<= n 0)
        1
        (* n (factorial (- n 1)))
))

; tail recursive
(define (facthelper n factpartial)
    (if (<= n 0)
        factpartial
        facthelper((- n 1) (* n factpartial))
    ))

(define (factorial n)
    (facthelper n 1)
)
```

## Support for Functional Programming in Primarily Imperative Languages
- Support for functional programming is increasingly creeping into imperative languages
    - Anonymous functions (lambda expressions)
        - JS: leave the name out of a function definition
        - C#: `i -> (i % 2) == 0`; (returns true or false depending on whether the parameter is even or odd)
        - Python: `lambda a, b: 2 * a - b`

- Python supports the higher-order functions filter and map (often use lambda expressions as their first parameters)
    `map(lambda x: x ** 3, [2, 4, 6, 8])`
    - Returns [8, 64, 216, 512]
- Python supports partial function applications
    ```py
    from operator import add
    add5 = partial(add, 5)
    add5(15)
    ```
    - The first line imports add as a function
- Ruby Blocks
    - Are effectively subprograms that are sent to methods, which makes the method a higher-order subprogram
    - A block can be converted to a subprogram object with `lambda`
        - `times = lambda {|a, b| a * b}`
        - Use: `x = times.(3, 4)`; sets x to 12
    - Times can be curried with
        - `times5 = times.curry(5)`
        - Use: `x5 = times5.(3)`; sets x5 to 15

## Comparing Functional and Imperative Languages
- Imperative Languages:
    - Efficient execution
    - Complex semantics
    - Complex syntax
    - Concurrency is programmer designed
- Functional Languages:
    - Simple semantics
    - Simple syntax
    - Less efficient execution
    - Programs can automatically be made concurrent

## Summary
- Functional programming languages use function application, conditional expressions, recursion, and functional forms to control program execution
- LISP began as a purely functional language and later included imperative features
- Scheme is a relatively simple dialect of LISP that uses static scoping exclusively
- Common LISP is a large LISP-based language
- ML is a static-scoped and strongly typed functional language that uses type inference
- Haskell is a lazy functional language supporting infinite lists and set comprehension
- F# is a .NET functional language that also supports imperative and object-oriented programming
- Some primarily imperative languages now incorporate some support for functional programming
- Purely functional languages have advantages over imperative alternatives, but still are not very widely used

# Regarding the Functional Programming
- Check the both the slides and appendix to learn more about the different functional programming languages