from collections import deque
class Solution:
    def minLength(self, s: str) -> int:
        st=collections.deque()
        for i in s:
            if not st:
                st.append(i)
            elif ((st[-1]=='A' and i=='B')or(st[-1]=='C'and i=='D')):
                st.pop()
            else:
                st.append(i)
        return len("".join(st))
