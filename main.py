from utils.data_preprocessing import load_data, preprocess_data
from utils.azfed_calculation import azfed_calculation
from utils.feature_extraction import extract_features
from utils.anomaly_detection import detect_anomalies
from utils.trend_analysis import analyze_trends
from utils.visualization import visualize_results

def main():
    try:
        # Veri yükleme ve ön işleme
        raw_data_folder = "data/raw_data"
        data = load_data(raw_data_folder)
        processed_data = preprocess_data(data)

        # AZFED hesaplama
        azfed_data = azfed_calculation(processed_data)

        # Özellik çıkarımı
        features = extract_features(azfed_data)

        # Anomali tespiti
        anomalies = detect_anomalies(features)

        # Trend analizi
        trends = analyze_trends(features)

        # Görselleştirme
        visualize_results(features, anomalies, trends)

        print("Ana program başarıyla tamamlandı.")
    except Exception as e:
        print("Ana programda bir hata oluştu.")
        print(f"Hata mesajı: {e}")

if __name__ == "__main__":
    main()