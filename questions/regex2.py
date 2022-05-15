class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        n1 = len(A)
        n2 = len(B)
        if not n1 and not n2:
            return 1
        if not n2:
            return 0
        i = 0
        j = 0
        star = None
        curr_i = None
        #print('HERE1')
        while i < n1:
            if j < n2 and (A[i] == B[j] or B[j] == '.'):
                i += 1
                j += 1
            elif j < n2 and B[j] == '*':
                #print('HERE2')
                star = j
                j += 1
                curr_i = i
            elif star is not None:
                #print('HERE3')
                curr_i += 1
                i = curr_i
                j = star + 1
            else:
                #print('HERE4')
                if j==n2:
                    return 0
                if j<n2 and B[j+1]!='*':
                    return 0
                j = j+1

                
        while j < n2 and B[j] == '*':
            j += 1
        #print('HERE5')
        return 1 if j == n2 else 0


x = Solution()
print(x.isMatch("a", "b"))