import pandas as pd


def load_and_clean_data(path):
    try:
        # Load dataset
        df = pd.read_csv(path)
        print("✅ File loaded successfully")

    except FileNotFoundError:
        print("❌ ERROR: File not found. Check the file path.")
        return None

    except Exception as e:
        print(f"❌ ERROR while loading file: {e}")
        return None

    # -------------------------------
    # BASIC CLEANING
    # -------------------------------

    # Remove leading/trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Drop completely empty rows
    df.dropna(how='all', inplace=True)

    # -------------------------------
    # HANDLE DATE COLUMN
    # -------------------------------
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        # Remove rows where Date is invalid
        df = df.dropna(subset=['Date'])

        # Sort by date (important for graphs)
        df = df.sort_values(by='Date')

    # -------------------------------
    # HANDLE NUMERIC COLUMN
    # -------------------------------
    if 'Estimated Unemployment Rate (%)' in df.columns:
        df['Estimated Unemployment Rate (%)'] = pd.to_numeric(
            df['Estimated Unemployment Rate (%)'],
            errors='coerce'
        )

        # Remove invalid numeric values
        df = df.dropna(subset=['Estimated Unemployment Rate (%)'])

    # -------------------------------
    # OPTIONAL CLEANING
    # -------------------------------

    # Standardize Region column
    if 'Region' in df.columns:
        df['Region'] = df['Region'].str.strip().str.title()

    # Reset index after cleaning
    df.reset_index(drop=True, inplace=True)

    # -------------------------------
    # FINAL INFO
    # -------------------------------
    print("✅ Data cleaned successfully")
    print("Shape after cleaning:", df.shape)

    return df