import pandas as pd
import random
from faker import Faker
from datetime import datetime
fake = Faker()
Faker.seed(0)

# Generate data
data = []
customers = [fake.name() for _ in range(100)]

# 100 unique customers
categories = ['Fruit', 'Dairy', 'Bakery', 'Meat', 'Personal Care', 'Beverages', 'Vegetables']
products = {
    'Fruit': ['Apple', 'Banana', 'Orange'],
    'Dairy': ['Milk', 'Cheese', 'Yogurt'],
    'Bakery': ['Bread', 'Cake', 'Croissant'],
    'Meat': ['Chicken Breast', 'Beef Steak', 'Pork Chop'],
    'Personal Care': ['Shampoo', 'Soap', 'Toothpaste'],
    'Beverages': ['Water', 'Juice', 'Soda'],
    'Vegetables': ['Carrot', 'Broccoli', 'Spinach']
}

for i in range(1000):
    if i<500:
        name = random.choice(customers)
    elif i>=500:
        name=fake.name()
    
    date = fake.date_this_year()
    if (300<=i) and (i<500):
        date=fake.date_between_dates(date_start=datetime(2023,1,1), date_end=datetime(2024,12,31))
    category = random.choice(categories)
    product = random.choice(products[category])
    data.append([name, date, product, category])

# Create DataFrame
df = pd.DataFrame(data, columns=['Customer Name', 'Date', 'Product', 'Product Category'])

# Save to CSV
df.to_csv('supermarket_dataset.csv', index=False)
