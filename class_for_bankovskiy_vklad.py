
class Bank:
    def __init__(self,start_money,years,percents):
        self.start_money=start_money
        self.years=years
        self.percents=percents
    
    def get_money(self):  
        for i in range(self.years):
            self.start_money=self.start_money+self.start_money*self.percents
        return self.start_money
    
bank=Bank(1000,2,0.1) 
final_money=bank.get_money()  
print(int(final_money))
