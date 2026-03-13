'''
    Exercise 10: Map, Filter, Reduce - Data Pipeline
'''
from functools import reduce
import itertools

if __name__ == "__main__":
    transactions = [
        {"id": 1, "amount": 100, "type": "debit", "category": "food"},
        {"id": 2, "amount": 200, "type": "credit", "category": "salary"},
        {"id": 3, "amount": 50, "type": "debit", "category": "entertainment"},
        {"id": 4, "amount": 150, "type": "credit", "category": "salary"},
        {"id": 5, "amount": 75, "type": "debit", "category": "transport"},
        {"id": 6, "amount": 120, "type": "debit", "category": "food"},
        {"id": 7, "amount": 300, "type": "credit", "category": "salary"},
        {"id": 8, "amount": 60, "type": "debit", "category": "utilities"},
        {"id": 9, "amount": 90, "type": "debit", "category": "shopping"},
        {"id": 10, "amount": 250, "type": "credit", "category": "salary"},
        {"id": 11, "amount": 40, "type": "debit", "category": "food"},
        {"id": 12, "amount": 180, "type": "credit", "category": "salary"},
        {"id": 13, "amount": 30, "type": "debit", "category": "entertainment"},
        {"id": 14, "amount": 220, "type": "credit", "category": "salary"},
        {"id": 15, "amount": 110, "type": "debit", "category": "transport"},
        {"id": 16, "amount": 70, "type": "debit", "category": "food"},
        {"id": 17, "amount": 400, "type": "credit", "category": "salary"},
        {"id": 18, "amount": 55, "type": "debit", "category": "utilities"},
        {"id": 19, "amount": 95, "type": "debit", "category": "shopping"},
        {"id": 20, "amount": 260, "type": "credit", "category": "salary"}
    ]
    
    debit_transacs = list(filter(lambda x: x['type']=='debit',transactions)) #1. debit only transacs
    print("Debit transactions:\n",*debit_transacs)
    
    amounts_list = list(map(lambda x: x['amount'],transactions)) #2. list of all the amounts
    print("\nAmounts list:\n",*amounts_list)
    
    total_debit = reduce(lambda x,y: x+y,list(map(lambda x: x['amount'],debit_transacs)),0) #3. total amount in debits
    print("\nTotal amount in debit transactions:\n",total_debit)
    
    print("Category wise total debit:")
    category_totals = {}
    for category,data in itertools.groupby(transactions,lambda x: x['category']):
        if category not in category_totals.keys():
            category_totals[category] = 0
        category_totals[category] += list(data)[0]['amount']
    
    print(category_totals)