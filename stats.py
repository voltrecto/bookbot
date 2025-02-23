def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    character_dict = {}
    for c in text.lower():
        character_dict[c] = character_dict.get(c, 0) + 1
    return character_dict

def sort_on(dict):
    return list(dict.values())[0]

def sort_dict(dict):
    sorted_list = []
    for k, v in dict.items():
        sorted_list.append({k: v})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list