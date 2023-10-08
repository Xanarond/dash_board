# Используем официальный образ Python
FROM miigotu/python3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости проекта (в данном случае, requirements.txt) в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущей директории (где находится Dockerfile) в контейнер
COPY . /app/

# Определяем порт, на котором будет работать приложение
EXPOSE 8050

# Команда для запуска приложения Dash
CMD ["python", "app.py"]