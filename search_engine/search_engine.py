import re

def search(documents, query):
    results = []
    for doc in documents:
        pattern = r'\b{}\b'.format(re.escape(query.strip('!?.,').lower()))
        matches = re.findall(pattern, doc['text'].lower())
        if matches:
            results.append((doc['id'], len(matches)))
    results.sort(key=lambda x: x[1], reverse=True)
    return [doc_id for doc_id, _ in results]