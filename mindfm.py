#!/usr/bin/env python3
"""Данное ПО разработано для подтверждения практических навыков по практике

"""


import argparse
import os
import sys
import shutil

# размер терминала для вывода в формате таблицы
terminalColumnSize, terminalRowSize = shutil.get_terminal_size()

parser = argparse.ArgumentParser(description=
"""args spec program command comment.

""")

outputFormat = parser.add_mutually_exclusive_group();
outputFormat.add_argument("-t",action="store_true",
help="вывод в формате таблицы; функция по умолчанию")
outputFormat.add_argument("-1", dest="one", action="store_true",
help="вывод в одноколоночном формате")
outputFormat.add_argument('-x','--xargs', action="store_true",
help="""вывод будет состоять из строки с нулевыми именами файлов, с сортировкой по горизонтали;
которые можно использовать в качестве входных данных для других команд;""")

group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-n", "--non-hidden", action='store_true', dest="non_hidden",
help="""показать файлы и/или каталоги с именами,
не начинающиеся с точки;""")
group1.add_argument("-i", "--hidden", action='store_true',
help="показать файлы и каталоги с именами, начинающимися с точки")
group1.add_argument("-a", "--include-hidden", action='store_true', dest="include_hidden",
help="показать все файлы и каталоги")

group1.add_argument("-s", "--search", action="store_true", dest="search",
help="Поиск файлов в заданном каталоге;")
group1.add_argument("-r", "--read", action="store_true", dest="read",
help="Чтение фала; !!!Данный функционал в разработке")
group1.add_argument("-c", "--copy", action="store_true", dest="copy",
help="Копирование файла; !!!Данный функционал в разработке")
group1.add_argument("-del", "--delete", action="store_true", dest="delete",
help="Удаление файла; !!!Данный функционал в разработке")

group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-d", "--only-dir", action="store_true", dest="only_dir",
help="Показать только каталоги")
group2.add_argument("-f", "--only-files", action="store_true", dest="only_files",
help="Показать только файлы")

parser.add_argument("files", metavar="FILE", nargs='*',
help="""Список разделенные проблеами файлов или каталогов;
если не задано, будет использован текущий каталог""")

parser.add_argument("-v", "--version",
help="Вывести Версию программы и Справку", action="store_true")

args = parser.parse_args()

# non-hidden is default option
if not args.non_hidden and not args.hidden and not args.include_hidden:
    args.non_hidden = True


"""function declarations STARTS"""

def version():
    """показать версию, Лицензию и выйти"""
    if args.version:
        print(
"""mindfm version 1.0.2b

Copyright (c) 2017 r00t (Skype:shafirov4911)
**********************************************************************************************
Этот проект явялется бесплатным программным обеспечением, выпущенным под лицензией MIT / X11:*
**********************************************************************************************
Разрешение предоставляется бесплатно любому лицу, получившему копию                          *
этого программного обеспечения и связанных файлов документации к этому                       *
программному обеспечению, чтобы обеспечить без ограничений, включая права:                   *
Использовать, Копировать, Изменять, Объединять, Публиковать, Распространять,                 *
Сублицензировать и / или продавать копии этого Программного беспечения.                      *
                                                                                             *
ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ВЫРАЖЕННЫХ ИЛИ  *
ПОДРАЗУМЕВАЕМЫЕ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ ​​ГАРАНТИЯМИ КОММЕРЧЕСКОЙ ЦЕННОСТИ.              *
АВТОР ИЛИ АВТОРСКИЕ ПРАВА НЕ НЕСУТ ОТВЕТСТВЕННОСТИ ЗА ЛЮБЫЕ ПРЕТЕНЗИИ, УБЫТКИ ИЛИ ДРУГУЮ     *
ОТВЕТСТВЕННОСТЬ, КАК В ДЕЙСТВИИ КОНТРАКТА, ТАК И ДЕЙСТВИЯ ИНОГО ХАРАКТЕРА,                   *
СВЯЗАННЫЕ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ЕГО ИСПОЛЬЗОВАНИЕМ...                               *
**********************************************************************************************
""")
        sys.exit(0)
                  	

