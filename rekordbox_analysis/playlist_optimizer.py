import numpy as np
from .camelot_wheel import CAMELOT_KEY_MAP

def get_camelot_compatibility(key1, key2):
    """Check if two Camelot keys are compatible for mixing."""
    if key1 == key2:
        return 3  # Perfect match
    
    # Get numeric positions (1-12 for each wheel)
    try:
        pos1 = int(key1[:-1])  # Extract number from "5B"
        wheel1 = key1[-1]       # Extract A/B from "5B"
        pos2 = int(key2[:-1])
        wheel2 = key2[-1]
        
        # Same wheel: adjacent positions are compatible
        if wheel1 == wheel2:
            diff = abs(pos1 - pos2)
            if diff == 1 or diff == 11:  # Adjacent or wrap-around
                return 2  # Good compatibility
            elif diff == 2 or diff == 10:  # Two positions apart
                return 1  # Moderate compatibility
            else:
                return 0  # Poor compatibility
        
        # Different wheels: relative minors/majors
        if wheel1 != wheel2:
            if pos1 == pos2:  # Same position, different wheel
                return 2  # Relative minor/major - good compatibility
            else:
                return 0  # Poor compatibility
                
    except (ValueError, IndexError):
        return 0  # Invalid key format
    
    return 0

def optimize_playlist(tracks):
    """Optimize playlist for DJ mixing with harmonic compatibility prioritized over BPM."""
    if len(tracks) < 2:
        return tracks
    
    # Sort tracks by BPM for energy curve planning
    sorted_by_bpm = sorted(tracks, key=lambda x: x['bpm'])
    
    # Create energy curve: start slow, build up, peak in middle/end, slow down
    n_tracks = len(tracks)
    
    # Define target BPM curve (bell curve shape)
    target_bpms = []
    if n_tracks <= 3:
        # Simple progression for small playlists
        target_bpms = [sorted_by_bpm[0]['bpm'], 
                      sorted_by_bpm[-1]['bpm'] if n_tracks > 1 else sorted_by_bpm[0]['bpm'],
                      sorted_by_bpm[1]['bpm'] if n_tracks > 2 else sorted_by_bpm[-1]['bpm']]
    else:
        # Bell curve for larger playlists
        min_bpm = sorted_by_bpm[0]['bpm']
        max_bpm = sorted_by_bpm[-1]['bpm']
        
        # Create bell curve with peak around 70-80% through the set
        peak_position = 0.75  # Peak at 75% through the set
        
        for i in range(n_tracks):
            # Normalized position (0 to 1)
            pos = i / (n_tracks - 1)
            
            # Bell curve: start low, peak in middle, end low
            if pos <= peak_position:
                # Rising phase
                curve_pos = pos / peak_position
                target_bpm = min_bpm + (max_bpm - min_bpm) * curve_pos
            else:
                # Falling phase
                curve_pos = (pos - peak_position) / (1 - peak_position)
                target_bpm = max_bpm - (max_bpm - min_bpm) * curve_pos
            
            target_bpms.append(target_bpm)
    
    # Build optimized playlist
    optimized_tracks = []
    used_indices = set()
    
    # Start with the track closest to the first target BPM
    first_target = target_bpms[0]
    best_start = min(range(len(tracks)), 
                    key=lambda i: abs(tracks[i]['bpm'] - first_target))
    
    optimized_tracks.append(tracks[best_start])
    used_indices.add(best_start)
    
    # Build the rest of the playlist
    for i in range(1, n_tracks):
        current_track = optimized_tracks[-1]
        target_bpm = target_bpms[i]
        
        best_next = None
        best_score = -1
        
        # Find the best next track - PRIORITIZE KEY COMPATIBILITY
        for j, track in enumerate(tracks):
            if j in used_indices:
                continue
            
            # Calculate compatibility score - KEY FIRST, then BPM
            key_compatibility = get_camelot_compatibility(
                current_track['camelot_key'], 
                track['camelot_key']
            )
            bpm_diff = abs(track['bpm'] - target_bpm)
            
            # BPM constraint: must be within ±3 BPM
            if bpm_diff > 3:
                continue
            
            # Prioritize key compatibility over BPM
            # Key compatibility is worth 10x more than BPM closeness
            key_score = key_compatibility * 10  # 0, 10, 20, or 30
            bpm_score = max(0, 3 - bpm_diff)   # 0 to 3
            
            total_score = key_score + bpm_score
            
            if total_score > best_score:
                best_score = total_score
                best_next = j
        
        # If no track fits BPM constraint, find closest
        if best_next is None:
            best_next = min([j for j in range(len(tracks)) if j not in used_indices],
                          key=lambda j: abs(tracks[j]['bpm'] - target_bpm))
        
        optimized_tracks.append(tracks[best_next])
        used_indices.add(best_next)
    
    return optimized_tracks

