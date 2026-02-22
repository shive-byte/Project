import pandas as pd
import random
from faker import Faker
fake = Faker()
Faker.seed(0)
data=[]
names=[fake.name() for _ in range(500)]
for i in range(9995):
    name=random.choice(names)
    data.append(name)
df=pd.DataFrame(data,columns=['Name'])
df.to_excel("super nname.xlsx")
