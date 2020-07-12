from utils import show_menu, read_DB, add_password, show_password, edit_password, del_password
import sqlite3

conn = sqlite3.connect('passwords.db')
is_success = read_DB(conn)
if is_success:
  while True:
    show_menu()
    cmd = input('輸入你的指令：')

    if cmd == '1':
      add_password(conn)
    elif cmd == '2':
      show_password(conn)
    elif cmd == '3':
      edit_password(conn)
    elif cmd == '4':
      del_password(conn)
    elif cmd == 'q':
      break
