
def load_rekordbox_txt(file_path):
    tracks = []
    with open(file_path, 'r', encoding='utf-16') as f:
        lines = f.readlines()
    #loop through lines and find the header index
    header_index = None
    for i, line in enumerate(lines):
        if "Track Title" in line and "Artist" in line:
            header_index = i
            break
    # if header line is not found, raise an error
    if header_index is None:
        raise ValueError("Header not found in the file")
    #strip and split the header line into a list of headers    
    headers = lines[header_index].strip().split('\t')
    data_lines = lines[header_index + 1:]

    for line in data_lines:
        if not line.strip():
            continue #skip the empty lines
        #split each row and match to the header
        values = line.strip().split('\t')
        if len(values) != len(headers):
            continue #skip the line if the # values doesn't match # headers
        # create a hashmap of headers and values and add to the tracks list
        track_info = dict(zip(headers, values))
        tracks.append({
            "title": track_info.get("Track Title", ""),
            "artist": track_info.get("Artist", ""),
            "bpm": track_info.get("BPM", ""),
            "key": track_info.get("Key", "")
        })
    return tracks


    
