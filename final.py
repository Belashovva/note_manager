note = {}

note["username"] = input('Введите имя пользователя ')
titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)
note["content"] = input('Введите текст ')
note["status"] = input("Введите статус задачи ")

created_date=input("Дата создания'дд.мм.гггг' ")
issue_date=input("Дата истечения заметки'дд.мм.гггг' ")
note["created_date"] = created_date[:5]
note["issue_date"] = issue_date[:5]

print(note)
