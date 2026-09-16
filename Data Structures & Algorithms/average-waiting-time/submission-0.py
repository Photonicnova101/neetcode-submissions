class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitingtime = 0
        currenttime = 0
        for arrival,time in customers:
            currenttime=max(arrival,currenttime)
            waitingtime+=currenttime+ time - arrival
            currenttime+=time
        return waitingtime/len(customers)

            

