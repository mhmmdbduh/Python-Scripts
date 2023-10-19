class Solutions:
    def __init__(self) -> None:
        pass

    def groupAnagrams(self, strs:list[str]):
        anagrams = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            print(f"Sorting {word} to {sortedWord}")
            if sortedWord in anagrams:
                anagrams[sortedWord].append(word)
            else:
                anagrams[sortedWord] = [word]
        return anagrams.values()


strs = ["aba", "assd"]
s = Solutions()
print(s.groupAnagrams(strs))


