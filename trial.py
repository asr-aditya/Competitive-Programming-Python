def maxArr(A):
        if not A:
            return 0
        else:
            N = len(A)
            mx1, mx2, mx3, mx4 = [-10**15] * 4
            for i in range(N):
                mx1 = max(mx1, A[i] + i)
                mx2 = max(mx2, - A[i] + i)
                mx3 = max(mx3, A[i] - i)
                mx4 = max(mx4, -A[i] - i)
            ans = -10**15
            for i in range(N):
                ans = max(ans, mx1 - A[i] - i);
                ans = max(ans, mx2 + A[i] - i);
                ans = max(ans, mx3 - A[i] + i);
                ans = max(ans, mx4 + A[i] + i);
            return ans
A = [1,-2,-3,4,-4,-9]
maxArr(A)
