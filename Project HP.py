import re
import nltk
from pymystem3 import Mystem
from nltk.tokenize import word_tokenize, sent_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from ruword_frequency import Frequency
from collections import Counter
import numpy as np
from PIL import Image
from collections import Counter

list_sent_tok = []  # делаем список, в котором каждый элемент список токенов одного предложения


def clean_text(sentences):
    for sent in sentences:
        text_str = sent.lower()  # нижний регистр
        text_list_nltk = word_tokenize(text_str)  # токенизация
        text_clean = [word for word in text_list_nltk if word[0].isalpha()]  # убираем пунктуацию
        list_sent_tok.append(text_clean)
    return list_sent_tok


# стоп-слова не удаляем, тк иначе попадает много лишнего из предыдущих словосочетаний в биграммы с Гарри
with open('full_text_HP.txt', encoding='utf-8') as f:
    text = f.read()

hp_sent = sent_tokenize(text, language="russian")  # разбиваем весь текст на предложения

clean_lists = clean_text(hp_sent)  # токенизируем и чистим каждое предложение

mystem = Mystem()

clean_lists_morph = []
for list in clean_lists:  # берем предложение
    lemmas = mystem.lemmatize(' '.join(list))  # лемматизируем
    tagged = nltk.pos_tag(lemmas, lang='rus')  # добавляем морф разбор в виде кортежей
    clean_result = []
    for elem in tagged:
        if elem[1] != 'NONLEX':  # убираем пробелы, которые nltk разметил как NONLEX
            tag_tog = '_'.join(elem)  # соединяем слово и метку
            clean_result.append(tag_tog)  # собираем слова предложения с метками в список
    clean_lists_morph.append(clean_result)  # формируем список списков

# разбиваем каждое предложение на биграммы
bigrams_hp = []  # разбиваем каждое предложение на биграммы
for sent in clean_lists_morph:
    bigrams = nltk.bigrams(sent)
    bigrams_hp.append(bigrams)

before_germ = []
germ_bigrams = []
before_ron = []
ron_bigrams = []
before_harry = []
harry_bigrams = []


#собираем список слов перед именем героя и список биграмм, где герой на втором месте

for i in bigrams_hp:
    for j in i:
        if j[1] == 'гермиона_S' or j[1] == 'грейнджер_S':
            before_germ.append(j[0])
            germ_bigrams.append(j)
        elif j[1] == 'рон_S' or j[1] == 'рона_S':  #у Рона для поиска используем только имя, так как Уизли много
            before_ron.append(j[0])
            ron_bigrams.append(j)
        elif j[1] == 'гарри_S' or j[1] == 'поттер_S':
            before_harry.append(j[0])
            harry_bigrams.append(j)


#ищем прилагательные

before_germ = ' '.join(before_germ)
list_of_addj_germ = re.findall('[а-яА-ЯёЁ]+_A=m', before_germ)
before_ron = ' '.join(before_ron)
list_of_addj_ron = re.findall('[а-яА-ЯёЁ]+_A=m', before_ron)
before_harry = ' '.join(before_harry)
list_of_addj_harry = re.findall('[а-яА-ЯёЁ]+_A=m', before_harry)

#убираем частеречные метки

final_adj_germ = []
for i in list_of_addj_germ:
    adj = re.sub('_A=m', '', i)
    final_adj_germ.append(adj)

final_adj_ron = []
for i in list_of_addj_ron:
    adj = re.sub('_A=m', '', i)
    final_adj_ron.append(adj)

final_adj_harry = []
for i in list_of_addj_harry:
    adj = re.sub('_A=m', '', i)
    final_adj_harry.append(adj)


#смотрим какие прилагательные нашлись и их частотность

print(Counter(final_adj_harry).most_common(50))
print(Counter(final_adj_ron).most_common(50))
print(Counter(final_adj_germ).most_common(50))

germ_mask = np.array(Image.open("germ.jpeg"))
ron_mask = np.array(Image.open("Ron.jpeg"))
harry_mask = np.array(Image.open("Harry.jpeg"))

#облако гарри
wordcloud3 = WordCloud(width = 2000,
                      height = 1500,
                      mask=harry_mask,
                      contour_width=3,
                      contour_color='steelblue',
                      background_color='black',
                      colormap='Pastel1').generate(', '.join(final_adj_harry))
plt.figure(figsize=(40, 30)) # Устанавливаем размер картинки
plt.imshow(wordcloud3) # Что изображаем
plt.title('Гарри Поттер')
plt.axis("off") # Без подписей на осях
plt.show() # показать изображение

#облако гермиона
wordcloud = WordCloud(width = 2000,
                      height = 1500,
                      mask=germ_mask,
                      contour_width=3,
                      contour_color='steelblue',
                      background_color='black',
                      colormap='Pastel1').generate(', '.join(final_adj_germ))
plt.figure(figsize=(40, 30)) # Устанавливаем размер картинки
plt.imshow(wordcloud) # Что изображаем
plt.title('Гермиона Грейнджер')
plt.axis("off") # Без подписей на осях
plt.show() # показать изображение

#облако рон
wordcloud2 = WordCloud(width = 2000,
                      height = 1500,
                      mask=ron_mask,
                      contour_width=3,
                      contour_color='steelblue',
                      background_color='black',
                      colormap='Pastel1').generate(', '.join(final_adj_ron))
plt.figure(figsize=(40, 30)) # Устанавливаем размер картинки
plt.imshow(wordcloud2) # Что изображаем
plt.title('Рон Уизли')
plt.axis("off") # Без подписей на осях
plt.show() # показать изображение

