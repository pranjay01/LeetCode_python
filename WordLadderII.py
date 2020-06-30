beginWord="hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        
        if endWord not in wordList:
            return []
        res=[[beginWord]]
        wrdL=len(wordList)
        for List in res:
            val=List[-1]
            while val is not endWord:
                count=1
                l=len(val)
                i=0
                while i<wrdL:
                    string=wordList[i]
                    if string in List:
                        i+=1
                        continue
                    if self.checkDiff(string,val,l)==1:
                        if count>1:
                            tmp=List[:]
                            tmp.pop()
                            tmp.append(string)
                            res.append(tmp)
                            wordList.pop(i)
                            wrdL-=1
                        else:
                            List.append(string)
                            wordList.pop(i)
                            wrdL-=1
                            count+=1
                    else:
                        i+=1
                val=List[-1]
                
        return res

    def checkDiff(self,string,val,l):
        #l1=len(string)
        count=0
        #if l1==l2:
        for i in range(l):
            if not string[i]==val[i]:
                count+=1
        return count

print(Solution().ladderLength(beginWord,endWord,wordList))