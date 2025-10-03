FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install pytest mutpy pytest-cov

# Устанавливаем нашу библиотеку в режиме разработки
RUN pip install -e .

# Создаем директорию для отчетов (на всякий случай)
RUN mkdir -p /app/reports

RUN chmod +x test_script.sh

# Запускаем тестовый скрипт
CMD ["./test_script.sh"]