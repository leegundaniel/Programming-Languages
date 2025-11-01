#include <iostream>
#include <chrono>
using namespace std;
using namespace chrono;

// function to declare large array statically
void staticArray() {
    // initialize static array, size 10,000
    static int arr[10000] = {0};
}

// function to declare large array on the stack
void stackArray() {
    // initialize stack array, size 10,000
    int arr[10000] = {0};
}

// function to declare large array on the heap
void heapArray() {
    // initialize heap array, size 10,000
    int* arr = new int[10000]();

    // Deallocate memory
    delete[] arr;
}

// run specified function 100,000 times and measure time taken
void measureTime(void (*func)(), const string& funcName) {
    auto start = high_resolution_clock::now();

    for (int i = 0; i < 100000; ++i) {
        func();
    }

    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start).count();

    cout << funcName << " Time: " << duration << " ms" << endl;
}

int main() {
    measureTime(staticArray, "Static Array");
    measureTime(stackArray, "Stack Array");
    measureTime(heapArray, "Heap Array");

    return 0;
}