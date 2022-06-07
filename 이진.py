#리트코드 278
# 자주 틀리는 것.
# 왼쪽이 오른쪽을 넘어갔을때 디테일.
# 왜 저래야만 하는가?

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (right + left) // 2
            if not isBadVersion(mid):
                left = mid + 1 
            else:
                right = mid
                
        return left
            

        
