""" Data loading process: 
storing data in both CSV and parquet file format 
"""
import pandas as pd

def save_to_csv(df:pd.DataFrame, filename:str) -> None:
    df.to_csv(filename, index = False)
    print(f"Data saved to {filename}")

def save_to_parquet(df:pd.DataFrame, filename:str) -> None:
    df.to_parquet(filename, engine="pyarrow", index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    raw_data = pd.DataFrame({
	"name": ["Alexander", "Bob", "David", "Nancy"],
	"age": [17, 30, 34, 50],
	"gender": ["Male", "Female", "Male", "Female"]
})

data_loading1 = save_to_csv(raw_data, "raw_data.csv")
data_loading2 = save_to_parquet(raw_data, "raw_data.parquet")

