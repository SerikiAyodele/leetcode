class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        Set = set()

        for i in count.values():
            if i not in Set:
                Set.add(i)
            else:
                return False
        return True