import os
from rekordbox_analysis.txt_reader import load_rekordbox_txt
from rekordbox_analysis.data_cleaning import clean_data
from rekordbox_analysis.playlist_optimizer import optimize_playlist
from visualization.playlist_visualizer import analyze_playlist

if __name__ == "__main__":
    file_path = input("Enter the path to your Rekordbox .txt file: ").strip()
    if not os.path.exists(file_path):
        print("File not Found, please try again.")
        exit()
    raw_tracks = load_rekordbox_txt(file_path)
    
    # Clean and add Camelot keys
    cleaned_tracks = clean_data(raw_tracks)
    
    print("\n🎵 Original Playlist:")
    for track in cleaned_tracks:
        artist = track['artist']
        if artist:
            print(f"{track['title']} by {artist} (BPM: {track['bpm']}, Key: {track['key']}, Camelot Key: {track['camelot_key']})")
        else:
            print(f"{track['title']} (BPM: {track['bpm']}, Key: {track['key']}, Camelot Key: {track['camelot_key']})")
    
    # Generate original playlist analysis and visualization
    print("\n Playlist Analysis:")
    analyze_playlist(cleaned_tracks)
    
    # Optimize playlist for DJ mixing
    print("\n Optimizing playlist for DJ mixing...")
    optimized_tracks = optimize_playlist(cleaned_tracks)
    
    print("\n Optimized Playlist:")
    for track in optimized_tracks:
        artist = track['artist']
        if artist:
            print(f"{track['title']} by {artist} (BPM: {track['bpm']}, Key: {track['key']}, Camelot Key: {track['camelot_key']})")
        else:
            print(f"{track['title']} (BPM: {track['bpm']}, Key: {track['key']}, Camelot Key: {track['camelot_key']})")
    
    # Generate optimized playlist visualization
    analyze_playlist(optimized_tracks)