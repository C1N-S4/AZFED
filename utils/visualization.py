import matplotlib.pyplot as plt

def visualize_results(features, anomalies, trends):
    scenarios = list(features.keys())
    energy_x = [features[scenario]['mean_energy_x'] for scenario in scenarios]
    energy_y = [features[scenario]['mean_energy_y'] for scenario in scenarios]
    energy_z = [features[scenario]['mean_energy_z'] for scenario in scenarios]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(scenarios, energy_x, label='Energy X')
    ax.bar(scenarios, energy_y, bottom=energy_x, label='Energy Y')
    ax.bar(scenarios, energy_z, bottom=[x + y for x, y in zip(energy_x, energy_y)], label='Energy Z')
    ax.set_xlabel('Scenarios')
    ax.set_ylabel('Energy')
    ax.set_title('Energy Distribution by Scenario')
    ax.legend()

    plt.tight_layout()
    plt.show()

def main():
    from data_preprocessing import load_data, preprocess_data
    from azfed_calculation import azfed_calculation
    from feature_extraction import extract_features
    from anomaly_detection import detect_anomalies
    from trend_analysis import analyze_trends

    raw_data_folder = "../data/raw_data"
    data = load_data(raw_data_folder)
    processed_data = preprocess_data(data)
    azfed_data = azfed_calculation(processed_data)
    features = extract_features(azfed_data)
    anomalies = detect_anomalies(features)
    trends = analyze_trends(features)

    visualize_results(features, anomalies, trends)

if __name__ == "__main__":
    main()