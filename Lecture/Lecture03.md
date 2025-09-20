# Programming Languages Syntax 2
## Outline
- The General Problem of Describing Syntax Cont.
    - Formal Methods of Describing Syntax
- Operators: Precedence and Associativity
- Syntactic Sugar
- Extended BNF
- Parsing Complexity

## Operator notation
- so, how do we interpret expressions like
1. 2 + 3 + 4
2. 2 + 3 * 4
- example 1 might not seem to matter, but it can for different operator (2 ** 3 ** 4) or when the limits of representation are hit (e.g., round off in numbers, e.g., 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 10 **6)
- Concepts:
    - explaining rules in terms of operator precedence and associativity
    - Realizing the rules in grammars

## Operators: Precedence and Associativity
- deal with the evaluation order within expressions
- Precedence rules specify order in which operators of different precedence level are evaluated, e.g.:
    - "*" Has a higher precedence than "+", so "*" groups more tightly than "+"
- What is the results of 4 * 5 ** 6?
    - 4 * (5 ** 6)
- A language's precedence hierarchy should match our intuitions, but the result's not always perfect, as in this Pascal example:
    - if (A < B) and (C < D), then  A:= 0
- Pascal relational operators have lowest precedence!
    if A < (B and C) < D then A := 0

### Operator Precedence Table
- check slides

## Operators: associativity
- Associativity rules specify order in which operators of the `same precendence` level are evaluated
- Operators are typically either **left** associative or **right** associative
- Left associativity is typical for +, -, * and /
- So A + B + C
    - Means: (A + B) + C
    - Not: A + (B + C)

- For + and *, it doesn't matter in theory (though it can in practice) but for - and / it matters in theory too.
- A - B - C
$$(A - B) - C \neq A - (B - C)$$

- 2 ** 3 ** 4
    - 2 ** (3 ** 4) = 2 ** 81 = 241785163922925834941235
    - (2 ** 3) ** 4 = 8 ** 4 = 256

- Languages diverge on this case:
    - Fortran: ** associates from right-to-left, as in normally the case for mathematics
    - In Ada, ** doesn't associate, you must write the expression with ( ) to obtain the expected answer

### Associativity in C
- in C, most of the operators associate left to right
    - a + b + c => (a + b) + c
- The various assignment operators however associate right to left
    - =, +=, -=, *=, /=, %=, >>=, <<=, &=, ^=, |=
- a += b += c
    - a += (b += c)
    - not (a += b) += c

## Precedence and associativity in Grammar
- If we use the parse tree to indicate precedence levels of the operators, we cannot have ambiguity
- unambiguous expression grammar:
$$<expr> \rightarrow <expr> - <term> | <term>$$
$$<term> \rightarrow <term> / const | const$$

## An Expression Grammar
- Here's a grammar to define simple arithmetic expressions over variables and numbers

- Exp ::= num
- Exp ::= id
- Exp ::= UnOp Exp
- Exp := Exp BinOp Exp
- Exp ::= '('Exp')'
- UnOp ::= '+'
- UnOp ::= '-'
- BinOp ::= '+' | '-' | '*' | '/'

> single quotes indicate terminal symbols
> unquoted symbols indicate non-terminals

### Derivation
- a + b * 2
```
Exp => // Exp := Exp BinOp Exp
Exp BinOp Exp => //Exp ::= id
id BinOp Exp => //BinOp ::= '+'
id + Exp => //Exp := Exp BinOp Exp
id + Exp BinOp Exp => //Exp ::= num
id + Exp BinOp num => //Exp ::= id
id + id BinOp num => // BinOp ::= '*'
id + id * num
a + b * 2
```
## Precedence
- Precedence refers to the order in which operations are evaluated
- Usual convention: exponents > mult, div > add, sub
- Deal with operations in categories: exponents, mulops, addops
- A revised grammar that follows these conventions:
```
Exp ::= Exp AddOp Exp
Exp ::= Term
Term ::= Term MulOp Term
Term ::= Factor
Factor ::= '(' + Exp + ')'
Factor ::= num | id
AddOp ::= '+' | '-'
MulOp ::= '*' | */*
```

## Associativity
- refers to the order in which two of the same operation should be computed
    - 3 + 4 + 5 = (3 + 4) + 5, left associative (all BinOps)
    - 3 ^ 4 ^ 5 = 3 ^ (4 ^ 5), right associative
- conditionals right associate but have a wrinkle: an else cause associates with closest *unmatched if*
    - if a then if b then c else d
    = if a then (if b then c else d)

### Associativity to the grammar

```
Exp ::= Exp AddOp Term
Exp ::= Term
Term ::= Term MulOp Factor
Term ::= Factor
Factor ::= '(' + Exp + ')'
Factor ::= num | id
AddOp ::= '+' | '-'
MulOp ::= '*' | */*
```

### Example: Conditionals
- Most languages allow two conditional forms, with and without an else clause:
    - if x < 0, then x = -x
    - if x < 0, then -x else x = x + 1
- But we'll need to decide how to interpret:
    - if x < 0 then if y < 0, x = -1 else x = -2
