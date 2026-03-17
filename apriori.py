import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# 1. Define a small, simple dataset (List of Transactions)
# Each list is a "basket" of items bought by a customer
dataset = [
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread'],
    ['Milk', 'Butter'],
    ['Milk', 'Bread', 'Butter', 'Jam'],
    ['Bread', 'Jam']
]

# 2. Convert the list into a one-hot encoded format (True/False)
# The Apriori algorithm needs a table where each column is an item
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

print("--- Data Table (One-Hot Encoded) ---")
print(df)
print("\n")

# 3. Apply Apriori Algorithm
# min_support=0.5 means the item must appear in at least 50% of transactions
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

print("--- Frequent Itemsets ---")
print(frequent_itemsets)
print("\n")

# 4. Generate Association Rules
# We use 'lift' to see if buying Item A actually increases the chance of buying Item B
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

print("--- Association Rules ---")
# Selecting important columns for clarity
result = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
print(result)

# Example Interpretation:
# If 'Milk' and 'Bread' have a high lift/confidence, it means they are frequently bought together.
