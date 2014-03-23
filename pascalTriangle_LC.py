'''
print pascal's triangle, LeetCode, ex: n=3
[
   [1]
  [1,1]
 [1,2,1]
]


Created on Dec 4, 2013

@author: Songfan
'''
def printPascal(result,n):
    print'['
    for i in range(1,n+1):
        spaceNum = n-i+1
        startIdx = i*(i-1)/2
        endIdx = (i+1)*i/2
        data = '['+','.join(result[startIdx:endIdx])+']'
        print ' '*spaceNum+data
    print ']'

def pascalTriangle(n):
    assert(n>=0 and isinstance(n,int)),'input error'
    result = []
    if n==1: result = ['1']
    else:
        currList = ['1','1']
        cnt = 2
        result = ['1','1','1']
        while(cnt<n):
            nextList = ['1']
            for i in range(len(currList)-1):
                nextList.append(str(int(currList[i])+int(currList[i+1])))
            nextList.append('1')
            currList = nextList
            result.extend(currList)
            cnt+=1
    printPascal(result,n)


n = 5
pascalTriangle(n)