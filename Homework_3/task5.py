'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
"мягкий"]
Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
'''


def get_jokes(amount: int):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    import random
    all_jokes = []
    for i in range(amount):
        new_joke = ' '.join([random.choice(nouns), random.choice(adverbs), random.choice(adjectives)])
        all_jokes.append(new_joke)
    return all_jokes


if __name__ == "__main__":
    print(get_jokes(2))
