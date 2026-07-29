import pandas as pd

def clean_excel(input_file, output_file):
    print("===== Excel Data Cleaner Started =====")
    
    df = pd.read_excel(input_file)
    original_rows = len(df)
    print(f"Pehle: {original_rows} rows")

    df = df.dropna()
    df = df.drop_duplicates()
    
    df.columns = df.columns.str.strip().str.lower()

    df.to_csv(output_file, index=False)
    cleaned_rows = len(df)
    
    print(f"Baad me: {cleaned_rows} rows")
    print(f"✅ File ready: {output_file}")

clean_excel("client_data.xlsx", "cleaned_data.csv")