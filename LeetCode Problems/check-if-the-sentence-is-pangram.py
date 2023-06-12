class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        library = defaultdict(int)
        for i in sentence:
            library[i] = 1 
        return len(library) == 26