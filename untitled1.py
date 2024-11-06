import pandas as pd

df = pd.read_excel("data.xlsx")

filtered_df = df[df["Age"] > 20]

gender_count = filtered_df["sex"].value_counts()

print("Filtered Data:")
print(filtered_df)

print("\nGender Counts:")
print(gender_count.to_string(index=False))
