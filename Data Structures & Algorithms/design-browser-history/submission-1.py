class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.history.append(homepage)
        self.currentpos = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.currentpos+1]
        self.history.append(url)
        self.currentpos+=1

    def back(self, steps: int) -> str:
        if self.currentpos - steps<=0:
            self.currentpos=0
            return self.history[0]
        else:
            self.currentpos-=steps
            return self.history[self.currentpos]

    def forward(self, steps: int) -> str:
        
        if steps+self.currentpos>=len(self.history):
            self.currentpos = len(self.history)-1
            return self.history[len(self.history)-1]
        else:
            self.currentpos+=steps
            return self.history[self.currentpos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)