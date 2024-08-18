other_words = []
def single_root_words(*other_words, root_word='ход'):
    same_words = []
    for word in other_words:
        if word. lower() in root_word. lower() or root_word. lower() in word. lower():
            same_words.append(word)
    return same_words
    print(same_words)


result1 = single_root_words("ВыхОд", "маятник", "переход", "сахар", "наХодка", "лето", "ход")
print(result1)
result2 = single_root_words( "жАровня", "солнце", "поЖар", "сходняк", "жаРкое", root_word="жар")
print(result2)
