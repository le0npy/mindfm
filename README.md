# mindfm
 Этот репозитарий содержит консольную утилиту на Python3, предназначеный для работы с файлами и каталогами.
 # Информация
 Скрип задумывался как универсальный инструмент управления файлами и каталогами стремящийся к кроссплатформенности.
 Скрип тестировался на Python3 и ОС: Debian, Windows*, Mac OS* (* часть функций поддерживается на Linux)
 
 *_Часть_ _функций_ _находится_ _в_ _разработке_
 
 *Опции: -1, -s не совместимы с win2k
 # Зависимости
 Этот скрипт имеет зависимости
 * os
 * sys
 * argparse
 * shutil
 * subprocess
 ```python
 +pip install shutil
 ```
 +# Применение
 ```
 +mindfm.py
 Применение:
 mindfm.py <dir> -a >> C:\Python\log.txt
 mindfm.py -s /var/log/*.log 
 
 +Опции:
   -h, --help            Вывод Справки;
   -t                    вывод в формате таблицы; функция по умолчанию;
   -1                    вывод в одноколоночном формате;
   -x, --xargs           вывод будет состоять из строки с нулевыми именами;
                         файлов, с сортировкой по горизонтали; которые можно
                         использовать в качестве входных данных для других
                         команд;
   -n, --non-hidden      показать файлы и/или каталоги с именами, не
                         начинающиеся с точки;
   -i, --hidden          показать файлы и каталоги с именами, начинающимися с
                         точки;
   -a, --include-hidden  показать все файлы и каталоги;
   -s, --search          Поиск файлов в заданном каталоге;
   -r, --read            Чтение фала; !!!Данный функционал в разработке;
   -c, --copy            Копирование файла; !!!Данный функционал в разработке;
   -del, --delete        Удаление файла; !!!Данный функционал в разработке;
   -d, --only-dir        Показать только каталоги;
   -f, --only-files      Показать только файлы;
   -v, --version         Вывести Версию программы и лицензию;
 ```

 # guifm
Этот репозитарий содержит консольную GUI утилиту на Python3, предназначеный для работы с файлами и каталогами.
# Информация
Скрип задумывался как универсальный инструмент управления файлами и каталогами

Скрип тестировался на Python3 и ОС: Debian, Windows, Mac OS

# Зависимости
Этот скрипт имеет зависимости
* os, path
* sys, sys, getopt, traceback
* shutil
* colorama
```python
pip install colorama
```
# Применение
```
********************
Менеджер Файлов GUIFM
********************

1.Чтение файла
2.Редактироване файла
3.Добавить текст в файл
4.Удалить файл
5.Список файлов в каталоге
6.Проверить наличие файла
7.Переместить файл
8.Скопировать файл
9.Создать каталог
10.Удалить каталог
11.Открыть программу
12.Выйти

Выберите номер опции:
5
Текущий каталог:
C:\Python\Python36
Введите расположение каталога:\
```
# Лицензия
Это программное обеспечение лицензировано MIT.
