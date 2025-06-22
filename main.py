"""
### Задача 1: Средние расходы по семестрам  
Джон записал свои ежемесячные расходы за прошлый год:  
```python
monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
```  
Напишите программу, которая с помощью цикла `for` вычисляет средние расходы Джона за первый семестр (январь–июнь) и второй семестр (июль–декабрь).  

---
"""
monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

sum_first = 0
for i in range(6):
    sum_first += monthly_spending[i]

sum_second = 0
for i in range(6, 12):
    sum_second += monthly_spending[i]

average_first = sum_first / 6
average_second = sum_second / 6

print("Средние расходы за первый семестр:", round(average_first, 2))
print("Средние расходы за второй семестр:", round(average_second, 2))


"""
### Задача 2: Кто тратил больше?  
У Джона есть друг Сэм, который также записал свои ежемесячные расходы за прошлый год:  
```python
john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]  
sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]
```  
Напишите программу, которая сравнивает расходы Джона и Сэма по месяцам и подсчитывает количество месяцев, в которых Джон тратил больше.  

"""
john = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
sam = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]

count = 0
for i in range(12):
    if john[i] > sam[i]:
        count += 1

print(count)


"""
---

### Задача 3: Список друзей  
У Пола и Тины есть списки друзей:  
```python
paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
```  
Объедините оба списка в один, исключив дублирующиеся имена.  

"""
paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

Common_friends = list(set(paul_friends + tina_friends))

print(Common_friends)

"""
---

### Задача 4: Общие друзья  
Используя те же списки друзей Пола и Тины, напишите программу, которая с помощью цикла находит их общих друзей.  

"""
paul_friends = ["Mary", "Tim", "Mike", "Henry"]  
tina_friends = ["Tim", "Susan", "Mary", "Josh"]
mutual_friends = []

for friend in paul_friends:
    if friend in tina_friends :
        mutual_friends.append(friend)

print(mutual_friends)

"""
---

### Задача 5: Игроки в баскетбол  
В спортивном клубе зарегистрированы игроки:  
```python
football_players = {"Eve", "Tom", "Richard", "Peter"}  
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}  
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}
```  
Напишите программу, которая определяет игроков, зарегистрированных только в баскетболе (не в футболе и не в волейболе).  

"""
football_players = {"Eve", "Tom", "Richard", "Peter"}  
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}  
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}
all_basket_players = basketball_players - (football_players | volleyball_players) 
print(all_basket_players)



"""
---

### Задача 6: Подсчёт голосов  
Результаты опроса о любимом языке программирования:  
```python
poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]
```  
Используя словарь, подсчитайте количество голосов за каждый язык.  
"""
poll_results = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]
votes_count = {}

for language in poll_results:
    if language in votes_count:
        votes_count[language] += 1
    else:
        votes_count[language] = 1

print(votes_count)


"""
---

### Задача 7: Подсчёт очков  
Три друга играют в игру, где каждый игрок зарабатывает очки в трёх раундах. Их результаты:  
```python
scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('Tom', 8), ('Tom', 9), ('Tom', 8)]
```  
Создайте словарь, где ключами будут имена игроков, а значениями — их суммарные очки.  
"""
scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), 
           ('John', 7), ('John', 8), ('John', 5), 
           ('Tom', 8), ('Tom', 9), ('Tom', 8)]
total_scores = {}
for player, score in scores:
    if player in total_scores:
        total_scores[player] += score
    else:
        total_scores[player] = score
print("Суммарные очки:")
for player, score in total_scores.items():
     print(f"{player}: {score} очков")


"""
---

### Задача 8: Статистика списка  
Дан список чисел:  
```python
numbers = [10, 3, 5, 9, 18, 3, 0, 7]
```  
Напишите функцию, которая возвращает максимальное значение, сумму и среднее арифметическое чисел в списке.  
"""
numbers = [10, 3, 5, 9, 18, 3, 0, 7]
def list_statistics(numbers):
    if not numbers:
        return None, None, None
    max_value = max(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return max_value, total_sum, average
numbers = [10, 3, 5, 9, 18, 3, 0, 7]
max_val, total_sum, avg = list_statistics(numbers)
print(f"Максимальное значение: {max_val}")
print(f"Сумма чисел: {total_sum}")
print(f"Среднее арифметическое: {avg}")

"""
---

### Задача 9: Длинные и короткие слова  
Дан список слов:  
```python
word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]
```  
Напишите программу, которая определяет самое длинное и самое короткое слово в списке.  
"""
word_list = ["apple", "airplane", "carrot", "elephant", "guitar", "moonlight"]

longest_word = max(word_list, key=len)

shortest_word = min(word_list, key=len)

print("Самое длинное слово:", longest_word)
print("Самое короткое слово:", shortest_word)
"""
---

### Задача 10: Фильтрация по частоте  
Дан список чисел:  
```python
number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 1, 5, 3]
```  
Создайте новый список, содержащий только числа, которые встречаются в оригинальном списке не менее трёх раз.  
"""
number_list = [5, 8, 2, 7, 3, 5, 6, 9, 2, 4, 8, 7, 1, 5, 3]
result = []

for num in number_list:
    if number_list.count(num) >= 3 and num not in result:
        result.append(num)

print(result)
"""
---

### Задача 11: Второй лучший результат  
Дан список результатов экзамена:  
```python
exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]
```  
Напишите программу, которая определяет второй по величине результат в списке.  
"""
exam_results = [23, 78, 96, 32, 53, 67, 23, 98, 33, 38, 45, 39, 86, 12, 43, 45]

max_result = max(exam_results) 
second_max = 0 

for score in exam_results:
    if score != max_result and score > second_max:
        second_max = score

print("Второй по величине результат:", second_max)

"""
--- 
"""
