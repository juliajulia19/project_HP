from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('punkt')
import matplotlib.pyplot as plt
import string

# 1st book
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
nltk.download('punkt')
import matplotlib.pyplot as plt
import string

with open(r"/content/sample_data/HP book1.txt", encoding='utf-8') as f:

    text = f.read()

text = text.translate(str.maketrans('', '', string.punctuation)).lower()

with open (r"/content/sample_data/spells_clean.txt", encoding='windows-1251') as file :
     spells = file.read
     spells = [line.strip().translate(str.maketrans('', '', string.punctuation)) for line in file.readlines()]

print(spells)
spell_counts = {spell.strip(): text.count(spell.strip()) for spell in spells}
print(spell_counts)
print(sorted(spell_counts.items(), key=lambda x: x[1],reverse=True))

spells = []
counts = []

for spell, count in sorted(spell_counts.items(), key=lambda x: x[1],reverse=True)[:10]:
   spells.append(spell)
   counts.append(count)
print(spells, counts)

plt.figure(figsize=(8, 5))

plt.bar(spells, counts)
plt.title('Количество заклинаний в "Гарри Поттер и философский камень"')
plt.xlabel('Заклинания')
plt.ylabel('Кол-во использований')
plt.xticks(rotation=90)
plt.show()


# 2nd book

with open(r"/content/sample_data/Гарри Поттер и Тайная комната .txt", encoding='windows-1251') as f:

    text = f.read()

text = text.translate(str.maketrans('', '', string.punctuation)).lower()

with open (r"/content/sample_data/spells_clean.txt", encoding='windows-1251') as file :
     spells = file.read
     spells = [line.strip().translate(str.maketrans('', '', string.punctuation)) for line in file.readlines()]

print(spells)
spell_counts = {spell.strip(): text.count(spell.strip()) for spell in spells}
print(spell_counts)
print(sorted(spell_counts.items(), key=lambda x: x[1],reverse=True))

spells = []
counts = []

for spell, count in sorted(spell_counts.items(), key=lambda x: x[1],reverse=True)[:10]:
   spells.append(spell)
   counts.append(count)
print(spells, counts)

plt.figure(figsize=(8, 5))

plt.bar(spells, counts)
plt.title('Количество заклинаний в "Гарри Поттер и Тайная комната"')
plt.xlabel('Заклинания')
plt.ylabel('Кол-во использований')
plt.xticks(rotation=90)
plt.show()

# 3 rd book

with open(r"/content/sample_data/Гарри Поттер и узник Азкабана.txt", encoding='windows-1251') as f:

    text = f.read()

text = text.translate(str.maketrans('', '', string.punctuation)).lower()

with open (r"/content/sample_data/spells_clean.txt", encoding='windows-1251') as file :
     spells = file.read
     spells = [line.strip().translate(str.maketrans('', '', string.punctuation)) for line in file.readlines()]

print(spells)
spell_counts = {spell.strip(): text.count(spell.strip()) for spell in spells}
print(spell_counts)
print(sorted(spell_counts.items(), key=lambda x: x[1],reverse=True))

spells = []
counts = []

for spell, count in sorted(spell_counts.items(), key=lambda x: x[1],reverse=True)[:10]:
   spells.append(spell)
   counts.append(count)
print(spells, counts)

plt.figure(figsize=(8, 5))

plt.bar(spells, counts)
plt.title('Количество заклинаний в "Гарри Поттер и узник Азкабана"')
plt.xlabel('Заклинания')
plt.ylabel('Кол-во использований')
plt.xticks(rotation=90)
plt.show()

#4th book

with open(r"/content/sample_data/Гарри Поттер и Кубок огня.txt", encoding='windows-1251') as f:

    text = f.read()

text = text.translate(str.maketrans('', '', string.punctuation)).lower()

with open (r"/content/sample_data/spells_clean.txt", encoding='windows-1251') as file :
     spells = file.read
     spells = [line.strip().translate(str.maketrans('', '', string.punctuation)) for line in file.readlines()]

