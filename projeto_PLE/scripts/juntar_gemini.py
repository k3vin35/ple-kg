import pandas as pd

# ==============================================================================
# 1. PREPARAR DADOS DOS PAÍSES (Detalhe para Mapas)
# ==============================================================================
mismanaged = pd.read_csv('datasets/mismanaged_plastic_waste_countries.csv')
emitted = pd.read_csv('datasets/emitted_countries.csv')
per_capita = pd.read_csv('datasets/percapita_countries.csv')
probability = pd.read_csv('datasets/probability_countries.csv')

# Juntar tudo (Merge)
df_countries = emitted.merge(per_capita, on=['Country', 'Year'], how='outer')
df_countries = df_countries.merge(probability, on=['Country', 'Year'], how='outer')
df_countries = df_countries.merge(mismanaged, on=['Country', 'Year'], how='outer')

# Criar a tal métrica de Microplásticos (assumindo que o que vai para o mar vira microplástico)
df_countries['Microplastics_Risk_Tonnes'] = df_countries['PlasticEmittedToOcean']

# Guardar
df_countries = df_countries.sort_values(['Country', 'Year'])
df_countries.to_csv('owid_plastic_countries.csv', index=False)
print("✅ Ficheiro 'owid_plastic_countries.csv' criado.")

# ==============================================================================
# 2. PREPARAR DADOS DAS REGIÕES (Histórico para Gráficos de Linha)
# ==============================================================================
# Certifica-te que guardaste os ficheiros das regiões na pasta datasets com estes nomes:
reg_emitted = pd.read_csv('datasets/emitted_regions.csv')
reg_mismanaged = pd.read_csv('datasets/mismanaged_plastic_waste_regions.csv')
reg_percapita = pd.read_csv('datasets/percapita_regions.csv')

# Juntar tudo (Merge)
df_regions = reg_mismanaged.merge(reg_emitted, on=['Country', 'Year'], how='outer')
df_regions = df_regions.merge(reg_percapita, on=['Country', 'Year'], how='outer')

# Mudar o nome de 'Country' para 'Region' para não confundir no PowerBI
df_regions = df_regions.rename(columns={'Country': 'Region'})

# Guardar
df_regions.to_csv('owid_plastic_regions.csv', index=False)
print("✅ Ficheiro 'owid_plastic_regions.csv' criado.")