import Unit_Interfase as ui
import Function as f
import os
import time

def run():
    input_from_user = ''
    while input_from_user != '7':
        ui.menu()
        input_from_user = input().strip()
        if input_from_user == '1': #Вывод списка заметок
            os.system('cls')
            f.show('all')
            continue_d = input("Нажмите любую клавишу для продолжения работы... ")
            os.system('cls')
        if input_from_user == '2': #Добавить заметку
            os.system('cls')
            f.add()
        if input_from_user == '3': #Удалить заметку
            os.system('cls')
            f.show('all')
            f.id_edit_del_show('del')
        if input_from_user == '4': #Редактировать заметку
            os.system('cls')
            f.show('all')
            f.id_edit_del_show('edit')
        if input_from_user == '5': #Вывод заметок по дате создания
            os.system('cls')
            f.show('date')
            continue_d = input("Нажмите любую клавишу для продолжения работы... ")
            os.system('cls')
        if input_from_user == '6': #Поиск по ID
            os.system('cls')
            f.show('id')
            f.id_edit_del_show('show')
            continue_d = input("Нажмите любую клавишу для продолжения работы... ")
            os.system('cls')
        if input_from_user == '7':
            os.system('cls')
            ui.buy()
            time.sleep(2)
            break