class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        col=0
        row=0
        list=[]
        result=[]
        for i in range(len(mat)+len(mat[0])-1):
            x=row
            y=col
            list.clear()
            while(x>=0 and y<len(mat[0])):
                  list.append(mat[x][y])
                  x-=1
                  y+=1
            if row==len(mat)-1:
                col+=1
            if row<len(mat)-1:
                row+=1
            if i%2==1:
               list.reverse()
            for j in range(len(list)):
                 result.append(list[j])

        return result