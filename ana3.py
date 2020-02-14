class BankAccount:
    def __init__(self, accountnumber, balance=0):
        self.account_number = accountnumber
        self.balance = balance

    def Deposite(self, amount):
        self.balance += amount
        balance = self.balance
        
        print(balance)
        return self.balance
    
    def Withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            balance = self.balance
            print(balance)
            return True
        else:
            return False

    def checking(self, amount):
        return self.balance

bankaccount1 = BankAccount("lool",300)
bankaccount1.Withdraw(100)

bankaccount2 = BankAccount('make me great again', 2000)
bankaccount2.Deposite(200)

class Nogermans:
    def __init__(self, health, weapon, enemyweapon, enemyhealth, deathplayer = 0, deathenemy= 0):
        self.health = health
        self.weapon = weapon
        self.enemyweapon = enemyweapon
        self.deathplayer = deathplayer
        self.deathenemy = deathenemy
        self.enemyhealth = enemyhealth

    def lifetotal_battle(self, health, enemyweapon, deathplayer):
        if self.enemyweapon == 'spear' or self.enemyweapon == 'tomahawk':
            dmg = 20
            if dmg >= self.health:
                return death + 1 
            else:
                self.health -= dmg
                health = self.health
                print(health)
                return health
        if self.enemyweapon == 'axe' or self.enemyweapon == 'cannon':
            dmg = 25
            if dmg >= self.health:
                return death + 1 
            else:
                self.health -= dmg
                self.health = health
                return health
        if self.enemyweapon == 'sword' or self.enemyweapon == 'bow':
            dmg = 15
            if dmg >= self.health:
                return death + 1 
            else:
                self.health -= dmg
                self.health = health
                return health

firstbattle = Nogermans(100,'sword','spear', 20)
firstbattle.lifetotal_battle(100,'spear',0)


