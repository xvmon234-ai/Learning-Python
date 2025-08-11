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
# 문제 3: Seaborn 고급 시각화 활용
# --------------------------------------------------------------------------------

# 내가 최초 제출한 코딩
sns.set(style="whitegrid")

# Figure & Axes 생성
fig, axes = plt.subplots(3, 1, figsize=(12, 15))

# 1. Lineplot - sales & customer_satisfaction 추이
sns.lineplot(x=df.index, y='sales', data=df, label='Sales', ax=axes[0])
sns.lineplot(x=df.index, y='customer_satisfaction', data=df, label='Customer Satisfaction', ax=axes[0])
axes[0].set_title('Sales & Customer Satisfaction Over Time')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Value')
axes[0].tick_params(axis='x', rotation=45)
axes[0].legend()

# 2. Barplot - 도시별 평균 Sales
sns.barplot(x='city', y='sales', data=df, ci=None, palette='pastel', ax=axes[1])
axes[1].set_title('Average Sales by City')
axes[1].set_xlabel('City')
axes[1].set_ylabel('Average Sales')

# 3. Heatmap - 숫자형 열 상관관계
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=axes[2])
axes[2].set_title('Correlation Heatmap')

plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------------
# 피드백 및 모범 답안
# --------------------------------------------------------------------------------

# - Seaborn의 다양한 기능(스타일, 팔레트)과 Pandas DataFrame의 연동을 완벽하게 이해하고 활용했습니다.
# - 'ax' 인자를 사용하여 Matplotlib의 서브플롯에 Seaborn 차트를 그린 점은 두 라이브러리를 유연하게 결합하는 좋은 예시입니다.
# - 특히 히트맵에서 'df.corr()'로 상관관계 행렬을 만들고 'annot=True', 'fmt=".2f"'로 가독성을 높인 부분은 매우 뛰어납니다.

# [추가 학습]
# - 'lineplot'에서 'hue' 매개변수를 사용하면 두 변수를 한 번에 더 깔끔하게 시각화할 수 있습니다.
# - 'barplot'에서 각 막대 위에 실제 값을 표시하고 싶다면, 반복문을 사용해 'axes[1].text()' 함수로 텍스트를 추가할 수 있습니다.
# - 'heatmap'에서 상관관계가 낮은 변수들을 찾아내고, 이 변수들을 제외하고 다시 히트맵을 그려보는 연습을 해보세요. 이는 불필요한 변수를 제거하는 데이터 분석의 중요한 과정입니다.
