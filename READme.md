# Curating the Perfect Set - DJ Playlist Optimizer

Transform your Rekordbox playlists into perfectly optimized DJ sets using advanced harmonic mixing algorithms.

## 🎯 What It Does

Curating the Perfect Set automatically reorganizes your DJ playlists to create smooth, professional sets by:

- **Harmonic Mixing**: Prioritizes compatible musical keys using the Camelot wheel
- **BPM Flow**: Maintains smooth energy progression (±3 BPM transitions)
- **Energy Curve**: Creates a natural bell curve from start to finish
- **Visual Analysis**: Shows energy flow and key progression with interactive charts

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install streamlit pandas matplotlib numpy
```

### 2. Run the Web App
```bash
streamlit run app.py
```

### 3. Upload & Optimize
1. Export your playlist from Rekordbox as .txt
2. Upload the file to the web app
3. View the optimization results
4. Download your optimized playlist

## 📁 Project Structure

```
ThePerfectSet/
├── app.py                          # Web interface
├── main.py                         # Command line version
├── requirements.txt                 # Dependencies
├── rekordbox_analysis/             # Core processing
│   ├── txt_reader.py              # File parser
│   ├── data_cleaning.py           # Data normalization
│   ├── camelot_wheel.py           # Key compatibility
│   └── playlist_optimizer.py      # Optimization engine
├── visualization/                  # Charts and graphs
│   └── playlist_visualizer.py     # Energy flow visualization
└── sample_files/                  # Example playlists
```

## 🎵 How It Works

### Optimization Algorithm

1. **Key Compatibility (Primary)**
   - Same key: Perfect match (score: 30)
   - Adjacent keys: Good mix (score: 20)
   - Relative minor/major: Compatible (score: 20)
   - Distant keys: Avoided (score: 0)

2. **BPM Progression (Secondary)**
   - Maximum jump: ±3 BPM between tracks
   - Energy curve: Bell shape with peak at 75%
   - Start slow, build up, peak, wind down

3. **Track Selection**
   - Prioritizes harmonic compatibility
   - Respects BPM constraints
   - Creates natural energy flow

### Example Optimization

**Before:**
```
Track 1: 125 BPM, Key: C (8B)
Track 2: 128 BPM, Key: F (7B)  ← Poor key transition
Track 3: 122 BPM, Key: Am (8A) ← Bad BPM jump
```

**After:**
```
Track 1: 125 BPM, Key: C (8B)
Track 2: 126 BPM, Key: G (9B)  ← Compatible key
Track 3: 127 BPM, Key: D (10B) ← Smooth progression
```

## 📊 Features

### Web Interface
- **Drag & Drop Upload**: Simple file upload
- **Real-time Analysis**: Instant playlist statistics
- **Visual Charts**: Energy flow with key colors
- **Dual Export**: CSV and M3U8 formats
- **Smart Naming**: Adds "_final" to original filename

### Command Line
```bash
python main.py
# Enter file path when prompted
```

## 🎨 Visualizations

### Energy Flow Chart
- **X-axis**: Track position in set
- **Y-axis**: BPM progression
- **Colors**: Camelot wheel positions
- **Annotations**: Track titles

### Statistics Dashboard
- Track count and average BPM
- BPM range and unique keys
- Before/after comparison

## 📤 Export Formats

### CSV Export
```csv
Track #,Title,Artist,BPM,Key,Camelot Key
1,Like This,Adam Ten,125.0,Eb,5B
2,Oxytocin Remix,Adam Ten,126.0,G,9B
```

### M3U8 Export
```m3u8
#EXTM3U
Like This - Adam Ten.mp3
Oxytocin Remix - Adam Ten.mp3
```

## 🔧 Technical Details

### Supported Input
- Rekordbox .txt exports
- Tab-separated format
- UTF-16 encoding

### Algorithm Performance
- **Time Complexity**: O(n²) for n tracks
- **Memory Usage**: Linear with playlist size
- **Optimization**: Single-pass greedy algorithm

### Key Compatibility Matrix
| Relationship | Score | Description |
|-------------|-------|-------------|
| Same Key | 30 | Perfect harmonic match |
| Adjacent | 20 | Smooth key transition |
| Relative | 20 | Minor/major relationship |
| Distant | 0 | Avoided in optimization |

## 🛠️ Development

### Adding New Features
```python
# New optimization strategy
def custom_optimizer(tracks):
    # Your algorithm here
    return optimized_tracks

# New visualization
def custom_chart(tracks):
    # Your chart here
    return matplotlib_figure
```

### Testing
```bash
# Test optimization engine
python -c "from rekordbox_analysis.playlist_optimizer import optimize_playlist; print('✅ Engine loaded')"
```

## 📝 License

This project is proprietary software developed by Taran Elgin.

---

**Curating the Perfect Set** - Advanced DJ Technology Solutions

