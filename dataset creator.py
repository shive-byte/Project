import pandas as pd
import random
from faker import Faker

fake = Faker()
Faker.seed(0)

# Generate data
data = []
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

for _ in range(1000):
    name = fake.name()
    date = fake.date_this_year()
    category = random.choice(categories)
    product = random.choice(products[category])
    data.append([name, date, product, category])

# Create DataFrame
df = pd.DataFrame(data, columns=['Customer Name', 'Date', 'Product', 'Product Category'])

# Save to CSV
df.to_csv('supermarket_dataset.csv', index=False)
