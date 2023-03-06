class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions=defaultdict(list)
        for i in range(len(s)):
            partitions[s[i]].append(i)
        ls=[[partitions[i][0],partitions[i][-1]] for i in partitions]
      
        arranged=[ls[0]]
        for i in range(len(ls)):
            if ls[i][0]>arranged[-1][1]:
                arranged.append(ls[i])
            else:
                arranged[-1][1]=max(ls[i][1],arranged[-1][1])
            
        arranged=[arranged[i][1]+1-arranged[i][0] for i in range(len(arranged))]
        
        return arranged

