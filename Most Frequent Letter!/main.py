#🔎 Find the most frequently used word!

#📦 Variables

random_words = [
    'apple', 'banana', 'orange', 'mango', 'grape', 'pineapple',
    'amethyst', 'diamond', 'sapphire', 'ruby', 'opal', 'emerald',
    'chicken', 'cow', 'horse', 'rabbit', 'lion', 'tiger'
]

#⚙️ Functions

def most_frequent_word(word):
    print('-' * 50)
    print(f'🔎 Checking Word: {word}')
    word = word.lower()

    # Count Letters

    dict_count = {}
    for letter in word:
        if letter not in dict_count:
            count = word.count(letter)
            dict_count[letter] = count

    # Print Reports

    for letter, count in dict_count.items():
        print(f'{letter} used this many {count} times.')

    # Find Max Count Letters

    max_count = max(dict_count.values())
    print(max_count)

    # Report Results


#🎯 Main

for word in random_words:
    most_frequent_word(word)