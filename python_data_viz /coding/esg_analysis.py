import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Load CSV File ---
# Assuming the CSV file already has the updated English headers and company names.
df = pd.read_csv('esg_data.csv')

# Print top 5 rows to confirm successful loading
print("--- Data Preview (Top 5 Rows) ---")
print(df.head())

# Print DataFrame info to check column types and missing values
print("\n--- DataFrame Info (Before Type Conversion) ---")
print(df.info())

# --- 2. Data Preprocessing ---
# Remove commas from 'GHG_Emissions' column and convert to numeric (float).
# errors='coerce' will convert unparseable values to NaN, preventing errors.
df['GHG_Emissions'] = df['GHG_Emissions'].str.replace(',', '').astype(float)

print("\n--- DataFrame Info (After Type Conversion) ---")
print(df.info()) # Check if Dtype has changed to float64 after conversion

# --- 3. Data Visualization ---

# 3-0. Define Common Styles and Settings
# Define company specific colors and order for consistent visualization
# IMPORTANT: Using the exact company names confirmed by the user, including the leading space for SK Innovation.
company_order = ['KB Financial Group Inc.', ' SK Innovation Co., Ltd.']
palette = {'KB Financial Group Inc.': '#4C72B0', ' SK Innovation Co., Ltd.': '#C44E52'} # KB (blueish), SK (reddish)

# Set Matplotlib style (applies to all graphs)
plt.style.use('seaborn-v0_8-whitegrid') # Clean white background with grid lines

# --- Font Settings ---
# For English text, 'DejaVu Sans' or 'Arial' are common.
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False # Prevents minus sign from breaking

# 3-1. ESG Keyword Mention Frequency Trend (by Company)
keyword_plots = {
    'E_Keyword_Freq': {
        'title': 'Company-wise Environmental (E) Keyword Mention Frequency Trend (2022-2024)',
        'ylabel': 'Mention Frequency',
        'filename': 'environmental_keyword_trend.png',
        'annotations': [
            # IMPORTANT: Using the exact company name ' SK Innovation Co., Ltd.' (with leading space)
            {'company': ' SK Innovation Co., Ltd.', 'year': 2023, 'offset_y': -80, 'ha': 'left'},
            {'company': 'KB Financial Group Inc.', 'year': 2023, 'offset_y': 80, 'ha': 'left'}
        ]
    },
    'S_Keyword_Freq': {
        'title': 'Company-wise Social (S) Keyword Mention Frequency Trend (2022-2024)',
        'ylabel': 'Mention Frequency',
        'filename': 'social_keyword_trend.png',
        'annotations': [
            # IMPORTANT: Using the exact company name ' SK Innovation Co., Ltd.' (with leading space)
            {'company': ' SK Innovation Co., Ltd.', 'year': 2023, 'offset_y': -60, 'ha': 'left'},
            {'company': 'KB Financial Group Inc.', 'year': 2023, 'offset_y': 60, 'ha': 'left'}
        ]
    },
    'G_Keyword_Freq': {
        'title': 'Company-wise Governance (G) Keyword Mention Frequency Trend (2022-2024)',
        'ylabel': 'Mention Frequency',
        'filename': 'governance_keyword_trend.png',
        'annotations': [
            # IMPORTANT: Using the exact company name ' SK Innovation Co., Ltd.' (with leading space)
            {'company': ' SK Innovation Co., Ltd.', 'year': 2023, 'offset_y': -80, 'ha': 'left'},
            {'company': 'KB Financial Group Inc.', 'year': 2023, 'offset_y': 80, 'ha': 'left'}
        ]
    }
}

for keyword, plot_info in keyword_plots.items():
    plt.figure(figsize=(10, 6))
    
    sns.lineplot(data=df, x='Year', y=keyword, hue='Company', marker='o',
                 hue_order=company_order, palette=palette, linewidth=2.5)

    plt.title(plot_info['title'], fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Year', fontsize=12, labelpad=10)
    plt.ylabel(plot_info['ylabel'], fontsize=12, labelpad=10)
    
    plt.xticks(df['Year'].unique(), fontsize=10)
    plt.yticks(fontsize=10)

    plt.grid(True, linestyle='--', alpha=0.6)

    plt.legend(title='Company', title_fontsize='12', fontsize='10', 
               loc='upper right', frameon=True, shadow=True, borderpad=1)

    for annot_info in plot_info['annotations']:
        company = annot_info['company']
        year = annot_info['year']
        offset_y = annot_info['offset_y']
        ha = annot_info['ha']

        data_point = df[(df['Company'] == company) & (df['Year'] == year)][keyword].values
        if len(data_point) > 0:
            value = data_point[0]
            plt.annotate(f'{value}', xy=(year, value), xytext=(year + 0.1, value + offset_y),
                         arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                         fontsize=9, color='black', ha=ha)
        else:
            print(f"Warning: No data found for {company} in {year} for {keyword}. Skipping annotation.")

    plt.tight_layout()
    plt.savefig(f'/content/{plot_info["filename"]}', dpi=300, bbox_inches='tight')
    plt.show()

# 3-2. Greenhouse Gas Emissions Trend (by Company)
plt.figure(figsize=(10, 6))

sns.lineplot(data=df, x='Year', y='GHG_Emissions', hue='Company', marker='o',
             hue_order=company_order, palette=palette, linewidth=2.5)

plt.title('Company-wise GHG Emissions Trend (2022-2024)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12, labelpad=10)
plt.ylabel('GHG Emissions (tCO2eq)', fontsize=12, labelpad=10)

plt.xticks(df['Year'].unique(), fontsize=10)
plt.yticks(fontsize=10)
plt.ticklabel_format(style='plain', axis='y')

plt.grid(True, linestyle='--', alpha=0.6)

plt.legend(title='Company', title_fontsize='12', fontsize='10', 
           loc='upper left', frameon=True, shadow=True, borderpad=1)

# Add annotations for GHG Emissions
# IMPORTANT: Using the exact company name ' SK Innovation Co., Ltd.' (with leading space)
sk_2024_ghg_data = df[(df['Company'] == ' SK Innovation Co., Ltd.') & (df['Year'] == 2024)]['GHG_Emissions'].values
if len(sk_2024_ghg_data) > 0:
    sk_2024_ghg = sk_2024_ghg_data[0]
    plt.annotate(f'{sk_2024_ghg:,.0f}', xy=(2024, sk_2024_ghg), xytext=(2024.1, sk_2024_ghg + 500000),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                 fontsize=9, color='black', ha='left')
else:
    print("Warning: No data found for SK Innovation Co., Ltd. in 2024 for GHG Emissions. Skipping annotation.")

kb_2024_ghg_data = df[(df['Company'] == 'KB Financial Group Inc.') & (df['Year'] == 2024)]['GHG_Emissions'].values
if len(kb_2024_ghg_data) > 0:
    kb_2024_ghg = kb_2024_ghg_data[0]
    plt.annotate(f'{kb_2024_ghg:,.0f}', xy=(2024, kb_2024_ghg), xytext=(2024.1, kb_2024_ghg + 10000),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                 fontsize=9, color='black', ha='left')
else:
    print("Warning: No data found for KB Financial Group Inc. in 2024 for GHG Emissions. Skipping annotation.")

plt.tight_layout()
plt.savefig('/content/ghg_emissions_trend_enhanced.png', dpi=300, bbox_inches='tight')
plt.show()
