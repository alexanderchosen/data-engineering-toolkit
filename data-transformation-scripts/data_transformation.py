""" Data Trandformation Process: change column names to lowercase, change AGE data type to int, fill missing age value with mean, map gender to M or F """
import pandas as pd

def transform_data(df:pd.DataFrame) -> pd.DataFrame:
    df.columns = [col.lower() for col in df.columns]
    df["age"] = df["age"].astype(int)
    df["age"] = df["age"].fillna(df["age"].mean())

    if "gender" in df.columns:
        df["gender_category"]= df["gender"].map({"Male":"M","Female":"F"})

    return df

if __name__ == "__main__":
    raw_data = pd.DataFrame({
	"Name": ["Alexander","Bob","David","Nancy"],
	"Age": ["17", "20", "34", "50"],
	"Gender": ["Male", "Female", "Male", "Female"]
})

data_transformed = transform_data(raw_data)
print(data_transformed)
