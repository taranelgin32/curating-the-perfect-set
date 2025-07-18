import matplotlib.pyplot as plt
import numpy as np

def plot_bpm_energy_flow(tracks):
    """Plot BPM progression to show energy flow across the playlist."""
    track_numbers = range(1, len(tracks) + 1)
    bpms = [track['bpm'] for track in tracks]
    camelot_keys = [track['camelot_key'] for track in tracks]
    
    plt.figure(figsize=(12, 6))
    
    # Plot BPM line
    plt.plot(track_numbers, bpms, 'o-', linewidth=2, markersize=8, color='#FF6B6B')
    
    # Color code by Camelot key
    unique_keys = list(set(camelot_keys))
    colors = plt.cm.Set3(np.linspace(0, 1, len(unique_keys)))
    key_colors = dict(zip(unique_keys, colors))
    
    for i, (bpm, camelot) in enumerate(zip(bpms, camelot_keys)):
        plt.scatter(i + 1, bpm, color=key_colors[camelot], s=100, zorder=5)
    
    # Add track titles as annotations
    for i, track in enumerate(tracks):
        plt.annotate(f"{track['title'][:20]}...", 
                    (i + 1, track['bpm']), 
                    xytext=(0, 10), textcoords='offset points',
                    ha='center', fontsize=8, rotation=45)
    
    # Add Camelot key legend
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                                  markerfacecolor=key_colors[key], markersize=10, label=key)
                      for key in unique_keys]
    plt.legend(handles=legend_elements, title="Camelot Keys", loc='upper right')
    
    plt.xlabel('Track Number')
    plt.ylabel('BPM')
    plt.title('Playlist Energy Flow (BPM Progression)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt

def analyze_playlist(tracks):
    """Generate playlist analysis with BPM energy flow visualization."""
    print(f"Playlist Analysis for {len(tracks)} tracks")
    print(f"Average BPM: {np.mean([t['bpm'] for t in tracks]):.1f}")
    print(f"BPM Range: {min([t['bpm'] for t in tracks])} - {max([t['bpm'] for t in tracks])}")
    print(f"Unique Keys: {len(set([t['key'] for t in tracks]))}")
    
    # Create BPM Energy Flow plot
    plot_bpm_energy_flow(tracks)
    plt.savefig('bpm_energy_flow.png', dpi=300, bbox_inches='tight')
    plt.show()
    return plt 