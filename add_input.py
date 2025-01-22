username=input('Введите имя пользователя ')

title1 = input("Введите заголовок№1 заметки: ")
title2 = input("Введите заголовок№2 заметки: ")
title3 = input("Введите заголовок№3 заметки: ")
titles = [title1, title2, title3]

content=input('Введите текст ')
status=input("Введите статус задачи ")
created_date=input("Дата создания'дд.мм.гггг' ")
issue_date=input("Дата истечения заметки'дд.мм.гггг' ")

print("Имя пользователя:", username)
print("Заголовки заметки:", titles)
print("Текст заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
