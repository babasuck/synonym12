def get_synonym(word):
    with open('synonyms.txt', 'r') as f:
        for line in f:
            w, syn = line.strip().split(' - ')
            if w == word:
                return syn
        return None

def add_synonym(word, syn):
    with open('synonyms.txt', 'r') as f:
        f.write(f'{word} - {syn}\n')

word = input('Enter a word to find a synonym: ')
synonym = get_synonym(word)

if synonym:
    print(f'The synonym of {word} is {synonym}')
    response = input(f'Is {synonym} OK? (y/n) ')
    if response.lower() == 'n':
        new_synonym = input(f'Enter a new synonym for {word}: ')
        add_synonym(word, new_synonym)
        print(f'{new_synonym} has been added as a synonym for {word}')
    else:
        print('OK, done!')
else:
    print(f'Sorry, there is no synonym for {word} in our records.')
    new_synonym = input(f'Enter a new synonym for {word}: ')
    add_synonym(word, new_synonym)
    print(f'{new_synonym} has been added as a synonym for {word}')