import numpy as np
from scipy.optimize import newton

cash_flows = [-500000000, 100000000, 150000000, 200000000, 180000000, 120000000]
discount_rates = 0.1

def npv(rate, cash_flows):
    return sum([cf / (1 + rate) ** i for i, cf in enumerate(cash_flows)])
def irr(cash_flows, guess=0.1):
    return newton(lambda r: npv(r, cash_flows), guess)

npv_result = npv(discount_rates, cash_flows)
irr_result = irr(cash_flows)

print(f"NPV (r={discount_rates*100:.1f}%): {npv_result:.2f}")
print(f"IRR: {irr_result*100:.2f}%")
