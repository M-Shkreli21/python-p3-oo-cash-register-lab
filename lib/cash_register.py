#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.prior_transaction = 0
        self.items = []
        
  def add_item(self, name, price, quantity = 1):
        self.prior_transaction = price * quantity
        self.total += self.prior_transaction
        for i in range(quantity):
              self.items.append(name)
  
  def apply_discount(self):
        if (self.discount > 0):
              discount_percent = (100 - float(self.discount)) / 100
              self.total = int(self.total * discount_percent)
              print(f"After the discount, the total comes to ${self.total}.")
        else:
              print("There is no discount to apply.")
  
  def void_last_transaction(self):
        self.total -= self.prior_transaction
  
