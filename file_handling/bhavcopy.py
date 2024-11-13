import pandas as pd
cm = pd.read_csv('sec_bhavdata_full_12112024.csv')
cm.columns = cm.columns.str.strip()
cm = cm.applymap(lambda x: x.strip() if isinstance(x, str) else x)

print(cm[cm['SERIES'] == 'BE'])
