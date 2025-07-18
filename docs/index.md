# Curating the Perfect Set

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-red)](https://curating-the-perfect-set-taranelgin32.streamlit.app)

## 🎵 Advanced DJ Playlist Optimization

Transform your Rekordbox playlists into perfectly optimized DJ sets using advanced harmonic mixing algorithms.

### 🚀 Live Demo

**Try it now:** [Curating the Perfect Set Web App](https://curating-the-perfect-set-taranelgin32.streamlit.app)

### ✨ Key Features

- **Harmonic Mixing**: Prioritizes compatible musical keys using the Camelot wheel
- **BPM Flow**: Maintains smooth energy progression (±3 BPM transitions)
- **Energy Curve**: Creates a natural bell curve from start to finish
- **Visual Analysis**: Shows energy flow and key progression with interactive charts
- **Dual Export**: CSV and M3U8 formats for easy import back to Rekordbox

### 🚀 Quick Start

```bash
# Install dependencies
pip install streamlit pandas matplotlib numpy

# Run the web app
streamlit run app.py
```

### 🎯 How It Works

The algorithm optimizes your playlist by:

1. **Analyzing Key Compatibility**: Uses the Camelot wheel to find harmonic matches
2. **Managing BPM Flow**: Ensures smooth transitions (±3 BPM rule)
3. **Creating Energy Curves**: Builds natural progression from start to finish
4. **Visualizing Results**: Shows energy flow with color-coded keys

### 📊 Example Optimization

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

### 🛠️ Technology Stack

- **Python**: Core optimization algorithms
- **Streamlit**: Web application interface
- **Matplotlib**: Data visualization
- **Pandas**: Data manipulation
- **NumPy**: Numerical computations

### 📈 Performance

- **Processing Time**: O(n²) for n tracks
- **Memory Usage**: Linear with playlist size
- **Optimization**: Single-pass greedy algorithm
- **Compatibility**: Full Rekordbox .txt support

### 🎨 Visualizations

The app provides:
- **Energy Flow Charts**: BPM progression with key colors
- **Statistics Dashboard**: Track count, average BPM, key distribution
- **Before/After Comparison**: Optimization metrics

### 📤 Export Options

- **CSV Format**: For data analysis and spreadsheets
- **M3U8 Format**: For direct import into Rekordbox
- **Smart Naming**: Adds "_final" to original filename

### 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/taranelgin32/curating-the-perfect-set.git
cd curating-the-perfect-set

# Install dependencies
pip install -r requirements.txt

# Run the web app
streamlit run app.py
```

### 🎵 Supported Formats

**Input:**
- Rekordbox .txt exports
- Tab-separated format
- UTF-16 encoding

**Output:**
- CSV with track metadata
- M3U8 playlist files
- Energy flow visualizations

### 🤝 Contributing

This project is open for contributions! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

### 📝 License

This project is proprietary software developed by Taran Elgin.

---

**Built by Taran Elgin aka InDJnous** - Advanced DJ Technology Solutions 