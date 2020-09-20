# HTML-библиотека

Это HTML-библиотека книг жанра "Научная фантастика". Работает оффлайн, если скачать весь репозиторий.
Посмотреть, как работает можно [здесь](https://kvrasuli.github.io/dvmn_online_library/).

![](https://i.imgur.com/tlU81cP.png)
## Как использовать
- Вариант 1 - скачать репозиторий и открыть в браузере файл index.html
- Вариант 2 - установить зависимости
    ```
    pip3 install -r requirements.txt
    ```
    затем запустить скрипт server.py
    ```
    python3 server.py
    ```
    и открыть в браузере страницу  http://127.0.0.1:5500

## Как обновить библиотеку книг
- Открыть [этот](https://github.com/kvrasuli/dvmn_tululu_parser) репозиторий.
- Скачать книги и json файл по инструкции
- Поместить скачанное (папку books и файл books.json) в корень сайта
- Запустить скрипт render_website.py
    ```
    python3 render_website.py
    ```

### Это учебный проект
[dvmn.org](https://dvmn.org)
