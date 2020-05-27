## Dashboard for ClickHouse Revision Performance Comparison and Analysis Interface

Данный дашборд содержит 5 разделов - Dashboard (Графики и диаграммы),
Tables (Таблицы с результатами тестирования), All Queries (Все SQL запросы из тестов), 
Logs (Логи работы), Download (Ссылка на скачивания архива со всеми файлами результатов тестирования)

### Превью

Посмотреть, как выглядит интерфейс можно, скачав архив preview.zip, 
разархивировав его и открыв файл index.html. 

### Запуск

Запуск генерации производится 2 способами. 

- Напрямую (с текущими данными с результатами тестировани в папке 
clickhouse-testing-interface/static/test_data): 
из папки clickhouse-testing-interface запустить следующий скрипт

    ``` 
    # install dependencies
    $ npm install
    
    # generate static project
    $ npm run generate
    ```

- Через sh файл (рекомендуется): Запустить из корневой папка файл run.sh:

    ``` 
    $ ./run.sh
    ```
   
Файл запустит генерацию json с результатами тестирования (из папки /test_data). 
После генерации файлов запустится генерация бандла со всеми статичными файлами и 
после окончания сборки статичная страница автоматически откроется в браузере, 
установленном как браузер по умолчанию на устройстве.

### Функционал - Графики

При наведении на части графиков и диаграмм, показывается дополнительная информация.
Некоторые графики имеют меню с настройками (расположены над графиком), которые можно изменять. 

### Функционал - Таблицы

##### Сортировка

При клике на заголовок столбца он сортируется сначала в порядке убывания значений,
если столбец содержит числа, в лексикографическом порядке, если это строка, 
и в порядке убывания элементов, начиная с первого, если это массив. 
При повторном клике на заголовок происходит так же сортировка, но уже в обратном порядке. 

##### Скрытие таблиц

При нажатии специального значка справа от названия таблицы таблица скрывается, 
при повторном нажатии вновь показывается.
 
### Скриншоты 

<img src="https://github.com/DariaHighfly/clickhouse-testing-interface/blob/master/img/clickhouse_img_1.png" width="100%" height="100%">
<img src="https://github.com/DariaHighfly/clickhouse-testing-interface/blob/master/img/clickhouse_img_2.png" width="100%" height="100%">
<img src="https://github.com/DariaHighfly/clickhouse-testing-interface/blob/master/img/clickhouse_img_3.png" width="100%" height="100%">
<img src="https://github.com/DariaHighfly/clickhouse-testing-interface/blob/master/img/clickhouse_img_4.png" width="100%" height="100%">
<img src="https://github.com/DariaHighfly/clickhouse-testing-interface/blob/master/img/clickhouse_img_5.png" width="100%" height="100%">
<img src="https://github.com/DariaHighfly/clickhouse-testing-interface/blob/master/img/clickhouse_img_6.png" width="100%" height="100%">


