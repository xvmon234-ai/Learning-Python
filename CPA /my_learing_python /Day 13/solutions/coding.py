import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# --- 데이터 준비 (파일이 없는 경우 생성) ---
# 이 부분은 모의고사 readme.md에 포함되어 있던 코드로, 파일 존재 유무에 관계없이 스크립트를 실행할 수 있도록 합니다.
try:
    df = pd.read_csv('sales_data.csv')
    print("DataFrame을 성공적으로 불러왔습니다.")
except FileNotFoundError:
    print("sales_data.csv 파일을 찾을 수 없습니다. 파일을 생성합니다.")
    data = {
        'sale_id': range(1, 2001),
        'product_id': np.random.choice(range(101, 151), 2000),
        'sale_date': pd.to_datetime(pd.date_range(start='2023-01-01', periods=2000, freq='H')),
        'quantity': np.random.randint(1, 20, 2000),
        'price': np.random.randint(1000, 50000, 2000)
    }
    df = pd.DataFrame(data)
    df.loc[50:100, 'price'] = np.nan
    df.loc[1000:1050, 'quantity'] = -1
    df.loc[1500:1510] = df.loc[0:10].values
    df.to_csv('sales_data.csv', index=False)
    df = pd.read_csv('sales_data.csv')


# --------------------------------------------------------------------------------
# 문제 1: 데이터 불러오기 및 전처리
# --------------------------------------------------------------------------------

# [내가 최초 제공한 코딩]
print("\n--- 초기 데이터 정보 ---")
df.info()

median_price = df['price'].median()
df['price'] = df['price'].fillna(median_price)

initial_rows = len(df)
df.drop_duplicates(inplace=True)
print(f"\n{initial_rows - len(df)}개의 중복된 행을 제거했습니다.")

df.loc[df['quantity'] < 1, 'quantity'] = 1

df['sale_date'] = pd.to_datetime(df['sale_date'])
print("\n--- 전처리 완료된 데이터 정보 ---")
df.info()


# [피드백 및 모범 답안]
# - 파일 존재 유무를 확인하는 'try-except' 구문은 실전에서 매우 유용한 방법입니다.
# - 'price' 결측치를 'median'으로 채워 이상치에 덜 민감하게 만든 판단이 탁월합니다.
# - 'drop_duplicates'와 '.loc'을 활용한 데이터 클리닝 과정이 매우 효율적이고 정확합니다.
# - 'to_datetime'으로 날짜 형식을 제대로 변환하여 다음 단계의 시계열 분석을 위한 준비를 완벽하게 마쳤습니다.


# --------------------------------------------------------------------------------
# 문제 2: 분석 및 시각화
# --------------------------------------------------------------------------------

# [내가 최초 제공한 코딩]
sns.set_style('whitegrid')

# 2-1. 2023년 1월 ~ 3월 일별 평균 판매량 추세 분석
start_date = '2023-01-01'
end_date = '2023-03-31'
df_period = df[(df['sale_date'] >= start_date) & (df['sale_date'] <= end_date)]

df_daily_avg = df_period.resample('D', on='sale_date')['quantity'].mean().reset_index()

plt.figure(figsize=(15, 7))
sns.lineplot(x='sale_date', y='quantity', data=df_daily_avg)
plt.title('Daily Average Sales Quantity (Jan-Mar 2023)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Average Quantity', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2-2. 총 판매액 기준 상위 10개 상품 분석
df['total_sales'] = df['quantity'] * df['price']
top10_products = df.groupby('product_id')['total_sales'].sum().nlargest(10).reset_index()

plt.figure(figsize=(12, 8))
sns.barplot(x='product_id', y='total_sales', data=top10_products, palette='viridis')
plt.title('Top 10 Products by Total Sales Amount', fontsize=16)
plt.xlabel('Product ID', fontsize=12)
plt.ylabel('Total Sales Amount', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# [피드백 및 모범 답안]
# - 시계열 데이터 분석에 'resample()' 메서드를 사용한 것은 매우 전문적인 접근입니다. 이를 통해 일별 평균 판매량을 정확하고 효율적으로 계산했습니다.
# - 'nlargest(10)'을 사용하여 상위 10개 상품을 손쉽게 찾았습니다.
# - 두 개의 시각화 모두 데이터의 특성(시간 흐름 vs. 항목 비교)에 맞는 차트 종류를 선택했고, 제목과 레이블을 명확히 표기하여 가독성이 높습니다.


# --------------------------------------------------------------------------------
# 문제 3: 데이터 저장
# --------------------------------------------------------------------------------

# [내가 최초 제공한 코딩]
conn = sqlite3.connect('sales_summary.db')
top10_products.to_sql('top_products', conn, if_exists='replace', index=False)
conn.close()
print("\n상위 10개 상품 데이터가 sales_summary.db에 성공적으로 저장되었습니다.")


# [피드백 및 모범 답안]
# - Pandas의 'to_sql' 메서드를 활용하여 데이터베이스에 데이터를 저장하는 가장 간편하고 효율적인 방법을 사용했습니다.
# - 'if_exists='replace''와 'index=False' 옵션을 정확하게 사용하여 재실행 시에도 오류 없이 테이블을 갱신하도록 구성했습니다.
# - 데이터베이스 연결을 'conn.close()'로 명시적으로 종료한 것도 좋은 습관입니다.
