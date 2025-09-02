# Lecture 1

## Topics
- Why study PL concepts?
- Programming domains
- PL evaluation criteria
- What influences PL design?
- Tradeoffs faced by programming languages
- Implementation methods
- Programming environments

## Programming Language
- formal constructed language
- communicate instructions to a machine
- to create programs
- express algorithms
- syntax (form) and semantics (meaning)

## Attempts to define PL
- a tool for humans to tell the computer what to do
- a means of formal and exact communication between humans
- a way of describing an abstract machine
- a way of describing computation that is readable by both man and machine

## Why programming languages
- enhanced ability to learn new languages
- borrowing ideas from other languages
- ability to express ideas and programming concepts
- ``Choice`` of programming language
- understanding the implementation behind languages
- mastering different programming paradigms
- designing your own "programming language"

## Programming Language Properties
- universal
    - every problem must have a programming solution
    - any language in which we can define recursive functions is universal
- Reasonably *natural* for solving problems within its intended application area
- **Implementable** on a computer
    - Possible to execute every well-formed program in the language
    - Mathematical notation is not implementable (it is possible to formulate problems that cannot be solved in any computer)
- Acceptably efficient implementation

## Language Evaluation Criteria
- **Readability**: programs can be read and understood
- **Writability**: language can be used easily to create programs
- **Reliability**: performs to its specifications
- **Cost**: the ultimate total cost
- **Portability**: moved from one to another
- **Generality**: wide range of applications

## Readability
- How easy it is to read and understand programs written in the programming language
- ``Arguably the most important criterion!``
- Factors effecting readability include:
    - **Overall simplicity**
    - **Orthogonality**
    - **Control Statements**
    - **Data type and structures**
    - **Syntax considerations**

### Readability: Simplicity
- Too many features is bad, as is a multiplicity of features
- PL with a large number of basic components are harder to learn
- Most programmers using these languages tend to learn and use subsets of the whole language
- Complex languages have multiplicity (more than one way to accomplish an operation)
- Overloading operators can reduce the clarity of the program's meaning

### Readability: Orthogonality
- relatively small set of primitive constructs can be combined in a relatively small number of ways to build the control and data structures of the language
    - Makes the language easy to learn and read
    - Meaning is context independent
- Language constructs should not behave differently in different contexts
- Exceptional situations are the causes of nonorthogonalities
- Modula-2, an example of nonorthogonality
    - Constant expressions may not include function calls
- Examples of nonorthogonalities:
    - In C/C++ arrays, types cannot be returned from a function
    - In C, local variables must be at the beginning of a block
    - C passes ALL paramaters by value except arrays (passed by reference)

### Data Types and Structures
- A more diverse set of data types and the ability of programmers to create their own increased program readability:
- Booleans make programs more readable:
    - TimeOut = I vs. TimeOut = True
- The use of records to store complex data objects make programs more readable:

```
CHARACTER*30 NAME(100)
INTEGER AGE(100), EMPLOYEE_NUM(100)
REAL SALARY(100)
```
**Wouldn't it be better if these were an array of records instead of 4 parallel arrays?**

### Syntax
- Most syntacic features in a programming language can enhance readability:
- Identifier forms - older languages (like FORTRAN) restrict the length of identifiers, which become less meaningful
- Special words - in addition to **while**, **do** and **for**, some languages use special words to close structures such as **endif** and **endwhile**. - Form and meaning
- In C a **static** variable within a function and outside a function mean two different things - this is undersirable.

### Evaluation Criteria: Writability
- How easy is it to write program in the language?
- Factors effecting writability:
    - Simplicity and orthogonality
    - Support for abstraction
    - Expressivity: set of relatively convenient ways of specifying operations
    - Fit for the domain and problem

### Evaluation Criteria: Reliability
- ``Type Checking`` 
    - a large factor in program reliability
    - Compile-time type checking is more desirable
    - C's lack of parameter type checking leads to many reliability problems
- ``Exception Handling``
    - the ability to catch runtime errors and make corrections can prevent reliability problems
- ``Aliasing``
    - having two or more ways of referencing the same data object can cause unnecessary errors

### Evaluation Criteria: Cost
- Categories:
    - Programmer training
        - Low training, low cost
    - Software creation
        - shorter creation time, low cost
    - Compilation
        - easier compilation, less cost
    - Execution
        - fast execution and less memory and less effort, less cost
    - Compiler cost
        - the compiler cost must be little
    - Poor reliability
        - more cost to maintain / fix
    - Maintenance
        - good code, less maintenance, less cost

### Evaluation Criteria: Others
- Portability
    - portable to any machine
- Generality
    - generality of the type of problems
