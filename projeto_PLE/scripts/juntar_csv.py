import pandas as pd

mismanaged = pd.read_csv('datasets/mismanaged_plastic_waste_countries.csv')
emitted = pd.read_csv('datasets/emitted_countries.csv')
per_capita = pd.read_csv('datasets/percapita_countries.csv')
probability = pd.read_csv('datasets/probability_countries.csv')


print(mismanaged.columns)
print(emitted.columns)
print(per_capita.columns)
print(probability.columns)


merged = emitted.merge(
    per_capita,
    on=['Country', 'Year'],
    how='outer'
)


merged = merged.merge(
    probability,
    on=['Country', 'Year'],
    how='outer'
)


merged = merged.merge(
    mismanaged,
    on=['Country', 'Year'],
    how='outer'
)

merged = merged.sort_values(['Country', 'Year'])
merged.to_csv('owid_plastic_final.csv', index=False)

print(merged.head())
print(merged.info())

