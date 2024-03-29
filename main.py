#  users, todos
# 1. get -> one, all
# 2. create-> поля для заполнения
# 3. update -> поля для обновления определенного пользователя
# 4. delete -> удаляем определенного пользователя
# рефакторинг
import texts
from crud.users import UserService
from database.db import Connection

user_service = UserService()
db = Connection('todos.db')


while True:
    work_with = input(texts.INTRO_TEXT)

    if work_with == 'users':
        print(texts.USERS_INTRO_TEXT)
        command = input(texts.USERS_COMMANDS_TEXT)
        if command == '1':
            print(texts.USER_SELECTED_COMMAND_TEXT[command])
            command_get = input(texts.USERS_COMMANDS_GET_TEXT)
            if command_get == '1':
                print()
            elif command_get == '2':
                users = user_service.read(db, all=True)
                for user_id, username in users:
                    print(f'''
==========
ID: {user_id}
USERNAME: {username}
==========
''')
        elif command == '2':
            print(texts.USER_SELECTED_COMMAND_TEXT[command])
            command_create = input(texts.USER_COMMANDS_CREATE_TEXT)
        elif command == '3':
            print(texts.USER_SELECTED_COMMAND_TEXT[command])
            command_update = input(texts.USER_COMMAND_UPDATE_TEXT)
        elif command == '4':
            print(texts.USER_SELECTED_COMMAND_TEXT[command])
            command_delete = input(texts.USER_COMMAND_DELETE_TEXT)