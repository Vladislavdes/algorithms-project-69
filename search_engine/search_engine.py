import re

def search(documents, query):
    result = []
    for doc in documents:
        pattern = r'\b{}\b'.format(re.escape(query.strip('!?.,')))
        matches = re.findall(pattern, doc['text'].lower())
        if matches:
            result.append(doc['id'])
    return result

