import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
# mini project engineering economics

# Project parameters 
initial_cost = 300_000_000 #initial investment cost
savings = 100_000_000 #saving cost 
maintenance = 15_000_000 #maintenancase cost
residual_value = 30_000_000 # rv at the end of the 10th year
discount_rate = 0.10 #discount rate
years = 11 #project period

# annual cashflows
cash_flows = [-initial_cost]
for year in range(1, years + 1):
    net_cash = savings - maintenance
    if year == years:
        net_cash += residual_value
    cash_flows.append(net_cash)

# Net present value
npv = sum(cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows))

# Internal rate of return
irr = npf.irr(cash_flows)

# Payback period
cumulative = 0
payback_year = None
for i, cf in enumerate(cash_flows[1:], start=1):
    cumulative += cf
    if cumulative >= initial_cost:
        payback_year = i
        break

# Output
print("Cash Flows:", cash_flows)
print(f"NPV = Rp {npv:,.2f}")
print(f"IRR = {irr*100:.2f}%")
print(f"Payback Period = {payback_year} tahun")

# 📊 Plot cash flows
years_list = list(range(0, years + 1))
plt.figure(figsize=(10, 6))
plt.bar(years_list, cash_flows, color='orange')
plt.axhline(0, color='black', linewidth=0.8)
plt.title("Project Cash Flows Graphic")
plt.xlabel("Year")
plt.ylabel("Cash Flows (Rp)")
plt.xticks(years_list)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()