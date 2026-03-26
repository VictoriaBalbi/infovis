import pandas as pd
from tqdm import tqdm

from src.enrich_runtime import get_runtime
from src.enrich_genres import get_genres
from src.enrich_language import get_original_language
from src.enrich_popularity import get_popularity, categorize_popularity

def enrich_all(df):

   # runtimes = []
    genres = []
    langs = []
    pops = []
    category_popularity=[]

    for idx, row in tqdm(df.iterrows(), total=len(df), desc="Enriqueciendo TMDb"):
        title = row["clean_title2"]
        season = row["Season"]
        episode = row["Episode"]

        # runtime exacto
       # runtimes.append(get_runtime(title, season, episode))

        # estos no dependen del episodio 
        genres.append(get_genres(title))
        langs.append(get_original_language(title))
        pops.append(get_popularity(title))
       category_popularity.append(categorize_popularity(row["popularity"]))
   # df["runtime"] = runtimes
   
    df["genres"] = genres
        #df["original_language"] = langs
        #df["popularity"] = pops
    # df["popularity_category"] = category_popularity

    return df
