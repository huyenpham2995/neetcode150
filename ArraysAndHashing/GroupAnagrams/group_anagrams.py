from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) == 0: return [[""]]

    anagrams_dict = defaultdict(list)

    for word in strs:
        sorted_word = "".join(sorted(word))
        # if sorted_word in anagrams_dict.keys():
        #     anagrams_dict[sorted_word].append(word)
        # else:
        #     anagrams_dict[sorted_word] = [word]
        anagrams_dict[sorted_word].append(word)

    return [anagrams_group for anagrams_group in anagrams_dict.values()]