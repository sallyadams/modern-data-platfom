import pandas as pd

data = {
    "user_id": [1, 2, 3],
    "amount": [100, 200, 150]
}

df = pd.DataFrame(data)
df.to_csv("transactions.csv", index=False)

print("Sample data generated")
