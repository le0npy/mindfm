# -*- coding: utf-8 -*-
__autor__ = 'le0npy'
__version__ = '1.0'

import shutil         #импорт модуля операции с файлами и папками
import os, sys, getopt, traceback            #imports the os
import os.path
from time import sleep
import colorama

colorama.init()
CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

print("The Python version is %s.%s.%s" % sys.version_info[:3])
#os.system("pause")
#sleep (1)

def Read():        #Чтение файлов
    import subprocess   
    print (CBEIGE + 70 * '*' + CEND)
    print (CVIOLET + 'Текущий каталог: ' + CEND + CGREEN + os.getcwd() + CEND)
    print (CBEIGE + 70 * '*' + CEND)
    subprocess.call(['ls', '-l'])
    print (CBEIGE + 70 * '*' + CEND)              
    path = input('Введите местоположение файла для чтения:')    
    try:		
        file = open(path,"r")
        print(file.read())
    except IOError:
        print("Нет такого файла")
        return
    else:
        input('Нажмите Enter...')   
    file.close()
    
if __name__ == "_main__":
   Read(sys.argv[1:])


def Write():    #Редактировать и создать файлы
    import subprocess
    import re
    print (CBEIGE + 70 * '*' + CEND)
    print (CVIOLET + 'Текущий каталог: ' + CEND + CGREEN + os.getcwd() + CEND)
    print (CBEIGE + 70 * '*' + CEND)
    subprocess.call(['ls', '-l'])
    print (CBEIGE + 70 * '*' + CEND) 
    path = input("Введите местоположение для создания файла или записи:")
    if os.path.isfile(path):
        print('Изменить существующий файл') #Существующий файл
    else:
        while True:
           print('Нет такого файла, cоздать новый? [Y/n]: ') #Новый файл
           response = input()          
           if response == "Y" or response == "y":
              text = input("Ввести текст для записи:")
              file = open(path,"w")
              file.write(text)
              file.close()
              return False
           elif response == "N" or response == "n":
              return True                          
           else:
              print("ВВедено некорректное значение: {}".format(response))


def Add():      #Редактирование текста
    print(CVIOLET + 'Текущий каталог:' + CEND)
    print(CGREEN + os.getcwd() + CEND)
    path=input("Введите местоположение файла:")
    text=input("Введите текст для записи:")
    file=open(path,"a")
    file.write('\n'+text)


def Delete():          #Удалить файл
    print(CVIOLET + 'Текущий каталог:' + CEND)
    print(CGREEN + os.getcwd() + CEND)
    path=input("Введите местоположение файла:")
    if os.path.exists(path):      # проверка существавания файла
        print('Файл не найден')     #Для несуществующего файла
        os.remove(path)          #os.remove(file path) is used to delete
        print('Файл удален')
    else:
        print('File Does\'nt exist')    #Файл не существует



def Dirlist():      #Списсок файлов в каталоге
    print(CVIOLET + 'Текущий каталог:' + CEND)
    print(CGREEN + os.getcwd() + CEND)
    path=input("Введите расположение каталога:")
    sortlist=sorted(os.listdir(path))       #Сортировка и листинг файлов
    i=0
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1


def Check():       #Проверка наличия файлов или каталога
    fp=int(input('Check the presence of \n1.File \n2.Directry \n'))
    if fp==1:
        path=input("Enter the file location:")
        os.path.isfile(path)
        if os.path.isfile(path)==True:
            print('File Found')
        else:
            print('File not Found')
    if fp==2:
        path=input("Enter the Directory location:")
        os.path.isdir(path)
        if os.path.isdir(path)==False:
            print('Directory Found')
        else:
            print('Directory Not Found')



def Move():        #For moving or renameing file
    path1=input('Enter the location of File to move or rename:')
    mr=int(input('1.Rename \n2.Move \n'))
    if mr==1:
        path2=input('Enter the resulting location with resulting file name:')
        shutil.move(path1,path2)
        print('File renamed')
    if mr==2:
        path2=input('Enter the location to move:')
        shutil.move(path1,path2)
        print('File moved')


def Copy():       #For copying
    print(CVIOLET + 'Текущий каталог:' + CEND)
    print(CGREEN + os.getcwd() + CEND)
    path1=input('Enter the location of File to copy or rename:')
    path2=input('Enter the location to copy:')
    shutil.copy(path1,path2)
    print('File copied')


def Makedir():            #For creating directory
    print(CVIOLET + 'Текущий каталог:' + CEND)
    print(CGREEN + os.getcwd() + CEND)
    path=input("Enter the directory name with location to make \neg. /newDir \nWhere newdir is new directory:")
    os.makedirs(path) 
    print('Directory Created')


def Removedir():             #For removing Directory
    print(CVIOLET + 'Текущий каталог:' + CEND)
    print(CGREEN + os.getcwd() + CEND)
    path=input('Enter the location of Directory:')
    treedir=int(input('1.Deleted Directory \n2.Delete Directory Tree \n3.Exit \n'))
    if treedir==1:
        os.rmdir(path)
    if treedir==2:
        shutil.rmtree(path)
        print('Directory Deleted')
    if treedir==3:
        exit()


def Openfile():
    print(CVIOLET + 'Текущий каталог:' + CEND)
    print(CGREEN + os.getcwd() + CEND)
    path=input('Enter the location of Program:')
    try:
        os.startfile(path)
    except:
        print('File not found')


run=1
while(run==1):     #Running the program again
    os.system('cls')        #Used to clear the screen after running again the program
    print (CBEIGE + 20 * '*' + CEND)
    print(CGREEN +'Менеджер Файлов' + CEND + CRED + ' Mind' + CEND)
    print (CBEIGE + 20 * '*' + CEND)
    dec=int(input('''
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
'''))
    if dec==1:
        Read()
    if dec==2:
        Write()
    if dec==3:
        Add()
    if dec==4:
        Delete()
    if dec==5:
        Dirlist()
    if dec==6:
        Check()
    if dec==7:
        Move()
    if dec==8:
        Copy()
    if dec==9:
        Makedir()
    if dec==10:
        Removedir()
    if dec==11:
        Openfile()
    if dec==12:
        exit()
    run=int(input("1.Меню  \n2.Выход \nВыберите номер опции: \n"))
    if run==2:
        exit()

