from nltk import pos_tag, download

def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])

def is_verb(word):
    if not word:
        return False
    try:
        pos_info = pos_tag([word])
    except LookupError:
        download('averaged_perceptron_tagger')
        pos_info = pos_tag([word])
    return pos_info[0][1].startswith('VB')

def is_noun(word):
    if not word:
        return False
    try:
        pos_info = pos_tag([word])
    except LookupError:
        download('averaged_perceptron_tagger')
        pos_info = pos_tag([word])
    return pos_info[0][1].startswith('NN')

def is_reserved_name(name):
    return (name.startswith('__') and name.endswith('__'))

def is_this_language(filename, language):
    if language == "python":
        return is_python(filename)
    else:
        return False

def is_python(filename):
    ext = filename.split(".")[-1]
    return ext == "py"

