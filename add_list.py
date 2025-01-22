username=input('Введите имя пользователя ')
title0=input('Введите название заметки ')
titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)
content=input('Введите текст ')
status=input("Введите статус заметки (Активна, Выполнена, В процессе, Просрочено) ")

created_date=input("Дата создания'дд.мм.гггг' ")
issue_date=input("Дата истечения заметки'дд.мм.гггг' ")


print("\nИнформация о заметке:")
print("Имя пользователя:", username)
print("Заголовки заметки:", titles)
print("Текст заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
