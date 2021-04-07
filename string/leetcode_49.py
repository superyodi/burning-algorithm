class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = dict()
        
        for str in strs:
            tmp = "".join(sorted(list(str)))
            
            if tmp in anagrams:
                anagrams[tmp].append(str)
            
            else:
                anagrams[tmp] = [str] 


        return list(anagrams.values())
                

        # 순서 상관없이 알파벳이 같아야함
        
    
