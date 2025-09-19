# Data Engineering Toolkit

A collection of beginner-friendly Python scripts demonstrating essential **data engineering tasks** such as data cleaning, transformation, and loading.  
This project follows the **Gitflow branching strategy** with pull requests and code reviews for collaboration.

---

## 📖 Documentation

### Features
1. **Data Cleaning** – removes duplicates, trims spaces, handles nulls.  
2. **Data Transformation** – standardizes column names, casts data types, maps categories.  
3. **Data Loading** – saves processed data to CSV and Parquet format for efficient storage.  

---

## 💻 Code Examples

### Data Cleaning
```python
from data_cleaning import clean_data
import pandas as pd

raw_data = pd.DataFrame({
    "Name": ["Alice ", "Bob", "Bob", None],
    "Age": [25, 30, 30, None]
})

cleaned = clean_data(raw_data)
print(cleaned)
```
### Data Transformation
```Python
from data_transformation import transform_data
import pandas as pd

raw_data = pd.DataFrame({
    "Name": ["Alexander", "Nancy"],
    "Age": ["22", "31"],
    "Gender": ["Male", "Female"]
})

transformed = transform_data(raw_data)
print(transformed)
```

### Data Loading
``` python
def save_to_csv(df:pd.DataFrame, filename:str) -> None:
    df.to_csv(filename, index = False)
    print(f"Data saved to {filename}")

def save_to_parquet(df:pd.DataFrame, filename:str) -> None:
    df.to_parquet(filename, engine="pyarrow", index=False)
    print(f"Data saved to {filename}")
```

---

## TEsting Instructions
# Run data cleaning
`python3 data-cleaning-scripts/data_cleaning.py`

# Run data transformation
`python3 data-transformation-scripts/data_transformation.py`

# Run data loading
`python3 data-loading-scripts/data_loading.py`

Dont forget to `pip install pyarrow` to be able to use the engine in converting to .parquet file format.

## Branching strategy
- `main`: stable production-ready code.
- `develop`: integration branch
- `feature/script-folder-name`: new scripts and features

## Contribution guide
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/feature-name`
3. Commit your code: `git commit -m "I added xyz new features"`
4. Push to your feature branch: `git push origin feature/feature-name`
5. Then, wait for code review and approval before it is merged into the `develop` branch, and later merged to the `main` branch.
