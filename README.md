# 🧹 Task 1: Data Cleaning and Preprocessing

## 🎯 Objective

Clean and prepare a raw sales dataset by identifying and handling:
- Missing values
- Duplicates
- Inconsistent formats
- Incorrect data types

---

## 🛠️ Tools Used

- **Language:** Python 3.x  
- **Library:** Pandas
- **IDE:** VS Code 
- **Dataset:** Sales Data (from Kaggle or any real-world sales CSV)

---

## 🔍 Data Cleaning Steps

### 1. **Load Dataset**
```python
import pandas as pd

df = pd.read_csv("sales_data.csv")
```

---

### 2. **Handle Missing Values**
```python
# Check for nulls
df.isnull().sum()

# Fill or drop missing values
df['Customer Name'].fillna('Unknown', inplace=True)
df.dropna(subset=['Order Date'], inplace=True)
```

---

### 3. **Remove Duplicates**
```python
# Check for duplicates
df.duplicated().sum()

# Remove duplicates
df.drop_duplicates(inplace=True)
```

---

### 4. **Standardize Text Fields**
```python
# Standardize Gender, Country, etc.
df['Gender'] = df['Gender'].str.strip().str.title()
df['Country'] = df['Country'].str.strip().str.title()
```

---

### 5. **Convert Date Formats**
```python
# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce', dayfirst=True)
```

---

### 6. **Clean Column Names**
```python
# Clean column names (lowercase, underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
```

---

### 7. **Fix Data Types**
```python
# Convert columns to appropriate types
df['quantity'] = df['quantity'].astype('int')
df['total_sales'] = df['total_sales'].astype('float')
```

---

## ✨ Summary of Changes

| Issue | Fix |
|------|-----|
| Missing values in `Customer Name`, `Order Date` | Filled with 'Unknown' or removed |
| Duplicate records | Removed using `drop_duplicates()` |
| Inconsistent text formatting | Standardized using `.str.title()` |
| Mixed date formats | Converted using `pd.to_datetime()` |
| Dirty column names | Renamed to `snake_case` |
| Incorrect data types (e.g. quantity as string) | Converted to `int`, `float`, `datetime` |

---

## 📦 Output

- ✅ Cleaned dataset: `cleaned_sales_data.csv`
- ✅ Ready for analysis, modeling, or visualization.

---

## 📘 Outcome

By completing this task, I practiced:
- Data auditing using `.isnull()`, `.duplicated()`, `.dtypes`
- Cleaning and preprocessing techniques
- Preparing raw data for reliable analysis

---