- To which *if* does the *else* clause attach
- This is like the syntactic ambiguity in attachment of prepositional phrases in English
    - <u> the man</u> <u>near a cat</u> <u>with a hat</u>

- All languages use standard rule to determine which *if* expression an *else* clause attaches to
- The rule:
    - an *else* clause attaches to the nearest *if* to its left that does not yet have an *else* clause
- Example:
    - if x < 0, then <u>if y < 0, x = -1 else x = -2</u>

#### Goal
- create a correct grammar for conditionals
- It needs to be non-ambiguous and the precedence is *else* with nearest unmatched *if*
```
- Statement ::= Conditional | 'whatever'
- Conditonal ::= 'if' test 'then' Statement 'else' Statement
Conditional ::= 'if' test 'then' Statement
```
- The grammar is ambiguous. The first Conditional allows unmatched *ifs* to be Conditionals
    - Good: if test then (if test then whatever else whatever)
    - Bad: if test then (if test then whatever) else whatever
- Goal: write a grammar that forces an else clause to attach to the nearest if w/o an else clause

#### The final unambiguous grammar
- Statement ::= Matched | Unmatched
- Matched ::= 'if' test 'then' Matched 'else' Matched | 'whatever'
- Unmatched ::= 'if' test 'then' Statement | 'if' test 'then' Matched 'else' Unmatched

## Syntactic Sugar
- syntactic features designed to make code easier to read or write while alternatives exist
- Makes the language *sweeter* for humans to use: things can be expressed more clearly, concisely, or in an alternative style that some prefer
- Syntactic sugar can be removed from language without effecting what can be done
- All applications of the construct can be systematically replaced with equivalents that don't use it

### Python example
```py
Full_Lost = [(1,0), (2,1), (3,5), (4,7), (5,5)]
filter = [1,3]

#The ugly
new_list = []
for id, count in Full_List:
    if id, count not in filter:
        new_list.append((id,count))
print(new_list)
new_list = []

#The Pythonic way
new_list = [(id,c) for id, c in Full_List | if id not in filter]
print (new_list)
```

## Extended BNF
- *Syntactic Sugar*: doesn't extend the expressive power of the formalism, but does make it easier to use, i.e., more readable and more writable
- Optional parts are placed in brackets([])
- <proc_call> -> ident [(<expr_list>)]
- Put alternative parts of RHSs in parentheses and separate them with vertical bars
- <term> -> <term> (+ | -) const
- Put repetitions (0 or more) in braces ({})
- <ident> -> letter {letter | digit}

### BNF vs EBNF
- BNF
```
<expr> -> <expr> + <term> | <expr> - <term> | <term>
<term> -> <term> * <factor> | <term> / <factor> | <factor>
```
- EBNF
```
<expr> -> <term> {(+ | -) <term>}
<term> -> <factor> {(* | /) <factor>}
```

## Parsing
- grammar describes the strings of tokens that are syntactically legal in a PL
- *recognizer* simply accepts or rejects strings
- *generator* procudes sentences in the language described by the grammar
- *parser* constructs a derivation or parse tree for a sentence (if possible)
- Two common types of parsers:
    - bottom-up or data driven
    - top-down or hypothesis driven
- A *recursive descent parser* is a way to implement a top-down parser that is particularly simple

### Bottom-up Parse
```
E -> int
E -> E + (E)
```
```
int + (int) + (int)
E + (int) + (int)
E + (E) + (int)
E + (int)
E + (E)
E
```

```
int + (int) + (int)
|   | | | | | | | |
E   + ( E ) | | | |
  \   /     | | | |
    E       + ( E )
      \       /
          E
```

### Parsing complexity
- How hard is the parsing task?
- Parsing an arbitrary <u>context free grammar</u> is $O(n^3)$, e.g, it can take time proportional the cube of the number of symbols in the input. This is bad!
- If we constrain the grammar somewhat, we can always parse in linear time. This is good!

- Linear-time parsing
    - LL parses
        - Recognize LL grammar
        - Use a top-down strategy
    - LR parsers
        - Recognize LR grammar
        - Use a bottom-up strategy

> LL(n): Left to right, Leftmost derivation, look ahead at most n symbols
> LR(n): Left to right, Right derivation, look ahead at most n symbols

- If it takes $t_l$ seconds to parse your C program with *n* lines of code, how long will it take if you make it twice as long?
$$time(n) = t_l, time(2n) = 2^3 * time(n)$$
    - 8 times longer
- Suppose v3 of your code has 10n lines
- Windows Vista was said to have ~50M lines of code

- Practical parsers have time complexity that is linear in the number of tokens, i.e., O(n)
- If your program is twice as long, it will take twice as long to parse

## Summary
- Syntax of a programming language is usually defined using BNF or a context free grammar
- In addition to defining what programs are syntactically legal, a grammar also encodes meaningful or useful abstractions (e.g., block of statements)
- Typical  syntactic notions like operator precedence, associativity, sequences, optional statements, etc. can be encoded in grammars
- Parser is based on a grammar and takes an input string, does a derivation and produces a parse tree