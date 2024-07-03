import re

def search(array, word):
    if array == []:
        return []
    result = []
    for i in array:
        if re.search(r'\b{}\b'.format(word), i['text']):
            result.append(i['id'])
    return result
        