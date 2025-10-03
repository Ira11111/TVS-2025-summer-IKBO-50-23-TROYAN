#!/bin/bash

set -e  # Выход при ошибках

echo "🧪 Запуск модульных тестов..."

# Создаем директории для отчетов
mkdir -p /app/reports/unit
mkdir -p /app/reports/mut

# Запускаем тесты с coverage
python -m pytest tests/ -v --cov=figure --cov-report=html:/app/reports/unit

echo "✅ Модульные тесты завершены"

echo "🧬 Запуск мутационных тестов..."

# Запускаем мутационные тесты
mut.py --target figure --unit-test tests --runner pytest --report-html /app/reports/mut

echo "🎉 Все задачи выполнены!"