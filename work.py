

class Worker: 
    
    #constructor of Worker with default role dev and default pay 1500

    def __init__(self, name: str, role: str ='dev', pay: int = 1500):
        
        self.name = name
        self.role = role
        self.pay = pay
    
    #raise the pay of the worker
    
    def raise_pay(self, amount : float):
        
        self.pay = int(self.pay * amount)
    
    #print name, role and pay of the worker

    def __str__(self):
        return f"{self.name} with a role of {self.role} is paid {self.pay}"
    
#subclass Manager of worker

class Manager(Worker):
    
    #override constructor of worker with default pay 2000 and with role Manager

    def __init__(self, name: str, pay = 2000):
        
        super().__init__(name, "Manager",pay)
    
    #raise pay of the Manager by worker  bonus 


    def raise_pay(self, amount : float , bonus : float):
        
        super().raise_pay(bonus)

#class Department of workers
class Department:

    #constructor method for Department with name and workers list(default empty List)

    def __init__(self, name: str, workers = []):

        self.name = name
        self.workers = workers
    
    #add workers to workers list of Department

    def add_worker(self,*args):
            for worker in args:
                self.workers.append(worker)
    
    #raise the pay of all the workers of amount and amount+bonus for the manager

    def raise_all(self, amount : float , bonus : float):
        
        for worker in self.workers:
            if isinstance(worker,Manager):
                worker.raise_pay(amount, bonus)
            else: 
                worker.raise_pay(amount)

    #get total workers of Department    
    
    def get_workers_number(self): 

        return len(self.workers)
    
    #print Department name with total number of workers, print the manager and a list of the workers

    def __str__(self):

        res = f" Dev: {self.name} with {self.get_workers_number()} workers \n"
        
        for worker in self.workers:
             if(isinstance(worker,Manager)):
                res += f"{worker.name} is the manager with a pay of {worker.pay}\n"
        
        for index, worker in enumerate(self.workers):
            if( not isinstance(worker,Manager)):
                res += f"{index + 1}. {worker.name} with a role of {worker.role} and a pay of {worker.pay}$\n"
        
        return res
    
def main():
    
    m1 = Manager("Stefano Giardino", 12000)
    m2 = Manager("Vincenzo Caracciolo",13000)

    w1 = Worker("Giuseppe Verdi")
    w2 = Worker("Andrea Pirlo")
    w3 = Worker("Paulo Dybala")
    w4 = Worker("Antonio Ricci")
    w5 = Worker("Christian De Sica","devops",1300)
    w6 = Worker("Francesco Doe", "operation engineer")
    w7 = Worker("Terence Hill","Cloud Architect",7000)
    w8 = Worker("Chuck Norris", "operation engineer")
    w9 = Worker("Chuck Doe", "operation engineer")

    dev = Department("Dev",[m1, w1, w2, w3, w4])
    ops = Department("Ops", [w6, m2, w7, w8])

    print(dev)
    print(ops)

    print("add workers ... \n")
    
    dev.add_worker(w5,w6)
    ops.add_worker(w9)
    
    print(dev)
    print(ops)

    ops.raise_all(1.15, 2)

    print("raise workers ops ...\n")
    print(ops)


if __name__ == "__main__":
    main()


