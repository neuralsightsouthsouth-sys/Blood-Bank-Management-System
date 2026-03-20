import os
import sys

# Ensure Python can find our modules if run from the root directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the core models 
from models.classes import Donor, BloodBank

# Import the data pipeline
from operations.data_operations import load_donations

# Import the inventory logic
from operations.inventory_operations import check_supply, flag_shortage

# Import the visualization generators
from visualization.visualizations import plot_inventory, plot_demographics, plot_donations_over_time


def main():
    print("==================================================")
    print("🩸 Starting Blood Bank Management System...")
    print("==================================================\n")
    
    # Setup paths relative to the root directory
    data_path = os.path.join("data", "blood_donations.csv")
    output_dir = os.path.join("outputs", "figures")
    
    # Ensure the output directory exists so the visualization script doesn't crash
    os.makedirs(output_dir, exist_ok=True)
    
    # Execute Data Pipeline
    print("--- Phase 1: Data Pipeline ---")
    try:
        df = load_donations(data_path)
    except FileNotFoundError:
        print(f"❌ Error: Could not find dataset at '{data_path}'. Make sure you are running the script from the root project folder!")
        return

    # Initialize Core System and Logic
    print("\n--- Phase 2: Core System & Inventory Logic ---")
    
    # --- OOP INTEGRATION LOOP ---
    print("Initializing system memory and registering donors...")
    regional_bank = BloodBank(name="SPARK South South Regional Blood Bank")
    
    # Loop through the Pandas DataFrame and create a Donor object for each row
    for index, row in df.iterrows():
        new_donor = Donor(
            donor_id=row['donor_id'],
            name=row['donor_name'],
            blood_type=row['blood_type'],
            volume_ml=row['volume_ml']
        )
        # Add the donor to the bank's registry silently
        regional_bank.donors.append(new_donor) 
        
    print(f"✅ Successfully registered {regional_bank.get_total_donors()} donors into the active system memory.")
    # ---------------------------------
    
    # Run the supply check and shortage flagger functions
    inventory_levels = check_supply(df)
    flag_shortage(inventory_levels, threshold_ml=1000)
    
    # Generate Visualizations
    print("\n--- Phase 3: Generating Visualizations ---")
    print("Creating charts and saving to 'outputs/figures/'...")
    
    # Trigger the three required charts
    plot_inventory(df, output_dir)
    plot_demographics(df, output_dir)
    plot_donations_over_time(df, output_dir)
    
    print("\n==================================================")
    print("✅ System Execution Complete!")
    print("Check the 'outputs/figures/' folder for your generated charts.")
    print("==================================================")


if __name__ == "__main__":
    main()