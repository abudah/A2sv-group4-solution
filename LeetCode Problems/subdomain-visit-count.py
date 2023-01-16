class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomains=defaultdict(int)
        for i in cpdomains:
            numOfVisits=int(i.split()[0])
            subDomain=i.split()[1].split('.')
            j=0
            while j<len(subDomain):
                subd=subDomain[j:]
                subdomains[".".join(subd)]+=numOfVisits
                j+=1
        sbdVisits=[]
        for key,values in subdomains.items():
            sbdVisit=str(values)+" "+key
            sbdVisits.append(sbdVisit)
        return sbdVisits