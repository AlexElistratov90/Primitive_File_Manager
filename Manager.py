from Scripts.Main import File_Manager
from Scripts.Properties import File_manager_path

Primitive_FM = File_Manager(File_manager_path)
print("Current path: ", Primitive_FM.cur_dir())


while 1:
    command = input("*type ")
    if command.split(' ')[0] == "mk_dir":
        new_dir = command.split(' ')[1]
        Primitive_FM.mk_dir(new_dir)

    elif command.split(' ')[0] == "dl_dir":
        dir_name = command.split(' ')[1]
        Primitive_FM.dl_dir(dir_name)

    elif command.split(' ')[0] == "ch_dir":
        dir_name = command.split(' ')[1]
        Primitive_FM.ch_dir(dir_name)

    elif command.split(' ')[0] == "mk_file":
        f_name = command.split(' ')[1]
        Primitive_FM.mk_file(f_name)

    elif command.split(' ')[0] == "w_file":
        f_name = command.split(' ')[1]
        text = ' '.join(command.split(' ')[2:])
        Primitive_FM.w_file(f_name, text)

    elif command.split(' ')[0] == "r_file":
        f_name = command.split(' ')[1]
        Primitive_FM.r_file(f_name)

    elif command.split(' ')[0] == "dl_file":
        f_name = command.split(' ')[1]
        Primitive_FM.dl_file(f_name)

    elif command.split(' ')[0] == "copy_file":
        cur_path = command.split(' ')[1]
        new_path = command.split(' ')[2]
        Primitive_FM.copy_file(cur_path, new_path)

    elif command.split(' ')[0] == "move_file":
        cur_path = command.split(' ')[1]
        new_path = command.split(' ')[2]
        Primitive_FM.move_file(cur_path, new_path)

    elif command.split(' ')[0] == "re_file":
        file_path = command.split(' ')[1]
        new_name = command.split(' ')[2]
        Primitive_FM.re_file(file_path, new_name)

    elif command.split(' ')[0] == "cur_dir":
        print("Show current folder:", Primitive_FM.cur_dir())

    elif command == "l_s":
        print("Contents of the current folder: ")
        Primitive_FM.l_s()

    elif command == "help":
        Primitive_FM.my_help()

    elif command == "exit":
        print("Thanks for stopping by!")
        break
    else:
        print("Invalid command. type help for reference.")
