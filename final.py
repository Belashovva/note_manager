username=input('Введите имя пользователя ')
title0=input('Введите название заметки ')
title1=input('Заголовок 1 ')
title2=input('Заголовок 2 ')
title3=input('Заголовок 3 ')
content=input('Введите текст ')
status=input("Введите статус задачи ")
created_date=input("Дата создания'дд.мм.гггг' ")
issue_date=input("Дата истечения заметки'дд.мм.гггг' ")

print(username)
print(title0)
print(title1)
print(title2)
print(title3)
print(content)
print(status)
print(created_date)
print(issue_date)

note=[
username,
content,
status,
created_date,
issue_date,
[title0, title1, title2, title3]]

print(note)