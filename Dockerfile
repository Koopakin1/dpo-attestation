FROM python:3.11-slim
WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копирование зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Создание директорий для данных
RUN mkdir -p /app/diplomas /app/logs

# Установка прав доступа
# (команда была удалена, так как в директории нет исполняемого файла dpo_attestation)

# Установка переменных окружения по умолчанию
ENV PYTHONPATH=/app
ENV DATABASE_URL=postgresql+asyncpg://dpo_user:password@db:5432/dpo_attestation
ENV FSM_DB_PATH=/app/fsm_storage.db
ENV DIPLOMAS_PATH=/app/diplomas
ENV LOGS_PATH=/app/logs

# Запуск приложения
CMD ["python", "-m", "src.partner_bot"]