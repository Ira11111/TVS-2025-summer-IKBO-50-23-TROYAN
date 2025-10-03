/** @type {import('@stryker-mutator/api/core').PartialStrykerOptions} */
module.exports = {
  // Пакетный менеджер
  packageManager: 'npm',

  // Репортеры для вывода результатов
  reporters: ['html', 'clear-text', 'progress'],

  // Test runner для запуска тестов
  testRunner: 'jest',

  // Анализ покрытия
  coverageAnalysis: 'perTest',

  mutate: [
      './src/calculator.js'
  ],
  // Конфигурация Jest
  jest: {
    config: {
      testEnvironment: 'node',
      testMatch: ['*.test.js']  // где искать тесты
    }
  },

  // Пороги для мутационного тестирования
  thresholds: {
    high: 80,    // отличный результат
    low: 60,     // минимально приемлемый
    break: 50    // ниже - провал
  },

  // Временные файлы
  tempDirName: '.stryker-tmp'
};