# # Write your code here
"""
Objectives
Write a program that will work endlessly to make coffee for all interested
persons until the shutdown signal is given.
Introduce two new options: "remaining" and "exit".

Do not forget that you can be out of resources for making coffee.
If the coffee machine doesn't have enough resources to make coffee,
the program should output a message that says it can't make a cup of coffee.

And the last improvement to the program at this step —
if the user types "buy" to buy a cup of coffee and then changes his mind,
they should be able to type "back" to return into the main cycle.
Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit):
> fill

Write how many ml of water do you want to add:
> 1000
Write how many ml of milk do you want to add:
> 0
Write how many grams of coffee beans do you want to add:
> 0
Write how many disposable cups of coffee do you want to add:
> 0

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
1050 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
> buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit):
> take

I gave you $564

Write action (buy, fill, take, remaining, exit):
> remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
0 of money

Write action (buy, fill, take, remaining, exit):
> exit
"""

class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

     #1 espresso
    espresso_w = 250
    espresso_b = 16
    espresso_mo = 4

    #2 latte
    latte_w = 350
    latte_b = 20
    latte_mi = 75
    latte_mo = 7

    #3 cappuccino
    cappuccino_w = 200
    cappuccino_b = 12
    cappuccino_mi = 100
    cappuccino_mo = 6
        
    def __init__(self):
        self.again = True  

    def actions(self):
        while self.again:
            action = input("\nWrite action (buy, fill, take, remaining, exit):")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                self.again = False
            else:
                print("wrong input")
    def buy(self):
        buy_what = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if buy_what == "1":
            if self.water <= self.espresso_w:
                print("Sorry, not enough water!")
            elif self.beans <= self.espresso_b:
                print("Sorry, not enough beans!")
            elif self.cups == 0:
                print("Sorry, not enough cups!")
            else:
                self.water = self.water - self.espresso_w
                self.beans = self.beans - self.espresso_b
                self.money = self.money + self.espresso_mo
                self.cups = self.cups - 1
                print("I have enough resources, making you a coffee!")
        elif buy_what == "2":
            if self.water <= self.latte_w:
                print("Sorry, not enough water!")
            elif self.beans <= self.latte_b:
                print("Sorry, not enough beans!")
            elif self.milk <= self.latte_mi:
                print("Sorry, not enough milk!")
            elif self.cups == 0:
                print("Sorry, not enough cups!")
            else:
                self.water = self.water - self.latte_w
                self.beans = self.beans - self.latte_b
                self.milk =  self.milk - self.latte_mi
                self.money = self.money + self.latte_mo
                self.cups = self.cups - 1
                print("I have enough resources, making you a coffee!")
        elif buy_what == "3":
            if self.water <= self.cappuccino_w:
                print("Sorry, not enough water!")
            elif self.beans <= self.cappuccino_b:
                print("Sorry, not enough beans!")
            elif self.milk <= self.cappuccino_mi:
                print("Sorry, not enough milk!")
            elif self.cups == 0:
                print("Sorry, not enough cups!")
            else:
                self.water = self.water - self.cappuccino_w
                self.beans = self.beans - self.cappuccino_b
                self.milk =  self.milk - self.cappuccino_mi
                self.money = self.money + self.cappuccino_mo
                self.cups = self.cups - 1
                print("I have enough resources, making you a coffee!")
                       
                        
        else:
            self.actions()
                

    def fill(self):
        self.water = self.water + int(input("Write how many ml of water do you want to add:"))
        self.milk = self.milk + int(input("Write how many ml of milk do you want to add:"))
        self.beans = self.beans + int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups = self.cups + int(input("Write how many disposable cups of coffee do you want to add:"))
          
    def take(self):
        print("I gave you $%d\n" %(self.money))
        self.money = 0
        
    def remaining(self):
        self.print_actions()
        
    def print_actions(self):
        print ("""
        The coffee machine has:
        %d of water
        %d of milk
        %d of coffee beans
        %d of disposable cups
        %d of money""" %(self.water, self.milk, self.beans, self.cups, self.money))

coffee_machine = CoffeeMachine()
coffee_machine.actions()
    
    
