import numpy as np

def detect_anomalies(features, threshold=2.0):
    anomalies = {}
    for scenario_name, scenario_features in features.items():
        mean_energy_x = scenario_features['mean_energy_x']
        mean_energy_y = scenario_features['mean_energy_y']
        mean_energy_z = scenario_features['mean_energy_z']
        std_energy_x = scenario_features['std_energy_x']
        std_energy_y = scenario_features['std_energy_y']
        std_energy_z = scenario_features['std_energy_z']

        # Anomali hesaplaması öncesinde koşulları yazdır
        print(f"{scenario_name} için mean_energy_y: {mean_energy_y}, hesaplanan eşik: {threshold * std_energy_y}")

        anomaly_x = mean_energy_x > threshold * std_energy_x
        anomaly_y = mean_energy_y > threshold * std_energy_y
        anomaly_z = mean_energy_z > threshold * std_energy_z

        anomalies[scenario_name] = {
            'anomaly_x': anomaly_x,
            'anomaly_y': anomaly_y,
            'anomaly_z': anomaly_z
        }
    return anomalies



def main():
    from data_preprocessing import load_data, preprocess_data
    from azfed_calculation import azfed_calculation
    from feature_extraction import extract_features

    raw_data_folder = "../data/raw_data"
    data = load_data(raw_data_folder)
    processed_data = preprocess_data(data)
    azfed_data = azfed_calculation(processed_data)
    features = extract_features(azfed_data)

    anomalies = detect_anomalies(features)
    print("Anomali tespiti tamamlandı.")
    print("Anomali sonuçları:")
    for scenario_name, scenario_anomalies in anomalies.items():
        print(f"Senaryo: {scenario_name}")
        for anomaly_name, anomaly_value in scenario_anomalies.items():
            print(f"  {anomaly_name}: {anomaly_value}")

if __name__ == "__main__":
    main()