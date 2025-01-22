note = {}

note["username"] = input('Введите имя пользователя ')
note["content"] = input('Введите текст ')
note["status"] = input("Введите статус задачи ")
note["created_date"] = input("Дата создания'дд.мм.гггг' ")
note["issue_date"] = input("Дата истечения заметки'дд.мм.гггг' ")

titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)

print(note)

