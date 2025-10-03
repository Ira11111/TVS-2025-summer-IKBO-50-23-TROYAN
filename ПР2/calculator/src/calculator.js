class Calculator {
    add(a, b) {
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Оба аргумента должны быть числами');
        }

        return a + b;
    }

    subtract(a, b) {
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Оба аргумента должны быть числами');
        }
        return a - b;
    }

    multiply(a, b) {
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Оба аргумента должны быть числами');
        }
        return a * b;
    }

    divide(a, b) {
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Оба аргумента должны быть числами');
        }
        if (b === 0) {
            throw new Error('Деление на ноль невозможно');
        }
        return a / b;
    }

    power(base, exponent) {
        if (typeof base !== 'number' || typeof exponent !== 'number') {
            throw new Error('Оба аргумента должны быть числами');
        }
        return Math.pow(base, exponent);
    }

    factorial(n) {
        if (typeof n !== 'number') {
            throw new Error('Аргумент должен быть числом');
        }
        if (n < 0) {
            throw new Error('Факториал определен только для неотрицательных чисел');
        }
        if (!Number.isInteger(n)) {
            throw new Error('Факториал определен только для целых чисел');
        }

        if (n === 0 || n === 1) {
            return 1;
        }

        let result = 1;
        for (let i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}

module.exports = Calculator;