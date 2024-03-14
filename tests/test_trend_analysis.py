import sys
import os

# Üst dizini Python arama yoluna ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.trend_analysis import analyze_trends

def test_analyze_trends():
    try:
        # Test verileri oluştur
        test_features = {
            "test1": {
                "mean_energy_x": 20,
                "mean_energy_y": 50,
                "mean_energy_z": 80
            },
            "test2": {
                "mean_energy_x": 30,
                "mean_energy_y": 60,
                "mean_energy_z": 90
            }
        }

        # Trendleri analiz et
        trends = analyze_trends(test_features)

        # Sonuçları doğrula
        assert len(trends) == 2
        assert "test1" in trends
        assert "test2" in trends
        assert trends["test1"]["energy_x"] == 20
        assert trends["test1"]["energy_y"] == 50
        assert trends["test1"]["energy_z"] == 80
        assert trends["test2"]["energy_x"] == 30
        assert trends["test2"]["energy_y"] == 60
        assert trends["test2"]["energy_z"] == 90

        print("Test başarıyla geçti.")
    except AssertionError as e:
        print("Test başarısız oldu.")
        print("Hata mesajı:", str(e))
    except Exception as e:
        print("Beklenmeyen bir hata oluştu.")
        print("Hata mesajı:", str(e))

if __name__ == "__main__":
    test_analyze_trends()