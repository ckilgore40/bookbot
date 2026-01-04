def word_count(text):
    words = text.split()
    return f"Found {len(words)} total words"

def occorances(text):
    occurance_dict = {}
    words = text.split()
    for word in words:
        for letter in word.lower():
            if letter in occurance_dict:
                occurance_dict[letter] += 1
            else:
                occurance_dict[letter] = 1
    return occurance_dict

def sort_on(letter_count):
    return letter_count["num"]

def sorted_dict(dict):
    sorted_list = []
    for letter in dict:        
        sorted_list.append({"char": letter, "num": dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list