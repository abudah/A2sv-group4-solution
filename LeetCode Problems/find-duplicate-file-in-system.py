class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicatedFiles=defaultdict(list)
        for i in paths:
            i=i.split(' ')
            path=i[0]
            for n in range(1,len(i)):
                endOfFile=i[n].index('(')
                content=i[n][endOfFile+1:-1]
                duplicatedFiles[content]+=[path+'/'+str(i[n][:endOfFile])]

        duplicates=[]        
        for key,values in duplicatedFiles.items():
            if len(values)>=2:
                duplicates.append(values)

        return duplicates