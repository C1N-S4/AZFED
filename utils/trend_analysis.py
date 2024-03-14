def analyze_trends(features):
    trends = {}
    for scenario_name, scenario_features in features.items():
        energy_x = scenario_features['mean_energy_x']
        energy_y = scenario_features['mean_energy_y']
        energy_z = scenario_features['mean_energy_z']

        trends[scenario_name] = {
            'energy_x': energy_x,
            'energy_y': energy_y,
            'energy_z': energy_z
        }
    return trends

def main():
    from data_preprocessing import load_data, preprocess_data
    from azfed_calculation import azfed_calculation
    from feature_extraction import extract_features

    raw_data_folder = "../data/raw_data"
    data = load_data(raw_data_folder)
    processed_data = preprocess_data(data)
    azfed_data = azfed_calculation(processed_data)
    features = extract_features(azfed_data)

    trends = analyze_trends(features)
    print("Trend analizi tamamlandı.")
    print("Trend sonuçları:")
    for scenario_name, scenario_trends in trends.items():
        print(f"Senaryo: {scenario_name}")
        for trend_name, trend_value in scenario_trends.items():
            print(f"  {trend_name}: {trend_value}")

if __name__ == "__main__":
    main()