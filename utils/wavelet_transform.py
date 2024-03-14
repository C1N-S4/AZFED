import pywt

def perform_wavelet_transform(data, wavelet='db4', level=2):
    coefficients = {}
    for scenario_name, scenario_data in data.items():
        accelerometer_data = scenario_data["accelerometer_data"]
        coeffs_x = pywt.wavedec(accelerometer_data["accelerometer_x"], wavelet, level=level)
        coeffs_y = pywt.wavedec(accelerometer_data["accelerometer_y"], wavelet, level=level)
        coeffs_z = pywt.wavedec(accelerometer_data["accelerometer_z"], wavelet, level=level)
        coefficients[scenario_name] = {
            "coeffs_x": coeffs_x,
            "coeffs_y": coeffs_y,
            "coeffs_z": coeffs_z
        }
    return coefficients

def main():
    from data_preprocessing import load_data, preprocess_data

    raw_data_folder = "../data/raw_data"
    data = load_data(raw_data_folder)
    processed_data = preprocess_data(data)

    wavelet_coefficients = perform_wavelet_transform(processed_data)
    print("Dalgacık dönüşümü tamamlandı.")
    print("Dalgacık katsayıları:")
    for scenario_name, coeffs in wavelet_coefficients.items():
        print(f"Senaryo: {scenario_name}")
        print(f"  Coefficients X: {coeffs['coeffs_x']}")
        print(f"  Coefficients Y: {coeffs['coeffs_y']}")
        print(f"  Coefficients Z: {coeffs['coeffs_z']}")

if __name__ == "__main__":
    main()