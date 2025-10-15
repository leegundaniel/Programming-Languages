# Programming Languages Names, Bindings, and Scopes II
## Chapter 5 Topics
- [Scope](#scope)
- [Scope and Lifetime](#lifetime-and-scope)
- [Named Constants](#constants)
- [Referencing Environments](#referencing-environments)

## Recap: Variables
- Imperative languages are abstractions of von Neumann architecture
    - memory
    - processor
- Variables are characterized by attributes
    - to design a type, must consider scope, lifetime, type checking, initialization, and type compatibility

## Scope
- scope of a declaration or scope of a binding: region of the program to which a binding applies
- scope of a variable: the range of statements over which it is visible
- `local variables` of a program unit are those that are declared in that unit
- `nonlocal variables` of a program unit are those that are visible in the unit but not declared there
- `global variables`: special category of nonlocal variables
- every language has scope rules which define the schope of declarations, definitions, etc.
- Two broad classes of scope rules:
    - static or lexical scope: scope determined by structure of program
    - dynamic scope: scope determined by path of execution

### Static or lexical scope
- based on prgoram code
- to connect a name reference to a variable, you (or the compiler) must find the declaration
- `Search process`: search declarations, first locally, then in increasingly larger enclosing scopes, until one is found for the given name
- Enclosing static scopes (to a specific scope) are called its `static ancestors`; the nearest static ancestor is called a `static parent`
- Some languages allow nested subprogram definiitions, which create nested static scope (e.g., Ada, JS, Common LISP, Scheme, Fortran 2003+, F# and Python)

#### Nested functions: Python
```py
def percent(a,b,c):
    def pc(x):
        return (x*100.0) / (a+b+c)
    print("Percentages are:", pc(a), pc(b), pc(c))

def outside(x):
    print(x)
    local = 7
    def inside():
        print("inside", x, local)
    return inside
```
#### Static or lexical scope hierarchy
- Global scope
    - the names of all classes defined in the program
- Class scope (OOP languages)
    - instant scope: all fields and methods of the class
    - static scope: all static methods
    - scope of subclass nested in scope of its superclass
- Method scope
    - formal parameters and local variables in code block of body method
- Code block scope
    - variables defined in block

#### Global Scope: Python
- A global variable can be referenced in funcitons, but can be assigned in a function only if it has been declared to be global in the function
```py
# access global variable in a function
globalvar = 5
def f():
    anotherVariable = globalvar + 8

# modifying global variable in a function
globalvar = 5
def f():
    global globalvar
    globalvar += 5
```

#### Scope Example: C
```c
// what are the scopes of vars?
int  n = 999; // global
int sub1() {
    int n = 10; // local
    // will use local
    printf("sub1: n = %d\n", n);
}

int sub2() {
    // will use global variable
    printf("sub2: n = %d\n", n);
}

int main() {
    // will use global variable
    printf("main: n = %d\n", n);
    int n = 50;
    sub1(); // n = 10
    sub2(); // n = 999
    printf("main: n = %d\n", n); // n = 50
}
```

#### Scope Example: C++
- in C++, names can be defined in any {...} block
- scope of name is from <u>point of declaration</u> to the end of the block
- Local scope can create "scope holes" for names in outer scopes
    - Example: while loop creates scope hole for "int x"

```c++
//what are the scopes of x?
int sub1() {
    int x = 10;
    double sum = 0;
    for(int k = 0; k < 10; k++) {
        cout << "x= " x << endl; // x = 10 (scope hole)
        double x = pow(2.0, k);
        sum += x; // uses local scope
    }
    // what is the value of x
}

```

#### Scope Example: Java
- scope of class members is entire class (can define anywhere)
- scope of local name is from <u>point of declaration</u> to the end of the block
```java
class Foo {
    int value; // class scope
    int test() {
        int b = 3; // local variable
        return value + b;
    }
    void setValue(int C) {
        value = c; // scope of formal parameter c
        {
            int d = c; // local variable
            c = c + d;
            value = c;
        }
    }
}

class Bar extends Foo {
    int value; // local variable
    void setValue(int c) {
        value = c; // scope of c
        test();
    }
}
```
```java
class A {
    public A(String name) {
        this.name = name;
    }
    publis String getName() {
        return name;
    }
    int sum(int n) {
        int sum = 0; // local name = method name
        for(int k = 1; k <= n; k++) {
            sum = sum + k;
        }
        return sum
    }
    private String name; // defined after use
}
```

- Inside of a method, a block may not redefine a name (flat namespace inside of methods)
```java
class A {
    int sum(int n) {
        int sum = 0; // OK
        for(int k = 1; j <= n; k++) {
            int sum = 0; // Illegal duplicate
            sum = sum + k++;
        }
        // Error: k is out of scope
        System.out.println(k);
    }
}
```

#### Scope Example: multiple files
- In C and C++ external variables have global scope unless declared "static", which indicates file scope.
```c
// File1.c
static char *s = "dog";
// external var & function
// using linker
extern int n;
extern int sub2();

int sub1() {
    printf("%s %d", s, n);
    return n;
}

int main() {
    int s = 0, n = 0;
    printf("%d", sub2()); // cat 10 1000
    printf("%d", sub1()); // dog 1000 1000
}
```
```c
// File2.c
static char *s = "cat";
int n = 10;

int sub2() {
    printf("%s %d", s, n);
    n = 1000;
    return n;
}
```

- Duplicate names will be detected by the linker (not the compiler)
```c
// File1.c
// multiple definition error
char *s = "file1";
int base = 7;

int sub1(int x) {
    printf("sub1 %s", s);
    return x % base;
}
int sub3() {return 1;}
int main() {
    sub1(10);
    sub2(s);
    sub3();
}
```
```c
// File2.c
// multiple definition error
char *s = "file2";
extern int base;

int sub1(int);
void sub2(char *s) {
    sub1(base + 5);
    printf("sub2 %s", s);
}

int sub3() {
    printf("sub3 %s", s);
    return 2;
}

```


#### Scope Rules for C, C++, and Java
- most compiled languages use **static scope**
- Local variables: scope is in the block in which variable is declared
    - a block is enclosed by {...}, a function, or a "for()" loop
- Parameters: scope is the function or method
- Class attributes: scope is the class definition
- Functions (C)
    - global scope
    - must include prototype in other files to use a function
    - linker will resolve function references
- External variables
    - global scope unless declared "static"
    - "static" externals have file scope
    - "extern" declares a variable whose definition is in another file
        - "extern" will not allocate storage for a variable

### Dynamic Scope
- Perl and some LISP versions use dynamic scope.
- scope of variable follows path of execution
```lisp
sub sub1 {
    print "sub1:x = $x\n"; 
    $x = "Elephants";
}

sub sub2 {
    print "sub2: x = $x\n"; 
    $x = "Rats!";
    sub1();
}

sub main {
    $x = 10;
    print "main: x = $x\n"; //main: x = 10
    sub1(); // sub1: x = 10
    print "main: x = $x\n"; // main: x = Elephant
    sub2(); // sub2: x = Elephant sub1: x = Rats!
    print "main: x = $x\n"; // main: x = Rats!
}
```

- "local" defines a new variable with dynamic scope
```lisp
sub sub1 {
    print "sub1:x = $x\n"; 
    $x = "Elephants";
}

sub sub2 { local $x; // copy and use it from now on
    print "sub2: x = $x\n"; 
    $x = "Rats!";
    sub1();
    print "sub2: x = $x\n"; 
}

sub main {
    $x = 10;
    print "main: x = $x\n"; // main: x = 10
    sub2(); // sub2: x =  sub1: x = Rats! sub2: x = Elephants
    print "main: x = $x\n"; // x = 10
}
```

- "my" defines a new variable with lexical scope
```lisp
sub sub1 {
    print "sub1:x = $x\n"; 
    $x = "Elephants";
}

sub sub2 { my $x;  // new local variable
    print "sub2: x = $x\n"; 
    $x = "Rats!";
    sub1();
    print "sub2: x = $x\n"; 
}

sub main {
    $x = 10;
    print "main: x = $x\n"; // main: x = 10
    sub2(); // sub2: x =  sub1: x = 10! sub2: x = Rats!
    print "main: x = $x\n"; // x = Elephants
}
```

### Lexical vs. Dynamic Scope
- scope is maintained by the properties of the lookup operation in the symbol table
- Static (lexical) scope: scope of names is known to the compiler
    - permits type checking by compiler
    - can easily check for uninitialized variables
    - easier to analyze program correctness
- Dynamic scope: meaning of variables is known only at run-time
    - cannot perform type checking before execution
    - programs are more flexible, but harder to understand & debug
    - almost always implemented using interpreter (Perl uses a just-in-time compiler, but no type checking)

### Scope holes
- Scope hole is a region where a new declaration hides another binding of the same name
```java
class ScopeHole {
    final String s = "global";
    String sub1() {return s;}
    String sub2(int which) {
        String s = "local";
        if(which == 1) return sub1();
        else return s;
    }
    void ScopeHole() {
        System.out.println("0: s = " + s); // global
        System.out.println("1: s = " + sub2(1)); // global
        System.out.println("0: s = " + sub2(2)); // local
    }
}
```

### Why limit scope of names?
- What are advantages of limiting scope of names?
- What would be the problem of making all names be global? Assume all variables are global...
```c
// sum.c
int n, total;

int sum() {
    total = 0;
    for(n = 1; n < 10; n++)
        total += product(n);

    printf("%d\n", total);
}
```

```c
// product.c
int n, total;

int product(int k) {
    total = 1;
    for(n = 1; n < k; n++)
        total += n;
    return total;
}
```

### Techniques to limit name collision
1. Limit scope of variables:
    - File scope:
        - static int MAX;
    - Function scope:
        - int sum(int n) {...}
    - Block scope:
        - for(int k= ...) {...}
```c
// file scope
static int MAX = 100;

// function scope
int sum(int n) {
    int total = 0;
    // block scope in C++
    // not in standard C
    for(int k=0; k<n; k++)
        total = total + k;
    return total;
}

```

2. For broader scopes, including scope of functions and variables:
    - Nested procedures in Pascal, Algol, Ada, ...
    - inner procedure can refer to other members of outer procedure.
    - scope of inner procedure is limited to the outer procedure
```pascal
procedure sub1(n: int)
var
    x: real;
    (* nested function *)
    procedure sum(n: int): int
    var
        k, t: int;
    begin
        t := 0;
        for k:=1 to n do
            t := t + k;
        return t;
    end sum;
begin (* start of sub1 *)
    x := sum(20);
    ...
end sub1;
```

3. Modules:
    - in Modula 1,2,3 and Ada
    - module encapsulates both variables and procedures
    - a module explicitly "exports" names it wants to make known to outside
    - Usage:
        ```ada
        var x,y,z: element;
        push(x);
        push(y);
        z := pop();
        ```

```Ada
CONST maxsize = 20;
Type element = INT;

MODULE stack;
EXPORT push, pop;
TYPE
    stack_index [1..maxsize];
VAR
    stack: ARRAY stack_index of element;
PROCEDURE push(x: element);
begin
    ...
end push;
PROCEDURE pop(): element;
begin
    ...
end pop;
END stack;
```
4. C++ and C# use "namespace" to encapsulate names
```cpp
using System;
using System.Data;
using System.Windows.Forms;
namespace MyApplication
{
    public class Form1 {
        public Dimension getSize() {
            ...
        }
        private double width;
        private double height;
        static void Main() {
            ...
        }
    }
}
```

5. What does Java use to define and use "namespace"
    - package
```java
package MyApplication;
import java.util.date;
import java.awt.*;

public class Form1 {
    public...
}
```

#### Purpose of "import"
- What does import java.util.*; 
do?
    - import all classes(*) from java.util library

- Does "import" effect the size of your program?
    - For example, would it be more efficient to write:
        >import java.util.Arrays;
    - instead of
        > import java.util.*;

- No, "import" statements have no effect on generated byte code and is mainly used for "readability" purposes of your source code

## Lifetime and Scope
- Scope of identifiers and lifetime of entity
    - what they both refer to are not the same
- Lifetime: time when entity exists in memory
- scope: the parts of a program where a name is known or "visible"
```c
void add(int count) {
    static long SUM = 0;
    float x = 0.5;
    while (count > 0) {
        int x = 2;
        SUM += x * count;
        count--;
    }
    printf("%f", x);
}
```
- count: 
    - scope: function add(); 
    - lifetime: unknown
- SUM:
    - scope: function body
    - lifetime: process execution time
- float x:
    - scope: part of the function excluding while loop
    - lifetime: function activation time
- int x:
    - scope: while loop
    - lifetime: duration of while loop

```c
int BUFSIZE = 1024;
static char buf[BUFSIZE];
void read(int length) {
    int k;
    for(k = 0; k < length; k++) {
        int c = getchar(); if (c<0) break;
        buf[k] = 0;
    }
    buf[k] = '\0';
}
```
- BUFSIZE:
    - scope: global (any file in this program can refer to its value)
    - lifetime: process's lifetime
- buf:
    - scope: file
    - lifetime: program's lifetime
- length, k:
    - scope: function
    - lifetime: duration of function
- c:
    - scope: for loop
    - lifetime: duration of "for" loop execution

### Lifetime
- Lifetime is the duration of time that an entity (variable, constant, ...) is bound to memory
- Lifetime can be...
    - duration of process execution (static variables)
    - duration of object existence (object attributes)
    - duration of function activation (local variables)
    - duration of scope activation (variable defined in a scope). A function also defines a scope
- Lifetime applies to entities that have values, not names
- "Lifetime of an identifier" doesn't make sense... identifiers have "scope" rather than "lifetimes"

### Scope Example
- Check [PDF](Lecture06-PL.pdf)

### Scope and Lifetime (cont.)
- scope and lifetime are sometimes closely related, but are different concepts
- Consider a static variable in a C or C++ function

## Constants
- C "const" can be compile time, load time, or run time constants:
```c
const int MaxSize = 80; // compile time
void mysub(const int n) {
    static const NUMBER = 8 * sizeof(int);
    const time_t now = time(0); // dynamic
    const int LastN = n; // dynamic 
}
```
- In Java, "final" merely means a variable cannot be changed after the first assignment
```java
final InputStream in = System.in;
void mysub (int n) {
    final int LastN = n;
}
```

### Types of Constants
- There are several classes of constants, depending on when their value is known
    - compile time: value can be computed at compile time, includes:
        - manifest constants (literals): const int MAX = 1024;
        - computable expressions: const int MAXBYTES = 8*MAX;
    - elaboration time: value is determined when the program is executed
        - sometimes this simply means a variable whose value cannot be changed (this is enforced by the compiler)

### Declaration Order
- C99, C++, Java, and C# allow variable declarations to appear anywhere a statement can appear
    - In C99, C++, and Java, the scope of all local variables is from the declaration to the end of the block
    - In C#, the scope of any variable declared in a block is the whole block, regardless of the position of the declaration in the block
        - However, a variable still must be declared before it can be used

## Referencing Environments
- The referencing environment of a statement is the collection of all names that are visible in the statement
- In a static-scoped language, it is the local variables plus all of the visible variables in all of the enclosing scopes
- A subprogram is active if its execution has begun but has not yet terminated
- In a dynamic-scoped language, the referencing environment is the local variables plus all visible variables in all active subprograms

### Symbol table example
```cpp
class Foo {
    int value; // scope of value within Foo class
    int test() {
        int b = 3; // scope of b within test function
        return value + b;
    }
    void setValue(int c) { // scope of c within setValue()
        value = c; 
        // block
        {
            int d = c; // scope of d within block
            c = c + d;
            value = c;
        }
    }
}

class Bar {
    int value; // scope of value within Bar class
    void setValue(int c) { // scope of c within setValue()
        value = c;
    }
}
```

## Chapter 5 Summary
- Scope
- Scope and Lifetime
- Named Constants
- Referencing Environments