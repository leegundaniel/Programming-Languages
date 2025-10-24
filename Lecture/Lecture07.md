# Programming Languages Data Types

## Important Topics
- [What is a "type system"?](#introduction)
- [What are common data types?](#primitive-data-types)
- How are numeric types stored and operated on?
- Compound types: arrays, struct, records
- [Enumerated types](#enumeration-types)
- [Character and string types](#character)
- Tuple Types and List types
- Pointer and Reference Types
- Strong type checking versus not-so-strong
    - enumerations, type compatibility, and type safety
- Advantages & disadvantages of compile-time checking

## Introduction
- A `data type` defines a collection of data objects and a set of predefined operations on those objects
- A `descriptor` is the collection of the attributes of a variable
    - Symbol, kind, type, address, value, attributes
- An `object` represents an instance of a user-defined (abstract data) type
    ```java
    Student engStudent = new Student(......);
    ```
- One design issue for all data types: What operations are defined and how are they specified?

## Primitive data types
- Almost all programming languages provide a set of *primitive data types*
- `Primitive data types`: Those not defined in terms of other data types
- Some primitive data types are merely reflections of the hardware
- Others require only a little non-hardware support for their implementation

### Integers
- Almost always an exact reflection of the hardware so the mapping is trivial
- There may be as many as eight different integer types in a language
- C++:
    1. short int
    2. unsigned short int
    3. unsigned int
    4. int
    5. long int
    6. unsinged long int
    7. long long int
    8. unsinged long long int
- Java's signed integer sizes: byte, short, int, long
- Python: only one type of **signed integers**: int

#### Integer Data Types
- C / C++ support both "unsigned" and "signed" integer types

| Type | # Bytes | Range of values |
| -- | -- | -- |
| short int | 2 | -32,768 ($-2^{15}$) to 32,767 ($2^{15} - 1$)
| unsigned short | 2 | 0 to 65,535 ($2^{16} - 1$) |
| int | 4 | -2,147,483,647 ($2^{31} - 1$) |
| unsigned int | 4 | 0 to 4,294,967,295 ($2^{32} - 1$) |
| long int | - | same as "int" on Pentium and Athlon CPU |

- C permits "char" type for integer values, too...
    - char: -128 to 127
    - unsigned char: 0 to 255

### Floating Point
- Model real numbers, but only as approximations
- Languages for scientific use support at least two floating-point types (e.g., **float** and **double**; sometimes more)
- Usually exactly like the hardware, but not always
- IEEE Floating-Point Standard 754
    - Float (4 bytes): $\pm3.40282347E$ i.e. 6-7 significant digits
    - Double (8 bytes): $\pm1.79769313486231570E + 308$ i.e. 15-16 significant digits

### Complex
- Some languages support a `complex type`, e.g., C99, Fortran, and Python
- Each value consists of two floats, the real part and the imaginary part
- Literal form (in Python):
    - (7 + 3j), where 7 is the real part and 3 is the imaginary part

### Decimal
- For business applications (money)
    - Essential to COBOL
    - C# offers a decimal data type
- Store a fixed number of decimal digits, in coded from (BCD)
- *Advantage*: accuracy
- *Disadvantages*: linited range, wastes memory

### Boolean
- Simplest of all
- Range of values: two elements, one for "true" and one for "false"
- Could be implemented as bits, but often as bytes
    - Advantage: readability

### Character
- Stored as numeric coding
- Most commonly used coding: ASCII
- An alternative, 16-bit coding: Unicode (UCS-2)
    - Includes characters from most natural languages
    - Originally used in Java
    - C# and JS also support Unicode
- 32-bit Unicode (USD-4)
    - Supported by Fortran, starting with 2003

## Character String Types
- Values are sequences of characters
- Design issues:
    - Is it a primitive type or just a special kind of array?
    - Should the length of strings be static or dynamic?
- Character String Types Operations
    - Assignment and copying
    - Comparison (=, >, etc.)
    - Catenation
    - Substring reference
    - Pattern matching

### Character String Length Options
- `Static`: COBOL, Java's String class, Python
    - when updating string will delete previous string, and new string will be created
        - contain = "ThisisString"
        - contain = contain + "new"
- `Limited Dynamic` Length: C and C++
    - In these languages, a special character is used to indicate the end of a string's characters, rather than maintaining the length
        - NULL (\0) character
- `Dynamic` (no maximum): SNOBOL4, Perl, JS
- Ada supports all three string length options

#### Compile- and Run-Time Descriptors
- Static length: compile-time descriptor
- Limited dynamic length: may need a run-time descriptor for length (but not in C and C++)
- Dynamic length: need run-time descriptor; allocation / deallocation is the biggest implementation problem

- Compile-time descriptor for static strings
    - static string
    - length
    - address
- Run-time descriptor for limited dynamic strings
    - limited dynamic string
    - Maximum length
    - current length
    - address
## User-Defined Ordinal Types
- An ordinal type is one in which the range of possible values can be easily associated with the set of positive integers
- Examples of primitive ordinal types in Java
    - integer
    - char
    - boolean
- There are two kinds of ordinal types: **enumeration** and **subrange**

### Enumeration Types
- All possible values, which are named constants, are provided in the definition
- C# example
    ```c#
    enum days {
        mon, tue, wed, thu, fri, sat, sun
    };
    ```
- Design issues
    - Is an enumeration constant allowed to appear in more than one type definition, and if so, how is the type of an occurrence of that constant checked?
    - Are enumeration values coerced to integer?
    - Any other type coerced to an enumeration type?

#### Evaluation of Enumeration Types
- Aid to readability, e.g., no need to code a color as a number
- Aid to reliability, e.g., compiler can check:
    - operations (don't allow colors to be added)
    - No enumeration variable can be assigned a value outside its defined range
    - Ada, C#, and Java 5.0 provide better support for enumeration than C++ because enumeration type variables in these languages are not coerced into integer types

```c++
// C++
enum week_days {
    Sunday,
    Monday = 1,
    Tuesday,
    Wednesday = 1,
    Thursday,
    Friday = 9,
    Saturday
};

int main () {
    week_days variable = Thursday;
    // variable = 5; error
    // variable++; error
    variable = (week_days)5;
    int i = Sunday;
    // i = 0
    int j = 3 + Monday;
    // j = 4
    return 0;
}
```

```java
// Java
class Ideone
{
    enum BookType { HARDCOPY, EBOOK };
    // where the semicolon is optional
    public static void main (String[] args)
    {
        BookType bt1 = BookType.HARDCOPY;
        BookType bt2 = BookType.EBOOK;
        System.out.println(bt1);
    }
}
```

```java
public class MainClass {
    enum Week {
        Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    }

    public static void main(String args[]) {
        // Obtain all ordinal values using ordinal()
        System.out.println("Here are all week constants" + " and their ordinal values: ");
        for(Week day : Week.values())
            System.out.println(day + " " + day.ordinal());
    }
}
```
```
Here are all week constants and their ordinal values:
Monday 0
Tuesday 1
Wednesday 2
Thursday 3
Friday 4
Saturday 5
Sunday 6
```

### Subrange Type
- Set up the type to support range checking
- Contiguous subsequence of an ordinal type
- It is for readability and writability
- e.g. Ada's code
    ```ada
    type Days is (mon, tue, wed, thu, fri, sat, sun);
    subtype Weekdays is Days range mon..fri;
    subtype Index is Integer range 1..100;

    Day1: Days;
    Day2: Weekday;
    Day2 := Day1;
    ```

#### Subrange Evaluation
- Aid to readability
    - Make it clear to the readers that variables of subrange can store only certain range of values
- Readability
    - Assigning a value to a subrange variable that is ouotside the specified range is detected as an error

### Implementation of User-Defined Ordinal Types
- Enumeration types are implemented as integers
- Subrange types are implemented like the parent types with code inserted (by the compiler) to restrict assignments to subrange variables

## Important Topics
- [Type compatibility](#type-compatibility-for-built-in-types)
    - What are compatibility rules in C, C++, and Java?
    - When are user-defined types compatible?
- Type conversion
    - What conversions are automatic in C, C++, Java?
    - What conversions are allowed using a cast?

### Type Compatibility for built-in types
- **Operations** in most languages will automatically convert ("propmote") some data types:
    - 2 * 1.75 converts 2 (int) to floating point
- **Assignment compatibility**: what automatic type conversions are allowed on assignment?
    ```c
    int n = 1234567890;
    float x = n; // OK in C
    n = x; // allowed in C? Java?
    ```
- char -> short -> int -> long -> double
    - short -> int -> float -> double
- What about long -> float?
- Rules for C/C++ not same as Java

### C / C++ Arithmetic Type Conversion
- For +, -, *, /, both operands must be the `same type`
- C/C++ compiler "promotes" mixed type operands to make all operands same using the following rules:

| Operand Types | Promote | Result |
| -- | -- | -- |
| short op int | short => int | int |
| long op int | int => long | long |
| int op float | int => float | float |
| int op double | int => double | double |
| float op double | float => double | double |

### Assignment Type Conversion is not Arithmetic Type Conversion
```c
int m = 15;
int n = 16;
double x = m / n; // 0
// since arguments are integer, integer division is used = 0
// must coerce "int" values to floating point
// Two ways

// Efficient way: cast as a double
double x = (double) m / (double)n;

// Clumsy way: multiply by a float (ala Fortran)
double x = 1.0*m/n;
```

```java
// Many students wrote this in Fraction program
public class Fraction {
    int numerator;  // numerator of the fraction
    int denominator;    // denominator of the fraction

    // compare fraction to another
    public int compareTo (Fraction frac) {
        double r1 = this.numerator / this.denominator;
        double r2 = frac.numerator / frac.denominator;
        if(r1 > r2) return 1;
        else if (r1 == r2) return 0;
        else return -1;
    }
}
```

## Array Types
- An array is a homogeneous aggregate of data elements in which an individual element is identified by its position in the aggregate, relative to the first element

### Array Design Issues
- What types are legal for subscripts?
- Are subscripting expression in element references range checked?
- When are subscript ranges bound?
- When does allocation take place?
- Are ragged or rectangular multidimensional arrays allowed, or both?
- What is the maximum number of subscripts?
- Can array objects be initialized?
- Are any kind of slices supported?

### Arrays
- An array is a series of elements of the same type, with an index, which occupy consecutive memory locations.
    - float x[10]; // C: array of 10 "float" vars
    - char [] c = new char[40]; // Java: array of 40 "char"

### Array "dope vectors"
- In C or Fortran an array is just a set of continuous elements. No type or length information is stored.
- Some languages store a "dope vector" (aka array descriptor) describing the array
```c
// C
double x[10]; 
/*
x => 01E4820 => x[0], x[1]...
*/

// language with dope
double x[10];
/*
x => double, 0, 10, 01E4820 => x[0], x[1]...
*/
```

### Array as Object
- In Java, arrays are objects:
    ```java
    double [] x = new double[10];
    ```
    - x is an Object; x[10] is a double (primitive type)
    ```java
    x.getClass().toString() // returns "[D"
    ```

### Arrray Indexing
- Indexing (or subscripting) is a mapping from indices to elements
    - array_name(index_value_list) => an element
- Index Syntax
    - Fortran and Ada use parentheses
        - Ada explicitly uses parentheses to show uniformity between array references and function calls because both are *mappings*
    - Most other languages use brackets

### Arrays Index (Subscript) Types
- FORTRAN, C: integer only
- Ada: integer or enumeration (includes Boolean and char)
- Java: integer types only
- Index range checking
    - C, C++, Perl, and Fortran do not specify range checking
    - Java, ML, C# specify range checking
    - In Ada, the default is to require range checking, but it can be turned off

### Subscript Binding and Array Categories
- **Static Array**: an array whose size is known, and whose storage is allocated, at compile time. In C, you might write at global (file) scope:
    - static int static_array[7];
    - Advantage: efficiency (no dynamic allocation)
- **Fixed stack-dynamic array**: you know the size of your array at compile time, but allows it to be allocated automatically on the stack (the size is fixed at compile time but the storage is allocated when you enter its scopoe, and released when you leave it)
    - Advantage: space efficiency
        ```c
        void foo() {
            int fixed_stack_dynamic_array[7];
        }
        ```
- **Stack-dynamic**: subscript ranges are dynamically bound and the storage allocation is dynamic (done at run-time)
    - Advantage: flexibility (the size of an array need not be known until the array is to be used)
    - For example: you don't know the size until runtime, eg. C99 allows this:
        ```c
        void foo(int n) {
            int stack_dynamic_array[n];
        }
        ```
- **Fixed heap-dynamic**: similar to fixed stack-dynamic: storage binding is dynamic but fixed after allocation (i.e., binding is done when requested and storage is allocated from heap, not stack)
    ```c
    int * fixed_heap_dynamic_array = malloc (7 * sizeof(int));
    ```
    - using explicit heap allocation

- **Heap-dynamic**: binding of subscript ranges and storage allocation is dynamic and can change any number of times
    - Advantage: flexibility (arrays can grow and shrink during program execution)
    ```c
    void foo (int n) {
        int * heap_dynamic_array = malloc(n * sizeof(int));
    }
    ```

- C and C++ arrays that include static modifiers are static
- C and C++ arrays without static modifier are fixed stack-dynamic
- C and C++ provide fixed heap-dynamic arrays
- C# includes a second array class ArrayList that provides fixed heap-dynamic
- Perl, JS, Python and Ruby support heap-dynamic arrays

### Array Initialization
- Some language allow initialization at the time of storage allocation
- C, C++, Java, C# example
```c
int list [] = {4,5,7,83};

// char strings
char name[] = "freddie";

// array of strings
char *names[] = {"Bob", "Jake", "Joe"};
```

```java
// java
String[] names = {"Bob", "Jake", "Joe"};
```

### Heterogeneous Arrays
- A **heterogeneous array** is one in which the elements need not be of the same type
- Supported by Perl, Python, JS, Ruby
- Python example
```python
lst=[1,'one',{1:'one'},a,[1,1],(1,),True,set((1,))]
for each in lst:
    print type(each), str(each)

# <type 'int'> 1
# <type 'str'> one
# <type 'dict'> {1: 'one'}
# <type 'function'> <function a at 0x100496938>
# <type 'list'> [1, 1]
# <type 'tuple'> (1,)
# <type 'bool'> True
# <type 'set'> set([1]
```