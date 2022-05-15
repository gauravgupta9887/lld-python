class Solution:
    	# @param A : string
	# @param B : string
	# @return an integer
    def __init__(self):
        self.ans = False
    def recurse(self,pos_A,pos_B,A,B):
        if pos_A==len(A) and (pos_B==len(B) or (pos_B==len(B)-1 and B[pos_B]=='*')):
            self.ans = True
            return
        if pos_B == len(B):
            return
        if pos_A == len(A):
            return 
        if A[pos_A]==B[pos_B] or B[pos_B]=='?':
            self.recurse(pos_A+1,pos_B+1,A,B)
        elif A[pos_A]!=B[pos_B] and B[pos_B]=='*':
            b_pos  = pos_B
            while b_pos<len(B):
                if B[b_pos] not in {'*'}:
                    break
                b_pos += 1
            if b_pos==len(B):
                self.ans = True
                return 
            for pos in range(pos_A,len(A)):
                if B[b_pos]=='?' or A[pos] == B[b_pos]:
                    self.recurse(pos+1,b_pos+1,A,B)
            if pos == len(A):
                return
        elif A[pos_A]!=B[pos_B]:
            return 
    def isMatch(self, A, B):
        self.recurse(0,0,A,B)
        return self.ans
    
x = Solution()
print(x.isMatch("bacb", "b**c*?*"))