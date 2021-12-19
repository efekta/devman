## Космический Телеграм
Программа ежедневно постит по 1 фотографии космоса в 
телеграм канал [@uploadphotos](https://t.me/uploadphotos).

### Как установить
1. Python3 должен быть уже установлен. 

2. Затем используйте pip (или pip3, есть есть конфликт с Python2) 
для установки зависимостей:

    ```
    pip install -r requirements.txt
    ```

3. Создайте файл .env для хранений ключей.

- Для ключа NASA_TOKEN зарегистрируйтесь 
на сайте [https://api.nasa.gov/ ](https://api.nasa.gov/)
и вставьте ключ в переменную NASA_TOKEN.

- Для ключа TG_TOKEN создайте бота телеграмм 
с помощью [@botfather](https://t.me/botfather)
и вставьте ключ в переменную TG_TOKEN.


- Что бы узнать свой ключ TG_CHAT_ID, используйте команды в консоли:
    ```
    bot = telegram.Bot(token=f'{tg_token}')
    update = bot.get_updates()
    chat_id = bot.get_updates()[-1].message.chat_id
    ```
    и вставьте полученный ключ chat_id в переменную TG_CHAT_ID.


- Для ключа CHANEL_ID используйте имя своего телеграм бота,
вставив его в переменную CHANEL_ID

### Как запустить
Ввести в терминале команду, где вместо @name_your_bot должно быть 
имя Вашего бота или ссылка https://t.me/name_your_bot:
```
python3 main.py @name_your_bot
```

или
```
python3 main.py https://t.me/name_your_bot:
```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе
для веб-разработчиков dvmn.org.