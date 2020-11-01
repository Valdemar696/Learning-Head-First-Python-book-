phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for a in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
# plist.insert(4, plist.pop())   9-ую написал сам, в учебнике для примера работы экстенда дана 10-ая. Бля, ну моя же проще
plist.extend([plist.pop(), plist.pop()]) # сначала работают попы, извлекает элементы p и a. потом экстендом их вставляет.
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)