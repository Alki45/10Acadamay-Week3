import pandas as pd
import scipy.stats as stats

# Load the dataset
data = pd.read_csv('A:/10x/10X_Acadamy/Data/MachineLearningRating_v3/MachineLearningRating_v3.txt', delimiter='|') 

province_claims = data.groupby('Province')['TotalClaims'].mean()
t_stat, p_value = stats.ttest_ind(data[data['Province'] == 'Province1']['TotalClaims'],
                                   data[data['Province'] == 'Province2']['TotalClaims'])

print(f'T-test for Province Risk Differences: T-statistic = {t_stat}, P-value = {p_value}')
