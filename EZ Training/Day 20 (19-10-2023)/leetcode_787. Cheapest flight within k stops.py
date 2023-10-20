class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")]*n
        prices[src]=0
        for i in range(k+1):
            temp=prices.copy()
            for s,d,w in flights:
                if prices[s]!=float("inf") and prices[s]+w<temp[d]:
                    temp[d]=prices[s]+w
            prices=temp
        return -1 if prices[dst]==float("inf") else prices[dst]
