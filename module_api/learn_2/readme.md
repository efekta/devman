## Обрезка ссылок с помощью Битли
#### main.py  
Модуль взаимодействует с API сервисa [bitly.com](https://app.bitly.com/) : </br>
Считывает пользовательский ввод,
если была введена короткая ссылка, то будет
выведено колличество кликов по датам в консоль.  

Если была введена обычная ссылка,
то программа сделает из нее короткую ссылку
и выведет ее в консоль.

Если пользователь ввел ссылку некорректно,
программа сообщит об этом в консоли.

#### функция main
Запускает всю программу.

#### функция shorten_link
Делает из обычной ссылки короткую.

#### функция count_clicks
Получает информацию о колличестве кликов 
по введенной ссылке.

#### функция is_bitlink
Проверяет была введена короткая ссылка или нет.

## Как установить
Создайте файл .env для хранений ключей
Зарегистрируййтесь на [bitly.com](https://app.bitly.com/) 
и получите токен для взаимодействия с сервисом.
Сохраните свой токен в переменной BITLINK_TOKEN в файле .env
Python3 должен быть уже установлен. 
Затем используйте pip (или pip3, есть конфликт с Python2) 
для установки зависимостей:
```
pip install -r requirements.txt
```

## Как запустить
```
python3 main.py тут должна быть введена ссылка
```
## Цель проекта
Код написан в образовательных целях на онлайн-курсе 
для веб-разработчиков dvmn.org.
