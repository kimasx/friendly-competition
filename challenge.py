import pandas

jobs = pandas.read_csv('./NYC_jobs.csv')

# group data by type of Agency
agencies = jobs.groupby('Agency')
jobs = []

for name, group in agencies:
  print(name, len(group['Business Title'].unique()))
  jobs.append((name, group['# Of Positions'].sum()))

# print sorted(jobs, key=lambda x: x[1])