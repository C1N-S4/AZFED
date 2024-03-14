import numpy as np

def extract_features(azfed_data):
    features = {}
    for scenario_name, azfed in azfed_data.items():
        energy_x = azfed['energy_x']
        energy_y = azfed['energy_y']
        energy_z = azfed['energy_z']

        # Ortalama enerji
        mean_energy_x = np.mean(energy_x)
        mean_energy_y = np.mean(energy_y)
        mean_energy_z = np.mean(energy_z)

        # Standart sapma
        std_energy_x = np.std(energy_x)
        std_energy_y = np.std(energy_y)
        std_energy_z = np.std(energy_z)

        # Maksimum enerji
        max_energy_x = np.max(energy_x)
        max_energy_y = np.max(energy_y)
        max_energy_z = np.max(energy_z)

        features[scenario_name] = {
            'mean_energy_x': mean_energy_x,
            'mean_energy_y': mean_energy_y,
            'mean_energy_z': mean_energy_z,
            'std_energy_x': std_energy_x,
            'std_energy_y': std_energy_y,
            'std_energy_z': std_energy_z,
            'max_energy_x': max_energy_x,
            'max_energy_y': max_energy_y,
            'max_energy_z': max_energy_z
        }
    return features

def main():
    from data_preprocessing import load_data, preprocess_data
    from azfed_calculation import azfed_calculation

    raw_data_folder = "../data/raw_data"
    data = load_data(raw_data_folder)
    processed_data = preprocess_data(data)
    azfed_data = azfed_calculation(processed_data)

    features = extract_features(azfed_data)
    print("Özellik çıkarımı tamamlandı.")
    print("Çıkarılan özellikler:")
    for scenario_name, scenario_features in features.items():
        print(f"Senaryo: {scenario_name}")
        for feature_name, feature_value in scenario_features.items():
            print(f"  {feature_name}: {feature_value}")

if __name__ == "__main__":
    main()