import os
import json
import numpy as np

def load_data(data_folder):
    data = {}
    for file_name in os.listdir(data_folder):
        if file_name.endswith(".json"):
            file_path = os.path.join(data_folder, file_name)
            with open(file_path, "r") as file:
                scenario_data = json.load(file)
                scenario_name = scenario_data["scenario"]
                data[scenario_name] = scenario_data
    return data

def preprocess_data(data):
    processed_data = {}
    for scenario_name, scenario_data in data.items():
        vibration_data = scenario_data["vibration_data"]
        accelerometer_data = {
            "timestamp": [],
            "accelerometer_x": [],
            "accelerometer_y": [],
            "accelerometer_z": []
        }
        for entry in vibration_data:
            accelerometer_data["timestamp"].append(entry["timestamp"])
            accelerometer_data["accelerometer_x"].append(entry["accelerometer_x"])
            accelerometer_data["accelerometer_y"].append(entry["accelerometer_y"])
            accelerometer_data["accelerometer_z"].append(entry["accelerometer_z"])
        processed_data[scenario_name] = {
            "parameters": scenario_data["parameters"],
            "accelerometer_data": accelerometer_data
        }
    return processed_data

def main():
    raw_data_folder = "../data/raw_data"
    data = load_data(raw_data_folder)
    processed_data = preprocess_data(data)
    print("Veri ön işleme tamamlandı.")
    print("İşlenmiş veri:")
    print(processed_data)

if __name__ == "__main__":
    main()