import pandas as pd
from src.enrichment_flow import enrich_all
from src.data_cleaning import clean_title,season_episode,classify_row,clean_title_first_sentence

df = pd.read_excel("data/generosFaltantes.xlsx")

df["clean_title"] = df["Title"].apply(clean_title)
df[["Season", "Episode"]] = df["Title"].apply(season_episode).apply(pd.Series)
df["Supplemental Video Type"] = df.apply(classify_row, axis=1)

df = enrich_all(df)

df.to_excel("output/Dataset_output.xlsx", index=False)
print("Archivo final generado.")

