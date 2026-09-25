class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary where default values are empty lists
        anagram_map = defaultdict(list)

        for word in strs:
            # Sort characters to form a canonical key: e.g., "pots" -> "opst"
            key = "".join(sorted(word))
            
            # Group the original word under its sorted key
            anagram_map[key].append(word)
           
            # Return the grouped anagram lists
        return list(anagram_map.values())

        