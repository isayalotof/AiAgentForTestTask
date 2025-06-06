# AI Agent for Test Task

Проект представляет собой простого AI-ассистента, построенного на базе LangChain и LangGraph, с возможностью отвечать на вопросы пользователя и предоставлять текущее время.

## Особенности

- Использует OpenAI GPT-4 (через LangChain)
- Имеет инструмент для получения текущего времени UTC
- Реализован как граф состояний с помощью LangGraph
- Поддерживает диалоговое взаимодействие

## Требования

- Python 3.8+
- Учетная запись OpenAI с API-ключом

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/isayalotof/AiAgentForTestTask.git
   cd AiAgentForTestTask
   ```

2. Создание виртуального окружения 
    ```
    python -m venv .venv 
    ```
3. Активация окружения
    для Windows
    ```
    .venv/Scripts/activate
    ```

    для linux
    ```
    source .venv/bin/activate
    ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` и добавьте ваш API-ключ OpenAI:
   ```
   OPENAI_API_KEY=ваш_ключ
   ```

## Использование

Запустите приложение:
```bash
langgraph dev
```

