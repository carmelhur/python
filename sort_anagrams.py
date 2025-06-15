
def sort_anagrams(list_of_strings):
    from collections import defaultdict

    # מילון שבו המפתח הוא tuple של האותיות הממוינות, והערך הוא רשימת מילים תואמות
    anagrams = defaultdict(list)

    for word in list_of_strings:
        # יוצרים מפתח לפי האותיות הממוינות
        key = tuple(sorted(word))
        anagrams[key].append(word)

    # שומרים על סדר ההופעה המקורי
    seen = set()
    result = []
    for word in list_of_strings:
        key = tuple(sorted(word))
        if key not in seen:
            result.append(anagrams[key])
            seen.add(key)

    return result
