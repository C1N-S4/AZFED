import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.anomaly_detection import detect_anomalies

def test_detect_anomalies():
    try:
        test_features = {
            "test1": {
                "mean_energy_x": 20,
                "mean_energy_y": 50,
                "mean_energy_z": 80,
                "std_energy_x": 10,
                "std_energy_y": 10,
                "std_energy_z": 10
            },
            "test2": {
                "mean_energy_x": 200,
                "mean_energy_y": 500,
                "mean_energy_z": 800,
                "std_energy_x": 10,
                "std_energy_y": 10,
                "std_energy_z": 10
            }
        }

        anomalies = detect_anomalies(test_features, threshold=3.0)

        # Anomali tespit sonuçlarını kontrol etmeden önce değerleri yazdır
        print(f"test1 için anomaly_y değeri: {anomalies['test1']['anomaly_y']}")
        print(f"test2 için anomaly_y değeri: {anomalies['test2']['anomaly_y']}")

        assert len(anomalies) == 2, "Anomali sayısı 2 olmalıdır."
        assert not anomalies["test1"]["anomaly_x"], "test1'in anomaly_x içermemesi gerekiyor."
        assert not anomalies["test1"]["anomaly_y"], "test1'in anomaly_y içermemesi gerekiyor."
        assert not anomalies["test1"]["anomaly_z"], "test1'in anomaly_z içermemesi gerekiyor."
        assert anomalies["test2"]["anomaly_x"], "test2 anomaly_x içermelidir."
        assert anomalies["test2"]["anomaly_y"], "test2 anomaly_y içermelidir."
        assert anomalies["test2"]["anomaly_z"], "test2 anomaly_z içermelidir."

        print("Test başarıyla geçti.")
    except AssertionError as e:
        print("Test başarısız oldu.")
        print(f"Hata mesajı: {e}")
    except Exception as e:
        print("Beklenmeyen bir hata oluştu.")
        print(f"Hata mesajı: {e}")

if __name__ == "__main__":
    test_detect_anomalies()
