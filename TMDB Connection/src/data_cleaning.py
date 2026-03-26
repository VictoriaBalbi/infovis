import re
import pandas as pd
import numpy as np

def clean_title(title):
    # 1. Quitar cualquier "(episodio X)" o "(Resumen)" o "(Tráiler)"
    title = re.sub(r"\(.*?\)", "", title)

    # 2. Quitar "Temporada X" y "Episodio X"
    title = re.sub(r":\s*Temporada\s*\d+", "", title, flags=re.IGNORECASE)
    title = re.sub(r":\s*Episodio\s*\d+", "", title, flags=re.IGNORECASE)

    # 3. Separar por ":"
    parts = [p.strip() for p in title.split(":")]

    # --- CASO 1: Si el segundo bloque es "Miniserie" → devolver solo el primero ---
    if len(parts) >= 2 and re.match(r"miniserie", parts[1], flags=re.IGNORECASE):
        return parts[0]

    # --- CASO 2: Si hay sub-show real (como "Dentro de ...") → devolver los dos primeros ---
    if len(parts) >= 2:
        return f"{parts[0]}: {parts[1]}"

    # --- CASO 3: Solo un bloque ---
    return parts[0]


def clean_title_first_sentence(title):
    # 1. Quitar cualquier "(episodio X)" o "(Resumen)" o "(Tráiler)"
    title = re.sub(r"\(.*?\)", "", title)

    # 2. Quitar "Temporada X" y "Episodio X"
    title = re.sub(r":\s*Temporada\s*\d+", "", title, flags=re.IGNORECASE)
    title = re.sub(r":\s*Episodio\s*\d+", "", title, flags=re.IGNORECASE)

    # 3. Separar por ":" y devolver solo lo anterior al primer bloque
    parts = [p.strip() for p in title.split(":")]
    return parts[0]


def season_episode(title):
    # Buscar temporada explícita
    season = re.search(r"Temporada\s*(\d+)", title, flags=re.IGNORECASE)
    season = int(season.group(1)) if season else None

    # Buscar episodio explícito
    episode = re.search(r"\(episodio\s*(\d+)\)", title, flags=re.IGNORECASE)
    if not episode:
        episode = re.search(r"Episodio\s*(\d+)", title, flags=re.IGNORECASE)
    episode = int(episode.group(1)) if episode else None

    # Si hay episodio pero no temporada → asumir temporada 1
    if episode is not None and season is None:
        season = 1

    return season, episode


def classify_row(row):
    # 1. Si ya tiene valor (TRAILER, HOOK, RECAP, etc.) → NO tocar
    if pd.notna(row["Supplemental Video Type"]) and row["Supplemental Video Type"] != "":
        return row["Supplemental Video Type"]
    
    # 2. Si NO tiene temporada → FILM
    if pd.isna(row["Season"]) or row["Season"] == "":
        return "FILM"
    
    # 3. Si tiene temporada → SERIE
    return "SERIE"



