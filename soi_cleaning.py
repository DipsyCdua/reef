import pandas as pd

# load all lines from file "raw_input_data/enso.txt"
with open("raw_input_data/enso.txt", "r") as file:
    lines = file.readlines()

# extract only the anomaly block (everything after first and before second header)
start_idx = next(i for i, line in enumerate(lines) if line.strip().startswith("1951"))
end_idx = next(i for i, line in enumerate(lines[start_idx:], start=start_idx) if "STANDARDIZED" in lines[i])

# keep only data lines
data_lines = lines[start_idx:end_idx]

# remove trailing newline characters, missing values and handle spacing
cleaned_lines = [line.strip().replace("-999.9", "NA") for line in data_lines if line.strip()]

# dataframe
data = [line.split() for line in cleaned_lines]

# remove rows that don't have at least 13 columns (year + 12 months)
data = [row for row in data if len(row) == 13]

for i, row in enumerate(data):
    if len(row) < 13:
        missing = 13 - len(row)
        data[i] = row + ['NA'] * missing
        
# make df
df = pd.DataFrame(data, columns=["Year", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# convert data types types
df["Year"] = df["Year"].astype(int)
for month in df.columns[1:]:
    df[month] = pd.to_numeric(df[month], errors="coerce")

# melt from wide to long format
enso_long = df.melt(id_vars="Year", var_name="Month", value_name="soi_anomaly")

# add new date column
enso_long["Date"] = pd.to_datetime(enso_long["Year"].astype(str) + "-" + enso_long["Month"],
                                   format="%Y-%b", errors="coerce")

# drop old year and month columns
enso_long = enso_long.drop(columns=["Year", "Month"])

# filter for valid dates and from 1985 onwards
enso_long = enso_long.dropna(subset=["Date"])
enso_long = enso_long[enso_long["Date"] >= "1985-01-01"]

# look 
print(enso_long.head())
print(enso_long.shape)
print(enso_long.info())

# download as csv
enso_long.to_csv("output_data/soi_index_py.csv", index=False)


import pandas as pd
print("Pandas version:", pd.__version__)
df = pd.DataFrame({'A':[1,2,3]})
print(df)