print(spells)
spell_counts = {spell.strip(): text.count(spell.strip()) for spell in spells}
print(spell_counts)
print(sorted(spell_counts.items(), key=lambda x: x[1],reverse=True))

spells = []
counts = []

for spell, count in sorted(spell_counts.items(), key=lambda x: x[1],reverse=True)[:18]:
   spells.append(spell)
   counts.append(count)
print(spells, counts)

plt.figure(figsize=(8, 5))

plt.bar(spells, counts)
plt.title('Количество заклинаний в "Гарри Поттер и Кубок огня"')
plt.xlabel('Заклинания')
plt.ylabel('Кол-во использований')
plt.xticks(rotation=90)
plt.show()

#5th book


with open(r"/content/sample_data/Гарри Поттер и принц-полукровка.txt", encoding='windows-1251') as f:

    text = f.read()

text = text.translate(str.maketrans('', '', string.punctuation)).lower()

with open (r"/content/sample_data/spells_clean.txt", encoding='windows-1251') as file :
     spells = file.read
     spells = [line.strip().translate(str.maketrans('', '', string.punctuation)) for line in file.readlines()]

print(spells)
spell_counts = {spell.strip(): text.count(spell.strip()) for spell in spells}
print(spell_counts)
print(sorted(spell_counts.items(), key=lambda x: x[1],reverse=True))

spells = []
counts = []

for spell, count in sorted(spell_counts.items(), key=lambda x: x[1],reverse=True)[:25]:
   spells.append(spell)
   counts.append(count)
print(spells, counts)

plt.figure(figsize=(8, 5))

plt.bar(spells, counts)
plt.title('Количество заклинаний в "Гарри Поттер и принц-полукровка"')
plt.xlabel('Заклинания')
plt.ylabel('Кол-во использований')
plt.xticks(rotation=90)
plt.show()

#6th book


with open(r"/content/sample_data/Гарри Поттер и принц-полукровка.txt", encoding='windows-1251') as f:

    text = f.read()

text = text.translate(str.maketrans('', '', string.punctuation)).lower()

with open (r"/content/sample_data/spells_clean.txt", encoding='windows-1251') as file :
     spells = file.read
     spells = [line.strip().translate(str.maketrans('', '', string.punctuation)) for line in file.readlines()]

print(spells)
spell_counts = {spell.strip(): text.count(spell.strip()) for spell in spells}
print(spell_counts)
print(sorted(spell_counts.items(), key=lambda x: x[1],reverse=True))

spells = []
counts = []

for spell, count in sorted(spell_counts.items(), key=lambda x: x[1],reverse=True)[:25]:
   spells.append(spell)
   counts.append(count)
print(spells, counts)

plt.figure(figsize=(8, 5))

plt.bar(spells, counts)
plt.title('Количество заклинаний в "Гарри Поттер и принц-полукровка"')
plt.xlabel('Заклинания')
plt.ylabel('Кол-во использований')
plt.xticks(rotation=90)
plt.show()

#7th book


with open(r"/content/sample_data/Гарри Поттер и дары смерти.txt", encoding='windows-1251') as f:

    text = f.read()

text = text.translate(str.maketrans('', '', string.punctuation)).lower()

with open (r"/content/sample_data/spells_clean.txt", encoding='windows-1251') as file :
     spells = file.read
     spells = [line.strip().translate(str.maketrans('', '', string.punctuation)) for line in file.readlines()]

print(spells)
spell_counts = {spell.strip(): text.count(spell.strip()) for spell in spells}
print(spell_counts)
print(sorted(spell_counts.items(), key=lambda x: x[1],reverse=True))

spells = []
counts = []

for spell, count in sorted(spell_counts.items(), key=lambda x: x[1],reverse=True)[:25]:
   spells.append(spell)
   counts.append(count)
print(spells, counts)

plt.figure(figsize=(8, 5))

plt.bar(spells, counts)
plt.title('Количество заклинаний в "Гарри Поттер и Дары смерти"')
plt.xlabel('Заклинания')
plt.ylabel('Кол-во использований')
plt.xticks(rotation=90)
plt.show()

