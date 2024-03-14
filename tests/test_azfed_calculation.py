import sys
import os

# Üst dizini Python arama yoluna ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.azfed_calculation import azfed_calculation

def test_azfed_calculation():
    try:
        # Test verileri oluştur, 'timestamp' anahtarını da içerecek şekilde güncelle
        test_data = {
            "test": {
                "accelerometer_data": {
                    "timestamp": [0, 1, 2],  # 'timestamp' değerleri eklendi
                    "accelerometer_x": [1, 2, 3],
                    "accelerometer_y": [4, 5, 6],
                    "accelerometer_z": [7, 8, 9]
                }
            }
        }

        # AZFED hesapla
        azfed_data = azfed_calculation(test_data)

        # Sonuçları doğrula
        assert len(azfed_data) == 1
        assert "test" in azfed_data
        assert azfed_data["test"]["energy_x"] == [14]  # Toplam enerji değerlerini list olarak güncelle
        assert azfed_data["test"]["energy_y"] == [77]
        assert azfed_data["test"]["energy_z"] == [194]

        print("Test başarıyla geçti.")
    except AssertionError as e:
        print("Test başarısız oldu.")
        print("Hata mesajı:", str(e))
    except Exception as e:
        print("Beklenmeyen bir hata oluştu.")
        print("Hata mesajı:", str(e))

if __name__ == "__main__":
    test_azfed_calculation()
