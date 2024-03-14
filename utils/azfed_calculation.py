import numpy as np

def azfed_calculation(processed_data, window_size=10):
    azfed_data = {}
    for scenario_name, scenario_data in processed_data.items():
        accelerometer_data = scenario_data["accelerometer_data"]
        energy_x = []
        energy_y = []
        energy_z = []
        for i in range(0, len(accelerometer_data["timestamp"]), window_size):
            window_x = accelerometer_data["accelerometer_x"][i:i+window_size]
            window_y = accelerometer_data["accelerometer_y"][i:i+window_size]
            window_z = accelerometer_data["accelerometer_z"][i:i+window_size]
            energy_x.append(np.sum(np.square(window_x)))
            energy_y.append(np.sum(np.square(window_y)))
            energy_z.append(np.sum(np.square(window_z)))
        azfed_data[scenario_name] = {
            'energy_x': energy_x,
            'energy_y': energy_y,
            'energy_z': energy_z
        }
    return azfed_data

def main():
    from data_preprocessing import load_data, preprocess_data

    raw_data_folder = "../data/raw_data"
    data = load_data(raw_data_folder)
    processed_data = preprocess_data(data)

    azfed_data = azfed_calculation(processed_data)
    print("AZFED hesaplaması tamamlandı.")
    print("AZFED verileri:")
    for scenario_name, azfed in azfed_data.items():
        print(f"Senaryo: {scenario_name}")
        print(f"  Energy X: {azfed['energy_x']}")
        print(f"  Energy Y: {azfed['energy_y']}")
        print(f"  Energy Z: {azfed['energy_z']}")

if __name__ == "__main__":
    main()