from src.tmdb_connection import search_title, get_details

def get_original_language(title):
    item = search_title(title)
    if not item:
        return None

    details = get_details(item["media_type"], item["id"])
    return details.get("original_language")