from src.tmdb_connection import search_title, get_details

def get_genres(title):
    item = search_title(title)
    if not item:
        return None

    details = get_details(item["media_type"], item["id"])
    genres = details.get("genres", [])
    return [g["name"] for g in genres] if genres else None
