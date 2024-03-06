import sqlite3

# Создаем базу данных
conn = sqlite3.connect('phone_book.db')
c = conn.cursor()
# Создаем таблицу
c.execute("""CREATE TABLE IF NOT EXISTS phone_book (
    name TEXT,
    phone_number TEXT
)""")
# Добавляем данные из файла
with open('phonebook.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, phone_number = line.strip().split()
        c.execute("INSERT INTO phone_book VALUES (?, ?)", (name, phone_number))

conn.commit()

conn.close()


def add(pb):
    conn = sqlite3.connect('phone_book.db')
    c = conn.cursor()
    name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    c.execute("INSERT INTO phone_book (name, phone_number) VALUES (?, ?)", (name, phone_number))
    with open('phonebook.txt', 'a', encoding='utf-8') as f:
        f.write(f"{name} {phone_number}\n")
    conn.commit()
    conn.close()

def all(pb):
    conn = sqlite3.connect('phone_book.db')
    c = conn.cursor()
    c.execute("SELECT  *  FROM phone_book ")
    results = c.fetchall()
    for result in results:
        print(f"{result[0]} {result[1]}\n")
    # c.execute("DELETE FROM phone_book")



def search(pb):
    conn = sqlite3.connect('phone_book.db')
    c = conn.cursor()
    name = input("Введите имя для поиска: ")
    c.execute("SELECT  *  FROM phone_book WHERE name=?", (name,))
    results = c.fetchall()
    for result in results:
        print(f"{result[0]} {result[1]}\n")
    # c.execute("DELETE FROM phone_book")
    conn.commit()
    conn.close()

def show_menu():
    print("\nВыберите:\n"
          "1. Отобразаить весь справочник\n"
          "2. Найти абонента по номеру телефона\n"
          "3. Добавить абонента в справочник\n"
	      "4. Сохранить справочник в текстовом формате\n"
          "5. Закончить работу")
    choice = int(input())
    return choice



def work_with_phonebook():
	

    choice=show_menu()

    phone_book=('phonebook.txt')

    while (choice!=7):
        if choice==1:
            all(phone_book)    
        elif choice==2:
            search(phone_book)  
        elif choice==3:
            add(phone_book)           
        
        choice=show_menu()
        

work_with_phonebook()