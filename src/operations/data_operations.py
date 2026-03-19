import pandas as pd

def load_donations(file_path):
    """
    Loads, cleans, and formats the blood donation dataset.
    Returns a cleaned Pandas DataFrame.
    """
    print("Loading dataset...")

    # Load the CSV
    df = pd.read_csv(file_path)
    
    # Handle missing values
    df.fillna("Unknown", inplace=True) 
    
    # Format the date column for the visualizations to easily plot the timeline chart.
    df['donation_date'] = pd.to_datetime(df['donation_date'])
    
    # Compute Summary Statistic
    # Calculate the total volume of all donations in the dataframe
    total_volume = df['volume_ml'].sum()
    average_age = df['age'].mean()
    
    print(f"✅ Data loaded successfully. Total blood volume recorded: {total_volume} ml")
    print(f"📊 Quick Stat: The average donor age is {average_age:.1f} years old.")
    
    return df