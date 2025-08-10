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
# 문제 2: Matplotlib 차트 꾸미기 및 여러 차트 배치하기
# --------------------------------------------------------------------------------

# 내가 최초 제출한 코딩
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 첫 번째 서브플롯 (시계열 꺾은선 그래프)
axes[0].plot(df.index, df['sales'], marker='o', linewidth=1.5, markersize=4, alpha=0.9)
axes[0].set_title('Daily Sales over Time')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Sales')
axes[0].grid(alpha=0.3)
axes[0].tick_params(axis='x', rotation=45)

# 두 번째 서브플롯 (산점도)
axes[1].scatter(df['temperature'], df['sales'], alpha=0.7)
axes[1].set_title('Sales vs Temperature')
axes[1].set_xlabel('Temperature (°C)')
axes[1].set_ylabel('Sales')
axes[1].grid(alpha=0.3)
m, b = np.polyfit(df['temperature'], df['sales'], 1)
xs = np.linspace(df['temperature'].min(), df['temperature'].max(), 100)
axes[1].plot(xs, m*xs + b, linestyle='--', linewidth=1)

plt.tight_layout()
plt.show()

# --------------------------------------------------------------------------------
# 피드백 및 모범 답안
# --------------------------------------------------------------------------------

# - 문제의 요구사항을 완벽하게 충족하는 훌륭한 코드입니다.
# - 'plt.subplots()'를 사용하여 여러 차트를 효율적으로 배치하고, 'axes' 객체를 활용한 객체 지향 방식의 코드가 매우 깔끔합니다.
# - 각 서브플롯에 'set_title', 'set_xlabel' 등 Axes 객체의 메서드를 사용하여 차트를 꾸민 점도 모범적입니다.

# [추가 학습]
# - 서브플롯을 만들 때 'plt.subplots(nrows=1, ncols=2)'처럼 인자를 명시하면 가독성을 더 높일 수 있습니다.
# - 'plt.figure()'를 먼저 만들고 'fig.add_subplot()'으로 서브플롯을 추가하는 방법도 있습니다. 'plt.subplots()'가 더 편리하지만, 이 방식도 알아두면 좋습니다.
