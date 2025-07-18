import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tempfile
import os
from rekordbox_analysis.txt_reader import load_rekordbox_txt
from rekordbox_analysis.data_cleaning import clean_data
from rekordbox_analysis.playlist_optimizer import optimize_playlist
from visualization.playlist_visualizer import plot_bpm_energy_flow

# Page config
st.set_page_config(
    page_title="Curating the Perfect DJ Set",
    page_icon="🎵",
    layout="wide"
)

# Title and description
st.title("🎵 Curating the Perfect DJ Set")
st.markdown("Upload your Rekordbox .txt file to optimize your playlist for DJ mixing with harmonic compatibility and BPM progression.")

# File upload
uploaded_file = st.file_uploader(
    "Choose your Rekordbox .txt file",
    type=['txt'],
    help="Upload a .txt file exported from Rekordbox"
)

if uploaded_file is not None:
    # Get original filename without extension
    original_filename = os.path.splitext(uploaded_file.name)[0]
    
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name
    
    try:
        # Load and process tracks
        raw_tracks = load_rekordbox_txt(tmp_path)
        cleaned_tracks = clean_data(raw_tracks)
        
        # Display original playlist
        st.header("📋 Original Playlist")
        
        # Create DataFrame for display
        original_df = pd.DataFrame(cleaned_tracks)
        st.dataframe(
            original_df[['title', 'artist', 'bpm', 'key', 'camelot_key']],
            use_container_width=True
        )
        
        # Original playlist statistics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Tracks", len(cleaned_tracks))
        with col2:
            st.metric("Avg BPM", f"{np.mean([t['bpm'] for t in cleaned_tracks]):.1f}")
        with col3:
            st.metric("BPM Range", f"{min([t['bpm'] for t in cleaned_tracks])} - {max([t['bpm'] for t in cleaned_tracks])}")
        with col4:
            st.metric("Unique Keys", len(set([t['key'] for t in cleaned_tracks])))
        
        # Original playlist visualization
        st.header("📊 Original Playlist Energy Flow")
        fig_original = plot_bpm_energy_flow(cleaned_tracks)
        st.pyplot(fig_original)
        
        # Optimization
        st.header("🔄 Optimizing Playlist...")
        with st.spinner("Optimizing for DJ mixing..."):
            optimized_tracks = optimize_playlist(cleaned_tracks)
        
        # Display optimized playlist
        st.header("🎯 Optimized Playlist")
        
        # Create DataFrame for display
        optimized_df = pd.DataFrame(optimized_tracks)
        st.dataframe(
            optimized_df[['title', 'artist', 'bpm', 'key', 'camelot_key']],
            use_container_width=True
        )
        
        # Optimized playlist statistics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Tracks", len(optimized_tracks))
        with col2:
            st.metric("Avg BPM", f"{np.mean([t['bpm'] for t in optimized_tracks]):.1f}")
        with col3:
            st.metric("BPM Range", f"{min([t['bpm'] for t in optimized_tracks])} - {max([t['bpm'] for t in optimized_tracks])}")
        with col4:
            st.metric("Unique Keys", len(set([t['key'] for t in optimized_tracks])))
        
        # Optimized playlist visualization
        st.header("📊 Optimized Playlist Energy Flow")
        fig_optimized = plot_bpm_energy_flow(optimized_tracks)
        st.pyplot(fig_optimized)
        
        # Download optimized playlist
        st.header("💾 Download Optimized Playlist")
        
        # Create download data
        download_data = []
        for i, track in enumerate(optimized_tracks, 1):
            download_data.append({
                "Track #": i,
                "Title": track['title'],
                "Artist": track['artist'],
                "BPM": track['bpm'],
                "Key": track['key'],
                "Camelot Key": track['camelot_key']
            })
        
        download_df = pd.DataFrame(download_data)
        csv = download_df.to_csv(index=False)
        
        st.download_button(
            label="📥 Download Optimized Playlist as CSV",
            data=csv,
            file_name=f"{original_filename}_final.csv",
            mime="text/csv"
        )
        
        # Create .m3u8 content
        m3u_content = "#EXTM3U\n"
        for track in optimized_tracks:
            m3u_content += f"{track['title']} - {track['artist']}.mp3\n"

        # M3U8 download button
        st.download_button(
            label="🎶 Download as .M3U8 Playlist to import into Rekordbox",
            data=m3u_content,
            file_name=f"{original_filename}_final.m3u8",
            mime="application/x-mpegURL"
        )
        
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        st.info("Please make sure you're uploading a valid Rekordbox .txt file.")
    
    finally:
        # Clean up temporary file
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

else:
    # Instructions when no file is uploaded
    st.info("👆 Please upload a Rekordbox .txt file to get started!")
    
    st.markdown("""
    ### How to export from Rekordbox:
    1. Open Rekordbox
    2. Select your playlist
    3. Right-click → Export → Export as .txt
    4. Upload the .txt file here
    
    ### What the optimizer does:
    - **Harmonic Mixing**: Prioritizes compatible Camelot wheel keys
    - **BPM Progression**: Maintains ±3 BPM transitions
    - **Energy Flow**: Creates a bell curve energy progression
    - **DJ-Friendly**: Optimizes for smooth transitions
    """)

# Footer
st.markdown("---")
st.markdown("Built by Taran Elgin, AKA InDJnous") 