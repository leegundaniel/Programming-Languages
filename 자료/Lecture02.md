# Programming Languages Syntax I
## Outline
- Introduction (Chapter 3 of textbook)
- The General Problem of Describing Syntax
- Formal Methods of Describing Syntax

## Introduction
- "Language is a system of gestures, grammar, signs, sounds, symbols, or words, which is used to represent and communicate concepts, ideas, meanings, and thoughts"
- Human language is a way to communicate representation from one (human) mind to another
- Programming language
    - A way to communicate representations (e.g., of data or a procedure) between ``human minds`` and/or ``machines``
- break down the problem of *defining* a programming language into two parts
    - defining the PL's ``syntax``
    - defining the PL's ``semantics``

- Syntax - the form or structure of the expressions, statements, and program units
- Semantics - the meaning of the expressions, statements, and program units

- There is not always a clear boundary between the two 

## Why and How
### Why
- We want specifications for several communities:
    - Other language designers
    - Implementers
    - Machines
    - Programmers (the users of the language)

### How
- One way is via natural language descriptions (e.g., user's manuals, text books)
- there are a number of more formal techniques for specifying the syntax and semantics

## Source to program
1. Character stream -> Scanner(lexical analysis) -> Token stream
2. Token stream -> Parser (syntax analysis) -> Parse tree
3. Parse tree -> Semantic analysis and intermediate code generation -> Abstract syntax tree or other intermediate form
4. Abstract syntax tree or other intermediate form -> Machine-independent code improvement (optional) -> Modified intermediate form
5. Modified intermediate form -> Target code generation -> Assembly or machine language, or other target language
6. Assembly or machine language, or other target language -> Machine-specific code improvement (optional) -> Modified target language

- 1 ~ 2: Scanner & Parser = Syntax Part (Compiler)

## Syntax Overview
- Language preliminaries
- Context-free grammars and BNF
- Syntax Diagrams

### Preliminaries
- ``Sentence``: string of characters over some alphabet (e.g., def add l(n): return n + l)
- ``Language`` is a set of sentences
- ``Lexeme``: lowest level syntactic unit of a language (e.g., *, addI, begin)
- ``Token``: category of lexemes (e.g., identifier)
- Formal approaches to describing syntax
    - `Recognizers`(within Parser) - device reads input strings over the alphabet of the language and decides whether the input strings belong to the language
        - Uses generators to check syntax
    - `Generators` - A device that generates sentences of a language. One can determine if the syntax of a particular sentence is ``syntactically correct`` by comparing it to the ``structure of the generator``

## Lexical Structure of Programming Languages
- The structure of its lexemes (words or tokens)
- The scanning phase (lexical analyser) collects characters into tokens
- Parsing phase (syntactic analyser / parser) determines syntactic structure

## Formal Grammar
- Set of rules for strings in a formal language
- Rules describe how to form string from the language's alphabet that are valid according to the language's syntax
- A grammar does not describe the meaning of the strings or what can be done with them in whatever context - only their form

## Grammars
- Context-Free Grammars
    - Developed by Noam Chomsky in the mid-1950s
    - Language generators, meant to describe the syntax of natural languages
    - Define a class of languages called context-free languages
- Backus Normal / Naur Form (1959)
    - Invented by John Backus to describe Algol 58 and refined by Peter Naur for Algol 60
    - BNF is equivalent to context-free grammars

## BNF
- Rule has a left-hand side (LHS) which is a single `non-terminal` symbol and a right-hand side (RHS), one or more `terminal` or *non-terminal* symbols
- ``grammar` is a finite, nonempty set of rules
- A *non-terminal* symbol is "defined" by its rules
- Multiple rules can be combined with the vertical-bar ( | ) symbol (read as "or")
- These two rules
$$<stmts> ::= <stmt>$$
$$<stmts> ::= <stmnt> ; <stmnts>$$
- Are equivalent to this one:
$$<stmts> ::= <stmt> | <stmnt> ; <stmnts>$$
- *metalanguage*: language used to describe another language
- In BNF, *abstractions* are used to represent classic of syntactic structures -- they act like syntactic variables (also called **nonterminal symbols**), e.g.
$$<while_stmt> ::= while <logic_expr> do <stmt>$$
- This is a *rule*; it describes the structure of a while statement

### Non-terminals, pre-terminals & terminals
- A `non-terminal` symbol is any symbol that is in the LHS of a rule. These represent abstractions in the language
- e.g., *if-then-else-statement*

\<if-then-else-statement> ::= if\<test> then \<statement> else \<statement>
- A `terminal` symbol is any symbol that is not on the LHS of a rule. AKA *lexemes*. These are the literal symbols that will appear in a program (e.g., *if, then, else* in rules above)
- A `pre-terminal` symbol is one that appears as a LHS of rule(s), but in every case, the RHSs consist of single terminal symbol, e.g., <digit> in:
- \<digit> ::= 0 | 1 | 2 | 3 ... 7 | 8 | 9

## BNF (continued)
- Repetition is done with recursion
- E.g., syntactic lists are described in BNF using recursion
- An <ident_list> is a sequence of one or more \<ident>s separated by commas

$$<ident_list> ::= <ident> | <ident>, <ident_list>$$

### BNF Example
- Example of a simple grammar for a subset of English
- Sentence is noun phrase and verb phrase followed by a period.

- \<sentence> ::= \<nounPhrase> \<verbPhrase>
- \<nounPhrase> ::= \<article>\<noun>
- \<article> ::= a | the
- \<noun> ::= man | apple | worm | penguin
- \<verbPhrase> ::= \<verb> | \<verb> \<nounPhrase>
- \<verb> ::= eats | throws | sees | is$$

## Derivations
- repeated application of rules, starting with the start symbol and ending with a sentence consisting of just all terminal symbols
- it demonstrates, or proves that the derived sentence is "generated" by the grammar and is thus in the language that the grammar defines
- Every string of symbols in the derivation is a *sentential form*
- A *sentence*: sentential form that has only terminal symbols
- A *leftmost derivation*: leftmost nonterminal in each sentential form is the one that is expanded in the next step
- Derivation may be either leftmost or rightmost or something else


### Derivation using BNF
- derivation for "the man eats the apple."
    - \<sentence> = \<nounPhrase>\<verbPhrase>
    - \<sentence> = \<article>\<noun>\<verbPhrase>
    - \<sentence> = the \<noun>\<verPhrase>
    - \<sentence> = the man \<verbPhrase>
    - \<sentence> = the man \<verb>\<nounPhrase>
    - \<sentence> = the man eats\<nounPhrase>
    - \<sentence> = the man eats \<article>\<noun>
    - \<sentence> = the man eats the \<noun>
    - \<sentence> = the man eats the apple

### Another BNF Example
- \<program> -> \<stmts>
- \<stmts> -> \<stmt> | \<stmt> ; \<stmts>
- \<stmt> -> \<var> = \<expr>
- \<var> -> a | b | c | d
- \<expr> -> \<term> + \<term> | \<term> - \<term>
- \<term> -> \<var> | const

- derivation
- \<program> => \<stmts>
    - => \<stmt>
    - => \<var> = \<expr>
    - => a = \<expr>
    - => a = \<term> + \<term>
    - => a = \<var> + \<term>
    - => a = b + \<term>
    - => a = b + const

## Finite and Infinite languages
- simple language may have a finite number of sentences
- The set of strings representing integers between $-10^6$ and $+10 ^6$ is a finite language
- finite language can be defined by enumerating the sentences, but using a grammar might be much easier
- Most interesting language have an infinite sentences

### Is English a finite or infinite language?
- Assume we have a finite set of words
- Consider adding rules like the following to the previous example
    - \<sentence> ::= \<sentence>\<conj>\<sentence>
    - \<conj> ::= and | or | because

- Hint: Whenever you see recursion in a BNF it’s likely that
the language is infinite.
    - recursive rule might not be reachable, there might be epsilons

## Parse Tree
- Hierarchical representation of a derivation

```
    <program>
        |
     <stmts>
        |
      <stmt>
  /     |       \
<var>   =      <expr>
  |         /     |   \
  a      <term>   +  <term>
            |           |
          <var>        const
          |
          b
```

```
         <sentence>
         /        \
<nounPhrase>    <verbPhrase>
    /     \         /    \
<article> <noun> <verb>    <nounPhrase>
    |       |       |       /        \
   the     man     eats  <article>  <noun>
                            |          |
                           the       apple

```

## Grammar
- `ambiguous` *if and only if*(iff) it generatese a sentential form that has two or more distinct parse trees
- Ambiguous grammars are, in general, very undersirable in *formal languages*
- We can eliminate ambiguity by revising the grammar

### Ambiguous grammar
- Simple grammar for expressions that is ambiguous
    - expression: code that is evaluated and produces a value
    - staement: code that is executed and does something but does not produce a value

- \<e> -> \<e> \<op> \<e>
- \<e> -> 1 | 2 | 3
- \op -> + | - | * | /

- The sentence 1 + 2 * 3 can lead to two different parse trees corresponding to 1 + (2 * 3) and (1 + 2) * 3

#### Two derivations for 1 + 2 * 3
```
<e> -> <e> <op> <e>
    -> 1 <op> <e>
    -> 1 + <e>
    -> 1 + <e> <op> <e>
    -> 1 + 2 <op> <e>
    -> 1 + 2 * <e>
    -> 1 + 2 * 3
```

```
<e> -> <e> <op> <e>
    -> <e> <op> <e> <op> <e>
    -> 1 <op> <e> <op> <e>
    -> 1 + <e> <op> <e>
    -> 1 + 2 <op> <e>
    -> 1 + 2 * <e>
    -> 1 + 2 * 3
```

#### Example 2: ambiguous expression grammar
- \<expr> -> \<expr>\<op>\<expr> | const
- \<op> -> / | -
```
                   <expr>
            /          |     \
        <expr>       <op>  <expr>
    /    |    \        |      |
<expr> <op>  <expr>    /    const
   |     |      |
const    -    const

```

```
                <expr>
          /      |          \
     <expr>    <op>       <expr>
        |       |      /    |   \
     const      -   <expr> <op> <expr>
                       |    |       |
                    const   /     const 
```

## Summary
- Syntax of a programming language is usually defined using BNF or a context free grammar
- In addition to defining what programs are syntactically legal, a grammar also encodes meaningful or useful abstractions (e.g., block of statements)