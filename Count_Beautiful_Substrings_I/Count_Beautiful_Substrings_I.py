

def beautifulSubstrings(s: str, k: int) -> int:
    satisfied_equal_pairs = {i for i in range(501) if (i * i) % k == 0}

    vowels_consonants_pairs = {(0, 0)}
    cur_num_vowels = cur_num_consonants = res = 0
    for c in s:
        if c in "ueoai": cur_num_vowels += 1
        else: cur_num_consonants += 1
        
        min_num = min(cur_num_vowels, cur_num_consonants, 500)
        for i in range(min_num + 1):
            if i in satisfied_equal_pairs and \
                (cur_num_vowels - i, cur_num_consonants - i) in vowels_consonants_pairs:
                res += 1
        vowels_consonants_pairs.add((cur_num_vowels, cur_num_consonants))

    return res


if __name__ == "__main__":
    print(beautifulSubstrings("baeyh", 2 ))
