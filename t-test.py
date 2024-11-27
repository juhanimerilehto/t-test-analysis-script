import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def perform_ttest_analysis(excel_path='data.xlsx', 
                         group_column='Group',      # Column containing group labels
                         value_column='Value',      # Column containing measurements
                         group1_name='Group1',      # Name of first group to compare
                         group2_name='Group2',      # Name of second group to compare
                         output_prefix='ttest'):    # Prefix for output files
    """
    Performs independent t-test analysis on two groups from Excel data.
    
    Parameters:
    -----------
    excel_path : str
        Path to Excel file containing the data
    group_column : str
        Name of column containing group labels
    value_column : str
        Name of column containing the values to compare
    group1_name, group2_name : str
        Names of the groups to compare
    output_prefix : str
        Prefix for output files
    """
    
    # Read the data
    print(f"Reading data from {excel_path}...")
    df = pd.read_excel(excel_path)
    
    # Extract the two groups
    group1_data = df[df[group_column] == group1_name][value_column]
    group2_data = df[df[group_column] == group2_name][value_column]
    
    # Perform t-test
    t_stat, p_value = stats.ttest_ind(group1_data, group2_data)
    
    # Calculate descriptive statistics
    desc_stats = pd.DataFrame({
        'Statistic': ['Mean', 'Std Dev', 'N', 'SEM'],
        group1_name: [group1_data.mean(), group1_data.std(), 
                     len(group1_data), group1_data.sem()],
        group2_name: [group2_data.mean(), group2_data.std(), 
                     len(group2_data), group2_data.sem()]
    })
    
    # Create results dictionary
    results = {
        'Test Type': 'Independent t-test',
        't-statistic': t_stat,
        'p-value': p_value,
        'Significant': 'Yes' if p_value < 0.05 else 'No',
        'Group 1': group1_name,
        'Group 2': group2_name,
        'Group 1 Mean': group1_data.mean(),
        'Group 2 Mean': group2_data.mean()
    }
    
    # Convert results to DataFrame
    results_df = pd.DataFrame([results])
    
    # Create timestamp for file naming
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save results to Excel
    excel_output = f'{output_prefix}_results_{timestamp}.xlsx'
    with pd.ExcelWriter(excel_output) as writer:
        results_df.to_excel(writer, sheet_name='Test Results', index=False)
        desc_stats.to_excel(writer, sheet_name='Descriptive Stats', index=False)
    
    print("\nResults saved to:", excel_output)
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    
    # Create boxplot
    sns.boxplot(x=df[group_column], y=df[value_column], 
                order=[group1_name, group2_name])
    
    # Add individual points
    sns.swarmplot(x=df[group_column], y=df[value_column], 
                 order=[group1_name, group2_name], 
                 color='0.25', size=4, alpha=0.5)
    
    plt.title(f'Comparison of {value_column} between Groups\np = {p_value:.4f}')
    plt.xlabel(group_column)
    plt.ylabel(value_column)
    
    # Save plot
    plot_output = f'{output_prefix}_plot_{timestamp}.png'
    plt.savefig(plot_output, dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Plot saved to:", plot_output)
    
    # Print results to terminal
    print("\nT-Test Results:")
    print("--------------")
    print(f"t-statistic: {t_stat:.4f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Significant difference: {'Yes' if p_value < 0.05 else 'No'}")
    print("\nDescriptive Statistics:")
    print(desc_stats)

if __name__ == "__main__":
    # Example usage:
    # Modify these parameters according to your data
    perform_ttest_analysis(
        excel_path='data.xlsx',
        group_column='Group',
        value_column='Value',
        group1_name='Control',
        group2_name='Treatment',
        output_prefix='ttest'
    )