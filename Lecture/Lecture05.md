# Programming Languages Names, Bindings, and Scopes

## Chapter 5 Topics
- [Introduction](#introduction)
- [Names](#names)
- [Variables](#variables)
- [The Concept of Binding](#the-concept-of-binding)

## Introduction
- Imperative languages are abstractions of von Neumann architecture
    - Memory
    - Processor
- Variables are characterized by attributes
    - To design a type, must consider scope, lifetime, type checking, initialization, and type compatibility

- Variables
    - Name
    - Address
    - Scope
    - Lifetime
    - Type
    - Value

## Names
- name is a fundamental attribute of variables
- The term *idenitifier* is often used interchangeably with *name*
- Design issues for names:
    - Are names case sensitive?
    - Are special words reserved words or keywords
    - length
    - Special characters

### Length
- Earliest programming languages used single-character names
- If too short, they cannot be connotative
- Language examples:
    - FORTRAN 95: maximum of 31
    - C99: no limit but only the first 63 are significant; also, external names are limited to a maximum of 31
    - C#, Ada, and Java: no limit, and all are significant
    - C++: no limit, but implementers often impose one

### Special characters
- PHP: all variable names must vegin with dollar signs
- Perl: all variable names begin with special characters, which specify the variable's type
    - $: Scalar variable
    - @: Array variable
    - %: Hash variable
- Ruby: variable names that begin with @ are instance variables
    - $: global variable
    - @: instance variable
    - [a - z] or _: local variable
    - [A - Z]: a constant
    - @@: class variable

### Case sensitivity
- Disadvantage: readability (names that look alike are different)
    - names in the C-based languages are case senstive
    - names in others are not
    - Worse in C++, Java, and C# because predefined names are mixed case (e.g. IndexOutOfBoundsException)
- "Case sensitive" is always better to reduce ambiguity 

### Special words
- An aid to readability; used to delimit or separate statement clauses
- A *keyword* is a word that is special only in certain contexts, e.g., in Fortran
- Real VarName (Real is a data type followed with a name, therefore Real is a ketword)
- Real = 3.5 (Real is a variable)
- A `reserved word` is a special word that cannot be used as a user-defined name
- Potential problem with reserved words: if there are too many, many collisions occur (e.g., COBOL has 300 reserved words!)

## Variables
- A variable is an abstract of a memory cell
- Variables can be characterized as a sextuple of attribtes:
    - Name
    - Address
    - Value
    - Type
    - Lifetime
    - Scope

### Variable Attributes
- Name
    - not all variables have them
- [Address](#variable-address)
    - the memory address with which it is associated
    - A variable may have `different addresses at different times` during execution
- [Type](#static-and-dynamic-binding-variable-type)
    - determines the range of values of variables and the set of operations that are defined for values of that type; in the case of floating point, type also determines the precision
- Value
    - the contents of the location with which the variable is associated
        - The l-value of a variable is its adress
        - The r-value of a variable is its value
    > x = 7
    - x: l-value
    - 7 = r-value
    - Abstract memory cell
        - the physical cell or collection of cells associated with a variable
- [Storage Bindings & Lifetime](#categories-of-variables-by-lifetimes)
    - Allocation - getting a cell from some pool of available cells
    - Deallocation - putting a cell back into the pool
    - The lifetime of a variable is the time during which it is bound to a particular memory cell


### Variable Address
- A variable may have `different addresses at different places` in a program
- If two variable names can be used to access the same memory location, they are called `aliases`
- Aliases are created via pointers, reference variables, C and C++ unions
- Aliases are harmful to readability (program readers must remember all of them)

### Aliases
- Java (aliasing available with objects)
```java
Rectangle box1 = new Rectangle (0, 0);
Rectangle box2 = box1;
```

- C++
```cpp
int main() {
    int a = 0;
    int &b = a; //alias
    int *c = &a; //alias

    cout << a << b << *c << endl;
    a = 7;
    cout << a << b << *c;
    //all the same
    return 0;
}
```

- Python (aliasing applied directly)
```py
# Assign a value to a new variable
a = 5
# Create an alias identifier for this variable
b = a
# Observe how they refer to the same variable!
print(id(a), id(b))
# Create another alias
c = b
# Now assign a new value to b!
b = 4
# And observe how a and c are still
# the same variable # but b is not
print (a,b,c)
print(id(a), id(b), id(c))

```

## The Concept of Binding
- `binding`
    - association between an entity and an attribute
        - such as between a variable and its type or value
        - between an operation and a symbol
- *binding time* is the time at which a binding takes place

### Possible Binding Times
- Language design time
    - bind operator symbols to operations
- Language implementation time
    - bind floating point type to a representation
- Compile time
    - bind a variable to a type in C or Java
- Load time
    - bind a C or C++ static variabele to a memory cell
- Runtime
    - bind a nonstatic local variable to a memory cell

#### Example
> count = count + 5;
- The `type` of count is bound at `compile time`.
- The set of possible values of count is bound at `compiler design time`
- The meaning of the operator symbol `+` is bound at `compile time`, when the types of its operands have been determined.
- The internal representation of the literal 5 is bound at `compiler design time`.
- The value of count is bound at `execution time` with this statement.

### Binding Time: Static and Dynamic
- `static binding`
    - first occurs before run time and remains unchanged throughout program execution
    - before run time
- `dynamic binding`
    - first occurs during execution or can change during execution of the program
    - After run time

#### Static and Dynamic Binding Variable Type
- Overridden instance methods are bound at `run time`; and this kind of binding depends on the instance object type

- For example in Java:
```java
public class Parent {
    public void writeName() {
        System.out.println("Parent");
    }
}

public class Child extends Parent {
    public void writeName() {
        System.out.println("Child");
    }
}

public static void main(String [] args) {
    Parent p = new Child();
    p.writeName();
}
```

- The instance variables, static variables, static overridden methods, and overloaded methods are all bound at `compile time`; and this kind of binding depends on the type of the reference variable and not on the object

```java
public class Parent {
    public static String age = "50";
    public String hairColor = "grey";
    public void writeName() {
        System.out.println("Parent");
    }
}

public class Child extends Parent {
    public static String age = "20";
    public String hairColor = "brown";
    public void writeName() {
        System.out.println("Child");
    }
    public void writeName(String order) {
        System.out.println(order + "Child");
    }
}

public static void main(String [] args) {
    Parent p = new Child();
    System.out.println("Age: " + p.age);
    System.out.println("Hair Color: " + p.hairColor);
    Child c = new Child();
    c.writeName("first");
}
```

```
Age: 50
Hair Color: Grey
first Child
```

### Variable Type Binding
- How is a type specified?
- When does the binding take place?
- If static, the type may be specified by either an explicit or an implicit declaration

#### Explicit / Implicit Declaration
- Explicit declaration
    - program statement used for declaring the types of variables
- Implicit declaration
    - default mechanism for specifying types of variables through default conventions, rather than declaration statements
- Fortran, BASIC, Perl, Ruby, JS, and PHP provide implicit declarations (Fortran has both explicit and implicit)
    - Advantage: writability (a minor convenience)
    - Disadvantage: reliability (less trouble with Perl)

- Some languages use type inferencing to determine types of variables (context)
    - C# - a variable can be declared with `var` and an initial value
        - The initial value sets the type
        ```c#
        var sum = 0;
        var total = 0.0;
        var name = "Fred";
        ```
    - Visual BASIC 9.0+, ML, Haskell, F#, and Go use type inferencing. 
        - The context of the appearance of a variable determines its type

### Dynamic Type Binding
- JS, Python, Ruby, PHP, and C#(limited)
- Specified through an assignment statement
    - e.g., JS
        ```js
        list = [2, 4.33, 6 , 8]; //array
        list = 17.3; //float
        ```
- Advantage: flexibility (generic program units)
- Disadvantages:
    - High cost (dynamic type checking and interpretation)
    - Type error detection by the compiler is difficult

## Categories of Variables by Lifetimes
- `Static`--bound to memory cells before execution begins and remains bound to the same memory cell throughout execution, e.g., C and C++ static variables in functions
    - Advantages: 
        - efficiency (direct addressing)
        - history-sensitive subprogram support
    - Disadvantage: lack of flexibility (no recursion)

- `Stack-dynamic`--Storage bindings are created for variables when their declaration statement are *elaborated*
    - A declaration is elaborated when the executable code associated with it is executed

    - If scalar, all attributes except address are statically bound
        - local variables in C subprograms (not declared **static**) and Java methods

    - Advantage:
        - allows recursion
        - conserves storage
    - Disadvantages:
        - Overhead of allocation and deallocation
        - Subprograms cannot be history sensitive
        - Inefficient references (indirect addressing)

- `Explicit heap-dynamic`--Allocated and delallocated by explicit directives, specified by the programmer, which take effect during execution
    - Referenced only through pointers or references, e.g., dynamic objects in C++ (via **new** and **delete**), all objects in Java
    - Advantage: provides for dynamic storage management
    - Disadvantage: inefficient and unreliable

- `Implicit heap-dynamic`--Allocation and deallocation caused by assignment statements
    - all variables in APL; all strings and arrays in Perl, JS, and PHP
    - Advantage: flexibility (generic code)
    - Disadvantages:
        - Inefficient, because all attributes are dynamic
        - Loss of error detection

## Summary
- Introduction
- Names
- Variables
- The Concept of Binding