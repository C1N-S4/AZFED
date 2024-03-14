import sys
import os
import numpy as np

# Üst dizini Python arama yoluna ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.feature_extraction import extract_features

# Özellik çıkarımı fonksiyonu burada zaten tanımlı, bu yüzden test fonksiyonunu ayrı tanımlamak lazım.

def test_extract_features():
    try:
        # Test verileri oluştur
        test_data = {
            "test": {
                "energy_x": [10, 20, 30],
                "energy_y": [40, 50, 60],
                "energy_z": [70, 80, 90]
            }
        }

        # Özellikleri çıkar
        features = extract_features(test_data)

        # Sonuçları doğrula, her assert ifadesi için açıklayıcı hata mesajları ekle
        assert len(features) == 1, "Özellik sayısı beklenen ile uyuşmuyor."
        assert "test" in features, "'test' senaryosu çıktıda bulunamadı."
        assert features["test"]["mean_energy_x"] == 20, "mean_energy_x hesaplaması yanlış."
        assert features["test"]["mean_energy_y"] == 50, "mean_energy_y hesaplaması yanlış."
        assert features["test"]["mean_energy_z"] == 80, "mean_energy_z hesaplaması yanlış."
        assert features["test"]["std_energy_x"] == np.std([10, 20, 30], ddof=0), "std_energy_x hesaplaması yanlış."
        assert features["test"]["std_energy_y"] == np.std([40, 50, 60], ddof=0), "std_energy_y hesaplaması yanlış."
        assert features["test"]["std_energy_z"] == np.std([70, 80, 90], ddof=0), "std_energy_z hesaplaması yanlış."
        assert features["test"]["max_energy_x"] == 30, "max_energy_x hesaplaması yanlış."
        assert features["test"]["max_energy_y"] == 60, "max_energy_y hesaplaması yanlış."
        assert features["test"]["max_energy_z"] == 90, "max_energy_z hesaplaması yanlış."

        print("Test başarıyla geçti.")
    except AssertionError as e:
        print("Test başarısız oldu.")
        print(f"Hata mesajı: {e.args[0] if e.args else 'No error message provided.'}")
        print(f"Tüm hata detayları: {e}")
    except Exception as e:
        print("Beklenmeyen bir hata oluştu.")
        print(f"Hata mesajı: {e.args[0] if e.args else 'No error message provided.'}")
        print(f"Tüm hata detayları: {e}")

if __name__ == "__main__":
    test_detect_anomalies()

if __name__ == "__main__":
    test_extract_features()


