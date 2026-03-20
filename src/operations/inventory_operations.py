import pandas as pd

def check_supply(df):
    """
    Calculates the total available blood volume for each blood type.
    Takes a cleaned Pandas DataFrame as input and returns a Pandas Series.
    """
    print("\n--- Checking Inventory Levels ---")
    
    # Group the data by blood type and sum the volumes
    inventory_summary = df.groupby('blood_type')['volume_ml'].sum()

    return inventory_summary

def flag_shortage(inventory_series, threshold_ml=500):
    """Flags any blood types that fall below the critical threshold."""
    print(f"\n--- Checking for shortages (Threshold: {threshold_ml}ml) ---")
    
    # Iterate through the Pandas Series to check each blood type
    shortages_found = False
    for blood_type, volume in inventory_series.items():
        if volume < threshold_ml:
            print(f"⚠️  CRITICAL SHORTAGE: Type {blood_type} only has {volume}ml available!")
            shortages_found = True
        else:
            print(f"✅ Type {blood_type} levels are adequate ({volume}ml).")
            
    if not shortages_found:
        print("✅ All blood type inventories are currently above the critical threshold.")