import numpy as np
from scipy.optimize import fsolve


class expense():
    def __init__(self, values):
        self.monthlyexp = values

    def expand(self):
        vals = np.ones(len(self.monthlyexp)*12)
        for i in range(len(self.monthlyexp)*12):
            vals[i] = self.monthlyexp[int(i/12)]
        return vals

class income(Expense):
    def __init__(self, values, tithing):
        expense.__init__(self, values)
        self.tithing = tithing
    def expand(self):
        vals = np.ones(len(self.monthlyexp)*12)
        for i in range(len(self.monthlyexp)*12):
            vals[i] = self.monthlyexp[int(i/12)]/12*(1-self.tithing)
        return vals

class Simulation():
    def __init__(self):
        self.exps = []
        self.incs = []
    def Expense(self, values):
        self.exps.append(expense(values))
    def Income(self, values):
        self.incs.append(income(values, tithing=.1))
    def test1(self):
        totinc = np.zeros(len(self.incs[0].expand()))
        for inc, i in self.incs:
            totinc[i] = 

salary = np.array([80000, 100000, 200000])
Rents = np.array([1600, 2000, 0])

rent = expense(Rents)
job1 = income(salary, .1)

print(rent.expand())
print(job1.expand())