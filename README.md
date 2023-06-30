# Telegram-translator-bot

- [About](#About)
- [Installation](#Installation)
  * [Before Installation](#Before-Installation)   
  * [Local](#Local-Installation)
  * [Docker](#Docker-Installation)

## About
This bot is a convenient tool for translating text from English to Russian. 

It uses the DeepL API, which ensures high-quality and accurate translation. Simply send it a message in English, and the bot will instantly provide you with the translation in Russian. 

By utilizing the powerful and reliable DeepL service, you can trust the quality of the translation, making it easy for you to understand foreign text or communicate with English speakers.

## Installation

### Before Installation
You need to set your env variables in .env file

### Local Installation

0. **in database/database.py, set mongo url to local url**

1. Install Poetry, if you didn't.
``` 
pip install poetry
```
2. Go to folder where pyproject.toml and install dependencies.
``` 
poetry install
```
3. Activate poetry env.
``` 
poetry shell
```
4. Start your bot.
```
python main.py
```

### Docker Installation

You need to be there where dockerfile and docker-compose.yml

#### Start your bot
```
docker compose up --build
```