- Well-definedness: completeness and precision of the language's official definition
- Good fit for hardware (e.g. cell) or environment (e.g., Web)
- etc.

## Recap Language Evaluation Criteria

| | | Criteria | |
| -- | -- | -- | -- |
| Characteristic | Readability | Writability | Reliability |
| Simplicity | V | V | V |
| Orthogonality | V | V | V |
| Data Types | V | V | V |
| Syntax Design | V | V | V |
| Support for abstraction | | V | V |
| Expressivity |  | V | V |
| Type Checking |  | | V |
| Exception handling |  | | V |
| Restricted aliasing |  | | V |

## Language Design Trade-Offs
- Reliability better = more cost of execution
    - Java demands all references to array elements be checked for proper indexing, leading to increased execution costs
- Readability better = worse writability
    - APL provides many powerful operators(and a large number of new symbols), allowing complex computations to be written in a compact program but at the cost of poor readability
- Writability (flexibility) better = reliability must be better
    - **IF THE COMPILER CAN HANDLE THE COMPLEX CODE**
    - C++ pointers are powerful and flexible, but unreliable

## Von Neumann Architecture

```
[            Memory             ]
^    |             ^    |
|    v             |    v
[Control]------>[Aritmetic]
[Unit]<--------[logic unit]
               [    []    ]
Processor       Accumulator
```

## Influences on Language Design
- Computer Architecture
    - languages are developed around the prevalent computer architecture, known as the **von Neumann** architecture
- Program Design Methodologies
    - New software development methodologies (e.g., object-oriented software development) led to new programming paradigms and by extension, new programming languages

```
New Methodologies -> New programming paradigm -> New programming languages
```

## Language Design Influences: Computer Architecture
- we use imperative languages, at least in part, because we use von Neumann machines
    - John von Neumann is generally considered the inventor of the "stored program" machines, the class to which most of today's computers belong
    - One CPU + one memory system that contains *both* program and data
- Focus on moving data and program instructions between registers in CPU to memory locations
- Fundamentally sequential

## Language Design Influences: Programming methodologies
- ``50s and early 60s``: Simple applications; worry about machine efficiency
- ``Late 60s``: People efficiency became important; readability, better control structures. maintainability
- ``Late 70s``: Data abstraction
- ``Middle 80s``: Object-oriented programming
- ``90s``: distributed programs, Internet
- ``00s``: Web, user interfaces, graphics, mobile, services
- ``10s``: parallel computing, cloud computing?, pervasive computing?, semantic computing?, virtual machines?

## Language Categories
- The big four PL paradigms:
    - Imperative or procedural (e.g., Fortran, C)
    - Object-oriented (e.g., Smalltalk, Java)
    - Functional (e.g., Lisp, ML)
    - Rule based (e.g., Prolog, Jess)
- Others:
    - Scripting (e.g., Python, Perl, PHP, Ruby)
    - Constraint (e.g., Eclipse)
    - Concurrent (Occam)
    - ...

## Implementation methods
- Direct execution by hardware
    - e.g., native machine language
- Compilation to another language
    - e.g., C compiled to native machine language
- Interpretation: direct execution by software
    - e.g., csh, Lisp (traditionally), Python, JavaScript
- Hybrid: compilation then interpretation
    - Compilation to another language (aka bytecode), then interpreted by a 'virtual machine', e.g., Java, Perl
- Just-in-time compilation
    - Dynamically compile some bytecode to native code (e.g., V8 javascript engine)

## Implementation issues
1. Complexity of compiler/interpreter
    -  compiler more complex
2. Translation speed
    - Interpreter slower
3. Execution speed
    - Compiler faster
4. Code portability
    - Interpreter better
5. Code compactness
    - Interpreter less compact
6. Debugging ease
    - Interpreter easier


```
3                  1,2,4,5,6
<--------------------------->
Compile    Hybrid    Interpret    
```

## Programming Environment
- collection of tools used in software development, often including an integrated editor, debugger, compiler, collaboration tool, etc
- Modern Integrated Development Environments (IDEs) tend to be language specific, allowing them to offer support at the level at which the programmer thinks
- Examples
    - UNIX -- OS with tool collection
    - EMACS -- highly programmable text editor
    - Smalltalk -- A language processor/environment
    - Microsoft Visual C++ -- A large, complex visual environment
    - Favorite Java environment: BlueJ, Jbuilder, J++,...
    - Generic: IBM's Eclipse

## Summary
- Programming languages have many aspects and uses
- There are many reasons to study the concepts underlying PL
- There are several criteria for evaluating PLs
- PLs are constantly evolving
- Classic techniques for executing PLs are compilation, and interpretation, with variations