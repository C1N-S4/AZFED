import os
import sys
import json

# Üst dizini Python arama yoluna ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.data_preprocessing import load_data, preprocess_data

def test_preprocess_data_vibration():
    try:
        # Test verileri oluştur, 'parameters' anahtarını da içerecek şekilde güncelle
        test_data = {
            "test": {
                "parameters": {},  # Bu örnekte boş bırakıldı, gerektiği gibi doldurulabilir
                "vibration_data": [
                    {"timestamp": 0.0, "accelerometer_x": 1, "accelerometer_y": 2, "accelerometer_z": 3},
                    {"timestamp": 0.1, "accelerometer_x": 4, "accelerometer_y": 5, "accelerometer_z": 6}
                ]
            }
        }

        # Verileri ön işle
        processed_data = preprocess_data(test_data)

        # Sonuçları doğrula
        assert len(processed_data) == 1
        assert "test" in processed_data
        assert processed_data["test"]["accelerometer_data"]["timestamp"] == [0.0, 0.1]
        assert processed_data["test"]["accelerometer_data"]["accelerometer_x"] == [1, 4]
        assert processed_data["test"]["accelerometer_data"]["accelerometer_y"] == [2, 5]
        assert processed_data["test"]["accelerometer_data"]["accelerometer_z"] == [3, 6]

        print("Test başarıyla geçti.")

    except AssertionError as e:
        print("Test başarısız oldu.")
        print("Hata mesajı:", str(e))
    except Exception as e:
        print("Beklenmeyen bir hata oluştu.")
        print("Hata mesajı:", str(e))

if __name__ == "__main__":
    test_preprocess_data_vibration()