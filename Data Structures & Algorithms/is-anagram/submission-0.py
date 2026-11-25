class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s=defaultdict(int)
        hashmap_t=defaultdict(int)

        for i in s:
            if i in hashmap_s:
                hashmap_s[i]+=1
            else:
                hashmap_s[i]=1
        for j in t:
            if j in hashmap_t:
                hashmap_t[j]+=1
            else:
                hashmap_t[j]=1
        return hashmap_s==hashmap_t
        