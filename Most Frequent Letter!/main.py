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
        if count > 1:
            print(f'{letter} used this many {count} times.')
        else:
            print(f'{letter} used this many {count} time.')
    # Find Max Count Letters

    max_count = max(dict_count.values())
    max_letters = []

    for letter, count in dict_count.items():
        if count == max_count:
            max_letters.append(letter)

    # Report Results
    print(f'The most frequently used letter is {max_letters}.'
          f'And it is used {max_count} times.')

    return max_letters, max_count

#🎯 Main

for word in random_words:
    results = most_frequent_word(word)