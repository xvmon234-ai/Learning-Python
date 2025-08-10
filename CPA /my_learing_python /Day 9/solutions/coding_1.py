import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 데이터 준비 ---
data = {
    'date': pd.to_datetime(pd.date_range(start='2024-01-01', periods=100, freq='D')),
    'sales': np.random.randint(50, 150, 100) + np.arange(100),
    'temperature': np.random.normal(15, 5, 100),
    'product': np.random.choice(['A', 'B', 'C'], 100),
    'city': np.random.choice(['Seoul', 'Busan', 'Jeju'], 100),
    'customer_satisfaction': np.random.uniform(3, 5, 100)
}
df = pd.DataFrame(data)
df.set_index('date', inplace=True)

# --------------------------------------------------------------------------------
# 문제 1: Matplotlib 기본 차트 그리기
# --------------------------------------------------------------------------------

# 1-1. 꺾은선 그래프: 내가 최초 제출한 코딩
plt.figure(figsize=(12, 4))
plt.plot(df.index, df['sales'], marker='o',
         linewidth=1.5, markersize=4, alpha=0.9)
plt.title('Daily Sales over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 1-2. 산점도: 내가 최초 제출한 코딩
plt.figure(figsize=(7, 5))
plt.scatter(df['temperature'], df['sales'], alpha=0.7)
plt.title('Sales vs Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Sales')
plt.grid(alpha=0.3)
m, b = np.polyfit(df['temperature'], df['sales'], 1)
xs = np.linspace(df['temperature'].min(), df['temperature'].max(), 100)
plt.plot(xs, m*xs + b, linestyle='--', linewidth=1)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------------
# 피드백 및 모범 답안
# --------------------------------------------------------------------------------

# 1. 꺾은선 그래프 피드백:
# Matplotlib의 기본 기능들을 매우 잘 활용했습니다. 'marker', 'linewidth', 'alpha' 등의 매개변수로 그래프를 꾸민 점이 훌륭합니다.
# 'plt.xticks(rotation=45)'와 'plt.tight_layout()'를 사용하여 가독성을 높인 것도 좋은 습관입니다.

# 2. 산점도 피드백:
# 'alpha'로 투명도를 조절하여 점들이 겹쳐 보일 때 밀도를 파악하기 쉽게 한 점이 좋습니다.
# 특히, 'np.polyfit'을 사용해 회귀선을 추가한 부분은 데이터를 분석하려는 뛰어난 접근입니다. 이는 단순히 시각화를 넘어 데이터의 추세를 파악하려는 좋은 시도입니다.

# [추가 학습]
# - 'plt.plot'과 'plt.scatter'는 Pandas DataFrame의 내장 시각화 함수인 'df.plot()'과 'df.plot.scatter()'로 더 간결하게 작성할 수도 있습니다.
#   - 예: 'df['sales'].plot(title='일별 매출 추이')'
