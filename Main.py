# Импорт библиотек
import os
import shutil
from pathlib import Path


class File_Manager:
    def __init__(self, my_work_dir):
        self.MY_WORK_DIR = Path(my_work_dir).absolute()

        try:
            os.chdir(self.MY_WORK_DIR)
        except FileNotFoundError:
            print("Could not find working folder.")

        self.my_cur_dir = Path(my_work_dir).absolute()
        self.my_latest_dir = self.MY_WORK_DIR.name

    # Справка
    def my_help(self):
        print("Welcome to в File_Manager. Main fuctions:\n")
        print("exit                          Exit File_Manager")
        print("mk_dir [name]                 Create a folder by name")
        print("ch_dir [name]                 Moving between folders")
        print("dl_dir [name]                 Deleting a folder by name")
        print("mk_file [name]                Create empty files with specified name")
        print("w_file [name] [text]          Writing text to file")
        print("r_file  [name]                View file")
        print("dl_file  [name]               Deleting a file by name")
        print("copy_file [name] [new_dir]    Copying files from one folder to another")
        print("move_file [name] [new_dir]    Moving file to another folder")
        print("re_file [name] [new_name]     Renaming file")
        print("l_s                           Show folder structure")
        print("cur_dir                       Show current folder")
        print("help                          Help")
    # Показать текущую папку
    def cur_dir(self):
        return os.getcwd()

    # Показать структуру
    def l_s(self):
        if os.listdir(path=self.cur_dir):
            for i in os.listdir(path=self.cur_dir):
                print(i)
        else:
            print("WARNING!! The folder is empty.")
    # Создание новой папки
    def mk_dir(self, path):
        try:
            if os.path.exists(path):
                print("WARNING!! A folder with the same name already exists.")
            else:
                os.makedirs(str(path))
                print(f'The folder {path.split("/")[-1]} successfully created.')
        except FileNotFoundError:
            print("WARNING!! Invalid path.")

    # Удаление папки
    def dl_dir(self, path):
        if os.path.isdir(path):
            shutil.rmtree(str(path), ignore_errors=True)
            print(f'The folder {path.split("/")[-1]} was successfully deleted.')
        else:
            print("WARNING!! The folder not found.")

    # Смена директории
    def ch_dir(self, path):
        try:
            if len(path) != 0:
                if path == "..":
                    if self.my_latest_dir in str(self.cur_dir.parent):
                        os.chdir(self.cur_dir.parent)
                        self.cur_dir = self.MY_WORK_DIR.joinpath(self.cur_dir.parent)
                        print("Current path: ", self.cur_dir)
                    else:
                        print("WARNING!! Unable to go outside the working folder!")
                else:
                    os.chdir(path)
                    self.cur_dir = self.MY_WORK_DIR.joinpath(path)
                    print("Current path:", self.cur_dir)
        except FileNotFoundError:
            print("WARNING!! The folder not found")
        except OSError:
            print("WARNING!! The folder not found")

    # Создание нового файла
    def mk_file(self, path):
        try:
            if os.path.exists(path):
                print("WARNING!! A file with the same name already exists.")
            else:
                open(path, "w", encoding="utf-8").close()
                print(f'The file {path} was successfully created.')
        except FileNotFoundError:
            print("WARNING!! The file not found")

    # Запись в файл
    def w_file(self, path, inner):
        try:
            self.cur_dir.joinpath(path).write_text(inner)
            print(f"Text '{inner}' successfully added into the {path}.")
        except FileNotFoundError:
            print("WARNING!! The file not found")

    # Чтение файла
    def r_file(self, path):
        try:
            if os.path.exists(path):
                print(str(self.cur_dir.joinpath(path).read_text()))
            else:
                print("WARNING!! The file not found")
        except OSError:
            print("WARNING!! The file not found")

    # Удаление файла
    def dl_file(self, path):
        try:
            if os.path.exists(path):
                os.remove(self.cur_dir.joinpath(path))
                print(f'The file {path} was removed.')
            else:
                print("WARNING!! The file not found")
        except OSError:
            print("WARNING!! The file not found")

    # Копирование файла
    def copy_file(self, cur_path, new_path):
        try:
            if os.path.exists(cur_path):
                shutil.copy2(cur_path, new_path)
                print(f'File copied into {new_path}')
            else:
                print("WARNING!! The file not found")
        except OSError:
            print("WARNING!! The file not found")

    # Перемещение файла
    def move_file(self, cur_path, new_path):
        try:
            if os.path.exists(cur_path):
                shutil.move(cur_path, new_path)
                print(f"File moved from {curr_path} into {new_path}")
            else:
                print("WARNING!! The file not found")
        except OSError:
            print("WARNING!! The file not found")

    # Переименование файла
    def re_file(self, path, new_name):
        try:
            if os.path.exists(path):
                self.cur_dir.joinpath(path).rename(new_name)
                print(f"File renamed to {new_name}")
            else:
                print("WARNING!! The file not found")
        except FileExistsError:
            print("WARNING!! The file already exists")
        except OSError:
            print("WARNING!! The file not found")