import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create an 'images' directory if it doesn't exist
output_dir = 'images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the data from the CSV file
file_path = 'ghg_data.csv'
df = pd.read_csv(file_path)

# --- IMPORTANT FIX: Strip whitespace from column names ---
df.columns = df.columns.str.strip()

# Data Cleaning: Remove commas and convert to numeric
df['GHG_Emissions'] = df['GHG_Emissions'].str.replace(',', '').astype(float)
df['Total_Emissions'] = df['Total_Emissions'].str.replace(',', '').astype(float)

# Clean company names by removing leading/trailing spaces
df['Company'] = df['Company'].str.strip()

# Set plot style and font for better aesthetics
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans' # Or 'Malgun Gothic' for Korean font if available
plt.rcParams['axes.unicode_minus'] = False # Prevents minus sign from breaking on some fonts

# --- Plot for SK Innovation ---
sk_df = df[df['Company'] == 'SK Innovation Co., Ltd.'].copy()

plt.figure(figsize=(12, 7))
sns.lineplot(data=sk_df, x='Year', y='GHG_Emissions', marker='o', label='Scope 1 + 2 Emissions', color='#4C72B0', linewidth=2.5)
sns.lineplot(data=sk_df, x='Year', y='Total_Emissions', marker='o', label='Scope 1 + 2 + 3 Emissions', color='#C44E52', linewidth=2.5)

plt.title('SK Innovation: GHG Emissions Comparison (Scope 1+2 vs Scope 1+2+3)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, labelpad=10)
plt.ylabel('GHG Emissions (tCO2eq)', fontsize=12, labelpad=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(sk_df['Year'].unique(), fontsize=10)
plt.yticks(fontsize=10)
plt.ticklabel_format(style='plain', axis='y') # Use plain format to avoid scientific notation for large numbers
plt.legend(title='Emission Scope', title_fontsize='12', fontsize='10', loc='upper left', frameon=True, shadow=True, borderpad=1)

# Annotate points for clarity
for _, row in sk_df.iterrows():
    plt.annotate(f'{row["GHG_Emissions"] / 1_000_000:,.1f}M', xy=(row['Year'], row['GHG_Emissions']),
                 xytext=(row['Year'] - 0.2, row['GHG_Emissions'] + 5000000), # Adjust y offset
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                 fontsize=9, color='#4C72B0', ha='center')
    plt.annotate(f'{row["Total_Emissions"] / 1_000_000:,.1f}M', xy=(row['Year'], row['Total_Emissions']),
                 xytext=(row['Year'] + 0.2, row['Total_Emissions'] + 5000000), # Adjust y offset
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                 fontsize=9, color='#C44E52', ha='center')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'sk_innovation_ghg_comparison.png'), dpi=300, bbox_inches='tight')
plt.show()

# --- Plot for KB Financial Group ---
kb_df = df[df['Company'] == 'KB Financial Group Inc.'].copy()

plt.figure(figsize=(12, 7))
sns.lineplot(data=kb_df, x='Year', y='GHG_Emissions', marker='o', label='Scope 1 + 2 Emissions', color='#4C72B0', linewidth=2.5)
sns.lineplot(data=kb_df, x='Year', y='Total_Emissions', marker='o', label='Scope 1 + 2 + 3 Emissions', color='#C44E52', linewidth=2.5)

plt.title('KB Financial Group: GHG Emissions Comparison (Scope 1+2 vs Scope 1+2+3)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, labelpad=10)
plt.ylabel('GHG Emissions (tCO2eq)', fontsize=12, labelpad=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(kb_df['Year'].unique(), fontsize=10)
plt.yticks(fontsize=10)
plt.ticklabel_format(style='plain', axis='y') # Use plain format to avoid scientific notation
plt.legend(title='Emission Scope', title_fontsize='12', fontsize='10', loc='upper left', frameon=True, shadow=True, borderpad=1)

# Annotate points for clarity
for _, row in kb_df.iterrows():
    # Adjusted text position for KB to prevent overlap, given smaller scale
    plt.annotate(f'{row["GHG_Emissions"]:,.0f}', xy=(row['Year'], row['GHG_Emissions']),
                 xytext=(row['Year'] - 0.2, row['GHG_Emissions'] + 50000), # Adjust y offset
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                 fontsize=9, color='#4C72B0', ha='center')
    plt.annotate(f'{row["Total_Emissions"]:,.0f}', xy=(row['Year'], row['Total_Emissions']),
                 xytext=(row['Year'] + 0.2, row['Total_Emissions'] + 50000), # Adjust y offset
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                 fontsize=9, color='#C44E52', ha='center')


plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'kb_financial_group_ghg_comparison.png'), dpi=300, bbox_inches='tight')
plt.show()
