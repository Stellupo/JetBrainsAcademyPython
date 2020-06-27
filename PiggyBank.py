class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money (self, deposit_dollars, deposit_cents):
        if deposit_cents + self.cents < 100:
            self.dollars += deposit_dollars
            self.cents += deposit_cents
            print(str(self.dollars) + " " + str(self.cents))
        elif deposit_cents + self.cents>=100:
            n = (deposit_cents + self.cents) // 100  #nombre de dollars gagnés à partir des centaines de cents
            print(n)
            self.dollars += int(n)+deposit_dollars
            self.cents = (deposit_cents + self.cents)%100 #reste des cents
            print((deposit_cents + self.cents)%100)
            print(str(self.dollars) + " " + str(self.cents))

test = PiggyBank(1,1)
test.add_money(500,500)