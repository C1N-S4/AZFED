# AZFED Algorithm: A Novel Approach to UAV Vibration Data Analysis

AZFED (Adaptive Time-Frequency Energy Distribution) is a comprehensive algorithm designed to analyze vibration data from UAVs (Unmanned Aerial Vehicles). This repository contains the Python implementation of the AZFED algorithm, sample datasets, and related documentation.

## Features

- Data preprocessing: Load, clean, and filter raw vibration data
- Wavelet transform: Perform time-frequency analysis of vibration signals
- AZFED calculation: Adaptively compute the time-frequency distribution of vibration energy
- Feature extraction: Calculate statistical features for analysis and extraction
- Anomaly detection: Identify anomalous conditions in vibration data
- Trend analysis: Reveal long-term changes in vibration behavior

## Requirements

- Python 3.7+
- NumPy
- SciPy
- Matplotlib
- PyWavelets

## Installation

1. Clone the repository: git clone https://github.com/C1N-S4/azfed-algorithm.git
2. Install the required libraries: pip install -r requirements.txt
3. Run the algorithm with the example datasets: python main.py

## Usage

1. Add your raw vibration data to the `data/raw_data` folder.
2. Adjust the algorithm parameters in the `config.py` file, if needed.
3. Use the `main.py` file to run the algorithm.
4. Results will be available in the `results` folder.



