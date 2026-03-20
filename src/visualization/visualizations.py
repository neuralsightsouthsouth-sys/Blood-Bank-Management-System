import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_inventory(df, output_dir):
    """Generates a bar chart of blood type inventory."""
    # Set figure size for better readability
    plt.figure(figsize=(10, 6))
    
    # Group data: Sum volume_ml per blood_type
    inventory_data = df.groupby('blood_type')['volume_ml'].sum().reset_index()
    
    # Create the bar plot using Seaborn
    sns.barplot(data=inventory_data, x='blood_type', y='volume_ml', palette='viridis', hue='blood_type', legend=False)
    
    # Add Title and Axis Labels
    plt.title('Total Blood Inventory by Blood Type', fontsize=14, pad=15)
    plt.xlabel('Blood Type', fontsize=12)
    plt.ylabel('Total Volume (ml)', fontsize=12)
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "inventory_bar_chart.png"))
    plt.close()
    print("✅ Saved inventory_bar_chart.png")

def plot_demographics(df, output_dir):
    """Generates a pie chart of donor gender split."""
    plt.figure(figsize=(8, 8))
    
    # Count the occurrences of each gender
    gender_counts = df['gender'].value_counts()
    
    # Create the pie chart using Matplotlib
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', 
            colors=['#ff9999', '#66b3ff'], startangle=90, textprops={'fontsize': 12})
    
    # Rubric Requirement: Add Title
    plt.title('Donor Demographics by Gender', fontsize=14, pad=15)
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "demographics_pie_chart.png"))
    plt.close()
    print("✅ Saved demographics_pie_chart.png")

def plot_donations_over_time(df, output_dir):
    """Generates a line chart of donations over time."""
    plt.figure(figsize=(12, 6))
    
    # Group data by date and sum the volume
    timeline_data = df.groupby('donation_date')['volume_ml'].sum().reset_index()
    
    # Ensure data is sorted chronologically
    timeline_data = timeline_data.sort_values('donation_date')
    
    # Create the line plot using Matplotlib
    plt.plot(timeline_data['donation_date'], timeline_data['volume_ml'], 
             marker='o', linestyle='-', color='#d62728', linewidth=2)
    
    # Add Title and Axis Labels
    plt.title('Donation Volume Over Time', fontsize=14, pad=15)
    plt.xlabel('Donation Date', fontsize=12)
    plt.ylabel('Daily Volume (ml)', fontsize=12)
    
    # Format the x-axis dates so they don't overlap
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "timeline_line_chart.png"))
    plt.close()
    print("✅ Saved timeline_line_chart.png")