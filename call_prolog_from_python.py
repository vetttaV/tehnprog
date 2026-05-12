'''
Для работы примера необходимо установить SWI-Prolog.
Под Windows и MacOS можно скачать последнюю версию с сайта
https://www.swi-prolog.org/download/stable
Под Ubuntu Linux надо ставить его, как сказано здесь:
https://www.swi-prolog.org/build/PPA.html (вариант ---stable version)
Под другие системы можно попробовать snap, но есть риск несовместимости версий с интерфейсным пакетом для Python:
https://www.swi-prolog.org/build/snap.html
Более общий вариант --- самостоятельная сборка; заниматься можно, если других вариантов нет:
https://www.swi-prolog.org/build/unix.html
Если будут вопросы с установкой, желательно обращаться ко мне напрямую.

После этого следует установить интерфейсный модуль SWI-Prolog и python:
pip3 install --user janus_swi

'''

import janus_swi

# разрешим до загрузки кода менять предикат
# parent с 2 параметрами; без этого можно будет только 
# запрашивать факты parent из базы, а добавлять
# новые будет нельзя
janus_swi.query_once('dynamic parent/2',{})

# загружаем файл с текстом программы на Prolog
janus_swi.consult('lecture1_examples.pl')

# запрос первого попавшегося совпадения
#print('One result:', janus_swi.query_once('parent(X,alice)',{}))
# ответ: {'truth': True, 'X': 'charlie'}

# запрос всех совпадений:
#print('All results:')
#for q in janus_swi.query('parent(X,alice)',{}):
 #   print(q)
# ответы:
# {'truth': True, 'X': 'charlie'}
# {'truth': True, 'X': 'diane'}

# запрос, завершающийся неудачей
#print('No results:', janus_swi.query_once('parent(alice, X)',{}))
# ответ: {'truth': False, 'X': None}

# запрос с указанием значений параметров
#print('Query with params:', janus_swi.query_once('parent(X, Y)',
    #                                             {'Y': 'bob'}))
# так как это query_once, то результат
# {'truth': True, 'X': 'charlie'}

# передача нового факта;
# если бы в начале мы не объявили
# предикат parent dynamic, это не сработало бы.
# assertz добавляет факт после всех имеющихся
# фактов с этим же предикатом,
# asserta --- до них
janus_swi.query_once('assertz(parent(alice,zack))',{})

# проверяем, что данные обновились
#print('New result:', janus_swi.query_once('parent(alice, X)',{}))

# проверяем, что прежние данные не испортились
#print('New query:')
#for q in janus_swi.query('parent(X,zack),parent(Y,X)',{}):
 #   print(q)
    
# удаляем факт из базы
janus_swi.query_once('retract(parent(alice,zack))',{})
# проверяем, что прежние данные не испортились
#print('Query retracted fact:',
#      janus_swi.query_once('parent(X,zack)',{}))

unique_names = set()
for result in janus_swi.query('has_kids_with_two_partners(X)', {}):
    unique_names.add(result['X'])
print('Люди с детьми от разных партнеров:')
for name in unique_names:
    print(name)

print('2А')

query1 = 'remove_third([1,2,3,4,5,6,7], Result).'
result1 = janus_swi.query_once(query1, {})
print(result1['Result'])

query2 = 'remove_third([a,b,c,d,e], Result).'
result2 = janus_swi.query_once(query2, {})
print(result2['Result'])


print('3А')

query1 = 'even_length([1, 2, 3, 4]).'
result1 = janus_swi.query_once(query1, {})
print(f"Длина списка [1, 2, 3, 4] чётная? {result1['truth']}")

query2 = 'even_length([a, b, c, d, e]).'
result2 = janus_swi.query_once(query2, {})
print(f"Длина списка [a, b, c, d, e] чётная? {result2['truth']}")

query3 = 'even_length([]).'
result3 = janus_swi.query_once(query3, {})
print(f"Длина пустого списка чётная? {result3['truth']}")


print('4Б')

q1 = "is_sublist([1,2,3], [0,1,2,3,4,5])."
print(f"Входит ли [1,2,3] в [0,1,2,3,4,5]? {janus_swi.query_once(q1, {})['truth']}")

q2 = "is_sublist([1,2,3], [a,b,c,1,2,3,d])."
print(f"Входит ли [1,2,3] в [a,b,c,1,2,3,d]? {janus_swi.query_once(q2, {})['truth']}")

q3 = "is_sublist([1,2,3], [1,2,a,3])."
print(f"Входит ли [1,2,3] в [1,2,a,3]? {janus_swi.query_once(q3, {})['truth']}")


print('5А')

query_flatten = "flatten_one_level([[a,b], [1,2,3], [c,d,[e,f]], [], [4]], Result)."
result_flatten = janus_swi.query_once(query_flatten, {})
print(f"Объединенный список:\n{result_flatten['Result']}")
