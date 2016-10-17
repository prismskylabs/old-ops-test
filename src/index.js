#!/usr/bin/env node
'use strict';

function factorial(n) {
    if (n < 0) {
        throw "Can't calculate factorial of negative number";
    }
    if (n <= 1) {
        return n;
    }
    return (n * factorial(n-1));
}

(function main() {
    console.log('Hello, world!');
})();
