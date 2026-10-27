import pandas as pd

df = pd.read_csv("Quotes.csv")

print(df.head())
print("Total rows:", len(df))
print("Missing values:\n", df.isnull().sum())
df["Tags"] = df["Tags"].fillna("No Tags")

print("Missing values after cleaning:")
print(df.isnull().sum())
df.to_excel("Quotes.xlsx" , index = False)
Quot = df[
    ~(df["Tags"].str.contains("Inspirational" , case = False)) &
    (df["Tags"].str.contains("Life" , case= False))
]
print(Quot)
print(len(Quot))
Quot.to_excel("Filtered_Quotes.xlsx", index=False)
Author = df.groupby("Author")["Quote"].count()
print(Author)
Author = Author.sort_values(ascending=False)
Authors = Author.reset_index()
Authors.to_excel("Quote.xlsx" , index= False)
print(df.duplicated())
print(df.duplicated("Quote"))