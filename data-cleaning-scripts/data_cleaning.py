import pandas as pd
""" Performing basic cleaning function using python to:
- Remove duplicate rows, drop rows with NaN values, and strip whitespace from string columns
"""
def data_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.dropna(how='all')
    for col in df.select_dtypes (include='object').columns:
        df[col] = df[col].str.strip()
        return df

if __name__ == "__main__":
    raw_data = pd.DataFrame({
        "name": [" Alexander ", "Cynthia", "David", "Amaka ", "David"],
        "age": [28, 33, 50, 22, 50],
        "course": [" Data Engineering ", "Machine Learning ", "Artificial Intelligence", "DevOps", "Artificial Intelligence"]
})

data_cleaned = data_clean(raw_data)
print(data_cleaned)