def createFileList(dirname):
    """вывести список файлов в указанном каталоге на основе различных опций"""
    files = []
    dirs = []
    all_files = os.listdir(dirname)
    print(90 * "*")

    if args.non_hidden:
        files = [file for file in all_files if not os.path.isdir(dirname + "/" + file) and file[0] != '.' ]
        dirs = [file+"/" for file in all_files if os.path.isdir(dirname + "/" + file) and file[0] != '.' ]
    elif args.hidden:
        files = [file for file in all_files if not os.path.isdir(dirname + "/" + file) and file[0] == '.' ]
        dirs = [file+"/" for file in all_files if os.path.isdir(dirname + "/" + file) and file[0] == '.' ]
    else:
        files = [file for file in all_files if not os.path.isdir(dirname + "/" + file)]
        dirs = [file+"/" for file in all_files if os.path.isdir(dirname + "/" + file)]
    if args.only_files:
        return files
    elif args.only_dir:
        return dirs
    else:
        return files + dirs
    if args.search(file_name):
        command = ['locate', file_name]
        output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
        output = output.decode()
        search_results = output.split('\n')
        return search_results

def read():
    print("Извините, функция чтения находится в разработке")

def copy():
    print("Извините, функция копирования находится в разработке")

def delete():
    print("Извините, функция удаление находится в разработке")

def xargsInput():
    """создать строку нулевых имен файлов для обработки командой xargs"""
    outputString = ""
    for file in args.files:
        if not os.path.isdir(file):
            outputString += file + "\0"
        else:
            for inode in createFileList(file):
                outputString += file + "/" + inode + "\0"
    return outputString


def columnOutput(printFunc):
    """функция, когда запрошенный вывод является таблицей или одним файлом в строке.
    Обратите внимание на использование printFunc; он заменяет функцию prettyPrint для вывода в виде таблиц,
     или oneFilePerLine для вывода одного файла на строку."""
    global didErrorOccur
    moreThanOneArg = 0
    for file in args.files:
        """продолжайте обрабатывать следующий файл в списке файлов, даже если возникает ошибка.
        если возникла ошибка, распечатайте ошибку и обработайте следующий файл в списке файлов.
        didErrorOccur используется как флаг, возникает ли ошибка или нет"""
        try:
            if not os.path.exists(file):
                raise FileNotFoundError("{}: cannot access '{}': no such file or directory".format(os.path.basename(sys.argv[0]), file))
            elif not os.path.isdir(file):
                if moreThanOneArg: print()
                print(file)
            else:
                if moreThanOneArg: print()
                if len(args.files) > 1:
                    print(file, ":", sep="")
                printFunc(createFileList(file))
        except FileNotFoundError as err:
            if moreThanOneArg: print()
            print(err)
            didErrorOccur = 1
        except PermissionError:
            if moreThanOneArg: print()
            print("{}: cannot open directory '{}': Permission denied".format(os.path.basename(sys.argv[0]), file))
            didErrorOccur = 1
        finally:
            moreThanOneArg = 1


def oneFilePerLine(list):
#    for l in list: #альтернатива для win2k
#        print(l)
    import subprocess
    p1 = 'ls'
    p2 = '-la'
    for l in list:
        subprocess.call([p1, p2, l])
    print(70 * "*")

def prettyPrint(list):
    """print files in table format"""
    maxlen = 0
    for f in list:
        if len(f) > maxlen:
            maxlen = len(f)
    # 2 для включения одинарных кавычек, 2 для пробелов после имени файла
    colWidth = maxlen + 4
    noOfCol = int(int(terminalColumnSize)/colWidth)
    if noOfCol == 0 or noOfCol == 1:
        for f in list:
            print("{!r}".format(f))
    else:
        nthCol=0
        for f in list:
            nthCol += 1
            print('{!r}'.format(f).ljust(colWidth), end="")
            if nthCol == noOfCol:
                print()
                nthCol=0
        if nthCol != noOfCol and nthCol != 0:
            print()


def main():
    global didErrorOccur
    version()
    if not len(args.files):
        """если аргумент не указан, предположим, что он является текущим каталогом"""
        args.files = ['.']
    if args.xargs:
        """если задано значение -x или --xargs, строка вывода имен файлов с нулевым завершением"""
        try:
            print(xargsInput(), end="")
            sys.exit(0)
        except FileNotFoundError as err:
            print(err)
            sys.exit(2)
        except PermissionError as err:
            print(err)
            sys.exit(2)
    elif args.read:
       read()
    elif args.copy:
       copy()
    elif args.delete:
       delete()
    elif args.one:
        """выводить один файл на строку"""
        columnOutput(oneFilePerLine)
        pass
    else:
        """имена выходных файлов в формате таблицы"""
        columnOutput(prettyPrint)
        """Версия правил. Для Python > версии 3.0"""
    if float(sys.version[0:3]) < 3.0:
        print("Этот скрипт требует версии Python 3.0 или выше.")
        print("Установлена версия Python %s" % sys.version)
        return 0


if __name__ == "__main__":
    didErrorOccur = 0 # используется как флаг, возникает ли ошибка или нет
    main()
    if didErrorOccur:
        sys.exit(2)
    else:
        sys.exit(0)
