# 🌞 PVWatts Lite (pvlib-based)

A lightweight **solar power prediction tool** inspired by NREL’s PVWatts, built using **pvlib** and real-world solar datasets (NASA POWER).

This project estimates **solar energy generation (kWh)** for any location using physics-based modeling.

---

## 🚀 Features

- 📍 Location-based solar power prediction  
- ☀️ Uses real irradiance & temperature data  
- 🔬 Physics-based modeling with pvlib  
- 📊 Monthly & annual energy output  
- ⚡ DC to AC conversion with system losses  
- 🧮 Simple alternative to PVWatts  

---

## 🧠 How It Works

The model follows standard solar PV simulation steps:

1. **Solar Irradiance Input (GHI)**
2. **Plane of Array (POA) Calculation**
3. **Cell Temperature Estimation**
4. **DC Power Calculation**
5. **Loss Adjustments (soiling, inverter, etc.)**
6. **Final AC Energy Output (kWh)**

---

## 📂 Project Structure

    pvwatts-lite-pvlib/

      │── main.py # Runs the simulation
      │── solar_model.py # Core PV calculations
      │── data_loader.py # Loads NASA/CSV data
      │── nasa_data.csv # Sample dataset
      │── requirements.txt # Dependencies

    ---

## ⚙️ Installation

- git clone https://github.com/ArpitChb2704/pvwatts-lite-pvlib.git
- cd pvwatts-lite-pvlib
- pip install -r requirements.txt 

## Usage

python main.py

## Example Output

    {
      
    "annual_energy_kwh": 4141.42,
  
      "monthly_energy_kwh": {
  
        "Jan": 1018.89,
        "Feb": 589.53,
        "Mar": 105.58
    
      }
    
    }

## 🧾 Inputs

- Latitude & Longitude
- Panel tilt & azimuth
- System size (kW)
- System losses (%)
- Weather dataset (NASA / CSV)

## 📊 Outputs

- Monthly energy generation (kWh)
- Annual energy output
- Performance insights

## 🛠 Tech Stack

- Python
- pvlib
- pandas
- numpy
- NASA POWER API

## 📜 License

- MIT License
