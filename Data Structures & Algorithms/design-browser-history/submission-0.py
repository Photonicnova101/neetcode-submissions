class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = [homepage]
        self.position = 0

    def visit(self, url: str) -> None:
        numToPop = len(self.browser) - self.position-1
        while numToPop>0:
            self.browser.pop()
            numToPop-=1
        self.browser.append(url)
        self.position = len(self.browser)-1

    def back(self, steps: int) -> str:
        if steps< self.position:
            self.position = self.position - steps
        else:
            self.position = 0
        return self.browser[self.position]

    def forward(self, steps: int) -> str:
        if steps>len(self.browser)-self.position-1:
            self.position = len(self.browser)-1
        else:
            self.position = self.position + steps
        return self.browser[self.position]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)