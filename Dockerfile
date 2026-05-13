FROM python:3.11-bookworm

ENV DEBIAN_FRONTEND=noninteractive

# Устанавливаем системные зависимости:
# - Firefox
# - Java (для Allure)
# - утилиты для работы с репозиториями и сертификатами
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    firefox-esr \
    default-jdk \
    && rm -rf /var/lib/apt/lists/*

# Chrome: на amd64 — из репозитория Google; на arm64 пакета нет, ставим Chromium из Debian
RUN set -eux; \
    arch="$(dpkg --print-architecture)"; \
    if [ "$arch" = "amd64" ]; then \
        mkdir -p /etc/apt/keyrings \
        && wget -qO /etc/apt/keyrings/google.asc https://dl.google.com/linux/linux_signing_key.pub \
        && echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google.asc] https://dl.google.com/linux/chrome/deb/ stable main" \
            > /etc/apt/sources.list.d/google.list \
        && apt-get update \
        && apt-get install -y --no-install-recommends google-chrome-stable \
        && rm -rf /var/lib/apt/lists/*; \
    elif [ "$arch" = "arm64" ]; then \
        apt-get update \
        && apt-get install -y --no-install-recommends chromium \
        && rm -rf /var/lib/apt/lists/* \
        && ln -sf /usr/bin/chromium /usr/bin/google-chrome-stable; \
    else \
        echo "Unsupported architecture for Chrome/Chromium: $arch" >&2; \
        exit 1; \
    fi

# Скачиваем и устанавливаем Allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.32.0/allure-2.32.0.tgz \
    && tar -zxvf allure-2.32.0.tgz -C /opt/ \
    && ln -sf /opt/allure-2.32.0/bin/allure /usr/bin/allure \
    && rm allure-2.32.0.tgz

# Версия Poetry (менеджер зависимостей Python)
ENV POETRY_VERSION=2.3.4

# Директория установки Poetry
ENV POETRY_HOME=/opt/poetry

# Добавление Poetry и user-local bin в PATH,
# чтобы команда `poetry` была доступна глобально
ENV PATH="$POETRY_HOME/bin:/root/.local/bin:$PATH"

# Установка Poetry через официальный install-скрипт
# (ставится в POETRY_HOME; wget уже установлен выше, curl в образе нет)
RUN wget -qO- https://install.python-poetry.org | python3 -

# Отключаем создание виртуального окружения внутри проекта
# (Poetry будет использовать глобальное окружение контейнера)
RUN poetry config virtualenvs.create false

# Устанавливаем рабочую директорию
WORKDIR /usr/workspace

# Копируем файлы Poetry
COPY pyproject.toml poetry.lock* ./

# Установка зависимостей через Poetry
# requirements.txt больше не используется
RUN poetry install --no-interaction --no-ansi