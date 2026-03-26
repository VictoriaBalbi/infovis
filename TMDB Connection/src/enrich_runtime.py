from src.tmdb_connection import search_title, get_details, safe_get, API_KEY

def get_runtime(title, season=None, episode=None):
    item = search_title(title)
    if not item:
        return None

    media_type = item["media_type"]
    tmdb_id = item["id"]

    if media_type == "movie":
        details = get_details("movie", tmdb_id)
        return details.get("runtime")

    if media_type == "tv":
        if season and episode:
            ep = safe_get(
                f"https://api.themoviedb.org/3/tv/{tmdb_id}/season/{season}/episode/{episode}",
                {"api_key": API_KEY}
            )
            if ep and ep.get("runtime"):
                return ep["runtime"]

        details = get_details("tv", tmdb_id)
        runtimes = details.get("episode_run_time", [])
        return runtimes[0] if runtimes else None
    

def find_episode_by_name(tv_id, title):
    # Obtener todas las temporadas
    details = get_details("tv", tv_id)
    seasons = details.get("seasons", [])

    for season in seasons:
        season_number = season["season_number"]

        # Obtener episodios de la temporada
        season_data = safe_get(
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}",
            {"api_key": API_KEY}
        )

        if not season_data or "episodes" not in season_data:
            continue

        for ep in season_data["episodes"]:
            # Comparo por nombre
            if ep["name"].lower() == title.lower():
                return season_number, ep["episode_number"], ep.get("runtime")

    return None, None, None

