import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

online_shop = pd.read_csv ("/mnt/research/NOS_mri/CSE801A_Spring2024_A2/online_shoppers_intention.csv")

#Boxplot comparison, filtering out the bounce rates of 0
df = online_shop[online_shop['BounceRates'] > 0]

plt.figure(figsize=(10, 6))
sns.boxplot(x='VisitorType', y='BounceRates', data=df)
plt.title('Bounce Rate by Visitor Type')
plt.xlabel('Visitor Type')
plt.ylabel('Bounce Rate')
plt.show()

#statistical comparison to see if there is a significant difference in the bounce rates of new visitors versus returning visitors.
new_visitors = df[df['VisitorType'] == 'New_Visitor']['BounceRates']
returning_visitors = df[df['VisitorType'] == 'Returning_Visitor']['BounceRates']

# Perform t-test
t_statistic, p_value = ttest_ind(new_visitors, returning_visitors)

print(f"t-test result: p-value = {p_value}")

# Hypothesis
alpha = 0.05
if p_value < alpha:
    print("Null Hypothesis (H0): There is no significant difference in bounce rates between new visitors and returning visitors")
    print("Alternative Hypothesis (H1): There is a significant difference in bounce rates between new visitors and returning visitors")
else:
    print("Null Hypothesis (H0): There is a significant difference in bounce rates between new visitors and returning visitors")
    print("Alternative Hypothesis (H1): There is no significant difference in bounce rates between new visitors and returning visitors")

# Interpretation
if p_value < alpha:
    print(f"Result: We reject the null hypothesis as the p-value ({p_value:.4f}) is less than alpha ({alpha}).")
    print("Conclusion: There is a significant difference in bounce rates between new visitors and returning visitors.")
else:
    print(f"Result: We fail to reject the null hypothesis as the p-value ({p_value:.4f}) is greater than alpha ({alpha}).")
    print("Conclusion: There is no significant difference in bounce rates between new visitors and returning visitors.")
