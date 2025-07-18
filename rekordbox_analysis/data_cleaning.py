from .camelot_wheel import CAMELOT_KEY_MAP

def clean_data(tracks):
    cleaned_tracks = []
    for track in tracks:
        try:
            bpm = float(track.get('bpm', 0))
        except ValueError:
            bpm = 0.0

        key = normalize_key(track.get('key', ''))
        camelot = CAMELOT_KEY_MAP.get(key, "Unknown")

        cleaned_tracks.append({
            "title": track.get("title", ""),
            "artist": track.get("artist", ""),
            "bpm": bpm,
            "key": key,
            "camelot_key": camelot
        })
    
    return cleaned_tracks

def normalize_key(key):
    #Standardize key names and spellings
    if not key:
        return ""

    key = key.strip().replace("♭", "b").replace("♯", "#").lower()

    # Capitalize properly, e.g., "ebm" → "Ebm"
    if "m" in key:
        note = key.replace("m", "").capitalize()
        return f"{note}m"
    else:
        return key.capitalize()