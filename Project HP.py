import re
import nltk
from pymystem3 import Mystem
from nltk.tokenize import word_tokenize, sent_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from ruword_frequency import Frequency
from collections import Counter

list_sent_tok = [] #делаем список, в котором каждый элемент список токенов одного предложения
def clean_text(sentences):
    for sent in sentences:
        text_str = sent.lower()  # нижний регистр
        text_list_nltk = word_tokenize(text_str)  # токенизация
        text_clean = [word for word in text_list_nltk if word[0].isalpha()] #убираем пунктуацию
        list_sent_tok.append(text_clean)
    return list_sent_tok

#стоп-слова не удаляем, тк иначе попадает много лишнего из предыдущих словосочетаний в биграммы с Гарри
with open('full_text_HP.txt', encoding='utf-8') as f:
    text = f.read()

hp_sent = sent_tokenize(text, language="russian") #разбиваем весь текст на предложения

clean_lists = clean_text(hp_sent) #токенизируем и чистим каждое предложение

mystem = Mystem()

clean_lists_morph = []
for list in clean_lists:  #берем предложение
    lemmas = mystem.lemmatize(' '.join(list))  #лемматизируем
    tagged = nltk.pos_tag(lemmas, lang='rus')  #добавляем морф разбор в виде кортежей
    clean_result = []
    for elem in tagged:
         if elem[1] != 'NONLEX':  # убираем пробелы, которые nltk разметил как NONLEX
             tag_tog = '_'.join(elem) #соединяем слово и метку
             clean_result.append(tag_tog) #собираем слова предложения с метками в список
    clean_lists_morph.append(clean_result) #формируем список списков

bigrams_hp = []  #разбиваем каждое предложение на биграммы
for sent in clean_lists_morph:
    bigrams = nltk.bigrams(sent)
    bigrams_hp.append(bigrams)

#for bigram in bigrams_hp:
    #print(list(bigram))  #не понимаю, как посмотреть все биграммы

before_harry = []
harry_bigrams = []
for i in bigrams_hp:
    for j in i:
     if j[1] == 'гарри_S' or j[1] == 'поттер_S':  #находим все биграммы, где имя или фамилия героя второй элемент
         before_harry.append(j[0])  #делаем список слов, которые идут перед именем героя
         harry_bigrams.append(j)   #делаем список всех биграмм с именем героя


before_harry = ' '.join(before_harry)
list_of_addj = re.findall('[а-яА-ЯёЁ]+_A=m', before_harry)  #находим все прилагательные по метке

final_adj = []
for i in list_of_addj:
     adj = re.sub('_A=m', '', i) #убираем частеречные метки
     final_adj.append(adj)

print(final_adj) #'общий попал из-за словосочетания "в общем" перед Гарри
print(len(final_adj))

#wordcloud = WordCloud(width = 2000,
                      #height = 1500,
                      #background_color='black',
                      #colormap='Pastel1').generate(', '.join(list_of_addj))
#plt.figure(figsize=(40, 30)) # Устанавливаем размер картинки
#plt.imshow(wordcloud) # Что изображаем
#plt.axis("off") # Без подписей на осях
#plt.show() # показать изображение
print(Counter(final_adj).most_common(30))

