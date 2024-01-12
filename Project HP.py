import re
import nltk
from pymystem3 import Mystem
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from ruword_frequency import Frequency
from collections import Counter



def clean_text(text_str):
  text_str = text_str.lower()  # нижний регистр
  text_list_nltk = word_tokenize(text_str)  # токенизация
  text_clean = [word for word in text_list_nltk if word[0].isalpha()]
  return text_clean

#стоп-слова не удаляем, тк иначе попадает много лишнего из предыдущих словосочетаний в биграммы с Гарри
with open('HP book1', encoding='utf-8') as f:
    text = f.read()

clean_text = ' '.join(clean_text(text))

mystem = Mystem()
clean_text = mystem.lemmatize(clean_text)


#возможно стоит сначала разбить на предложения, чтобы не попадали предыдущие предложения
#добавить еще формы Поттер Поттера и тд

tagged = nltk.pos_tag(clean_text, lang='rus')


list_of_tagged = []
for elem in tagged:
    if elem[1] != 'NONLEX': #убираем пробелы, которые nltk разметил как NONLEX
        tag_tog = '_'.join(elem)
        list_of_tagged.append(tag_tog) #приклеиваем к словам части речи


bigrams_hp = nltk.bigrams(list_of_tagged)

before_harry = []
harry_bigrams = []
for i in list(bigrams_hp):
    if i[1] == 'гарри_S':
        before_harry.append(i[0])
        harry_bigrams.append(i)

before_harry = ' '.join(before_harry)
list_of_addj = re.findall('[а-яА-ЯёЁ]+_A=m', before_harry)

final_adj = []
for i in list_of_addj:
    adj = re.sub('_A=m', '', i) #убираем частеречные метки
    final_adj.append(adj)

print(before_harry)
print(final_adj)

#wordcloud = WordCloud(width = 2000,
                      #height = 1500,
                      #background_color='black',
                      #colormap='Pastel1').generate(', '.join(list_of_addj))
#plt.figure(figsize=(40, 30)) # Устанавливаем размер картинки
#plt.imshow(wordcloud) # Что изображаем
#plt.axis("off") # Без подписей на осях
#plt.show() # показать изображение
print(Counter(final_adj).most_common(30))

print(list_of_tagged)
