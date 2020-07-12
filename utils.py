# from ast import literal_eval
# from pathlib import Path
from os import system
# import sqlite3

def show_menu():
  system('clear')
  menu = '''
密碼管理大師
=================
1. 新增帳密
2. 顯示帳密
3. 修改密碼
4. 刪除帳密

輸入q結束程式
=================
'''
  print(menu)
  

def read_DB(conn):
  cursor = conn.cursor()
  
  cursor.execute("CREATE TABLE IF NOT EXISTS Passwords('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'name' TEXT NOT NULL,'password' TEXT NOT NULL);")

  cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Passwords'")
  if cursor.fetchone()[0] == 1:
    print('開啟資料庫...')
    return True
  else:
    print('資料庫無法開啟')
    return False

    


def add_password(conn):
  while True:
    name = input('輸入帳號(按ENTER鍵返回)：')
    if name == '':
      break
    cursor = conn.execute(f'SELECT * FROM Passwords WHERE "name" = "{name}"')
    row = cursor.fetchone()
    if row != None:
      print('帳號已存在，請換另一個帳號名稱')
      continue
    password = input('輸入密碼(按ENTER鍵返回)：')
    if password == '':
      break
    conn.execute(f'INSERT INTO Passwords (name, password) VALUES("{name}", "{password}")')
    conn.commit()
    print(f'{name} 已儲存')
    # with open('password.txt', 'w', encoding='utf-8-sig') as f:
    #   f.write(str(passwords_dict))
    #   print(f'{name}已儲存')
    input('')
    break
    

  

def show_password(conn):
  s = '''
ID\t\t帳號\t\t密碼
===========================
'''
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM Passwords')
  rows = cursor.fetchall()
  for row in rows:
    s += f'{row[0]}\t\t{row[1]}\t\t{row[2]}\n'
  s+= '\n'
  print(s)
  input()

def edit_password(conn):
  while True:
    name = input('輸入帳號(按ENTER鍵返回)：')
    if name == '':
      break
    cursor = conn.execute(f'SELECT * FROM Passwords WHERE "name" = "{name}"')
    row = cursor.fetchone()
    if row == None:
      print('帳號不存在')
      continue
    while True:
      password = input('輸入原密碼：')
      if password == row[2]:
        break
      print('密碼錯誤')

    new_password = input('輸入新密碼：')
    conn.execute(f'UPDATE Passwords SET password = {new_password} WHERE name={name};')
    conn.commit()

    # with open('password.txt', 'w', encoding='utf-8-sig') as f:
    #   f.write(str(passwords_dict))
    #   print(f'{name} 密碼已儲存')
    input('')
    break
  
  

def del_password(conn):
  while True:
    name = input('輸入帳號(按ENTER鍵返回)：')
    if name == '':
      break
    cursor = conn.execute(f'SELECT * FROM Passwords WHERE "name" = "{name}"')
    row = cursor.fetchone()
    if row==None:
      print('帳號不存在')
      continue
    
    choice = input(f'確定要刪除{name}的帳密嗎？(y/n) ').lower()
    if choice == 'y':
      conn.execute(f'DELETE FROM Passwords WHERE "name" = "{name}";')
      conn.commit()
      print(f'{name} 已刪除')
      # with open('password.txt', 'w', encoding='utf-8-sig') as f:
      #   f.write(str(passwords_dict))
      #   print(f'{name} 已刪除')

    input('')
    break
  
 
  

