
def count_words(text):
    word_count = len(text.split())
    return word_count

def count_characters(text):
    lower_text = text.lower()
    letter_count = {}
    for letter in lower_text:
        letter_count[letter] = 0
    
    for letter in lower_text:
        letter_count[letter] += 1
        
    return letter_count

def sort_on(items):
    return items["num"]

def letter_dictionaries(letter_count):
    letters = []
    for letter in letter_count:
        letter_dict = {"char":letter, "num":letter_count[letter]}
        letters.append(letter_dict)
    letters.sort(key=sort_on)
    return letters