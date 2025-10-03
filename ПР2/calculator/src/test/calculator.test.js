const Calculator = require('../calculator');

describe('Calculator', () => {
    let calculator;

    beforeEach(() => {
        calculator = new Calculator();
    });

    describe('add', () => {
        test('должен корректно складывать два положительных числа', () => {
            expect(calculator.add(2, 3)).toBe(5);
        });

        test('должен корректно складывать отрицательные числа', () => {
            expect(calculator.add(-2, -3)).toBe(-5);
        });

        test('должен корректно складывать положительное и отрицательное число', () => {
            expect(calculator.add(5, -3)).toBe(2);
        });

        test('должен выбрасывать ошибку при нечисловых аргументах', () => {
            expect(() => calculator.add('2', 3)).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add('2', false)).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add(2, '3')).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add(null, 3)).toThrow('Оба аргумента должны быть числами');
        });
    });

    describe('subtract', () => {
        test('должен корректно вычитать числа', () => {
            expect(calculator.subtract(5, 3)).toBe(2);
        });

        test('должен корректно работать с отрицательными числами', () => {
            expect(calculator.subtract(2, 5)).toBe(-3);
        });

        test('должен выбрасывать ошибку при нечисловых аргументах', () => {
            expect(() => calculator.subtract('5', 3)).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add('2', false)).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add(5, 'u')).toThrow('Оба аргумента должны быть числами');
        });
    });

    describe('multiply', () => {
        test('должен корректно умножать числа', () => {
            expect(calculator.multiply(4, 5)).toBe(20);
        });

        test('должен корректно умножать на ноль', () => {
            expect(calculator.multiply(4, 0)).toBe(0);
        });

        test('должен выбрасывать ошибку при нечисловых аргументах', () => {
            expect(() => calculator.multiply('4', 5)).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add(2, false)).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add('9', false)).toThrow('Оба аргумента должны быть числами');
        });
    });

    describe('divide', () => {
        test('должен корректно делить числа', () => {
            expect(calculator.divide(10, 2)).toBe(5);
        });

        test('должен корректно делить дробные числа', () => {
            expect(calculator.divide(1, 4)).toBe(0.25);
        });

        test('должен выбрасывать ошибку при делении на ноль', () => {
            expect(() => calculator.divide(10, 0)).toThrow('Деление на ноль невозможно');
        });

        test('должен выбрасывать ошибку при нечисловых аргументах', () => {
            expect(() => calculator.divide('10', 2)).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add(8, false)).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add('l', false)).toThrow('Оба аргумента должны быть числами');
        });
    });

    describe('power', () => {
        test('должен корректно возводить в степень', () => {
            expect(calculator.power(2, 3)).toBe(8);
        });

        test('должен корректно работать с нулевой степенью', () => {
            expect(calculator.power(5, 0)).toBe(1);
        });

        test('должен корректно работать с отрицательной степенью', () => {
            expect(calculator.power(2, -1)).toBe(0.5);
        });

        test('должен выбрасывать ошибку при нечисловых аргументах', () => {
            expect(() => calculator.power('2', 3)).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add(9, false)).toThrow('Оба аргумента должны быть числами');
            expect(() => calculator.add('d', false)).toThrow('Оба аргумента должны быть числами');
        });
    });

    describe('factorial', () => {
        test('должен корректно вычислять факториал 0', () => {
            expect(calculator.factorial(0)).toBe(1);
        });

        test('должен корректно вычислять факториал 1', () => {
            expect(calculator.factorial(1)).toBe(1);
        });

        test('должен корректно вычислять факториал 5', () => {
            expect(calculator.factorial(5)).toBe(120);
        });

        test('должен выбрасывать ошибку для отрицательных чисел', () => {
            expect(() => calculator.factorial(-1)).toThrow('Факториал определен только для неотрицательных чисел');
        });

        test('должен выбрасывать ошибку для нецелых чисел', () => {
            expect(() => calculator.factorial(2.5)).toThrow('Факториал определен только для целых чисел');
        });

        test('должен выбрасывать ошибку при нечисловом аргументе', () => {
            expect(() => calculator.factorial('5')).toThrow('Аргумент должен быть числом');
            expect(() => calculator.factorial(false)).toThrow('Аргумент должен быть числом');
        });
    });
});