#include <stdio.h>

int factorial(n) {
    if (n < 0) {
        return -1; /* don't do that! */
    }
    if (n <= 1) {
        return n;
    }
    return n * factorial(n-1);
}

int main(int argc, char *argv[]) {
    printf("Hello, world!\n");
    return 0;
}
