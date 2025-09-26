def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def get_num_words(filepath):
    return len(get_book_text(filepath).split())

def get_characters(filepath):
    with open(filepath) as f:
        raw_text = f.read()
        lowered_text = raw_text.lower()
        chars = set(lowered_text)
        char_totals = dict()
        for char in chars:
            char_totals[char] = lowered_text.count(char)
        return char_totals
        #returns dictionary of each character
def sort_on(items):
    return items["num"]

def get_ordered_pairs(dictionary):
    
    ordered_pairs = list()
    for dic in dictionary:
        ordered_pairs.append({"char" : dic, "num" :dictionary.get(dic)})
    ordered_pairs.sort(reverse=True, key=sort_on)
    return ordered_pairs

def header(filepath):
    return f"============ BOOKBOT ============\n Analyzing book found at{filepath}..."

def book_bot(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(filepath)} total words")
    print("--------- Character Count -------")
    words_dict = get_characters(filepath)
    sorted_dictionaries = get_ordered_pairs(words_dict)
    for dict in (sorted_dictionaries):
        if dict.get("char").isalpha():
            print(f"{dict.get("char")}: {dict.get("num")}")
    #runs bookbot on sepcified file
