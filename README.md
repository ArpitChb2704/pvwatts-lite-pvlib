# 🌞 Solar Mitra

A full-stack solar analytics platform that predicts **annual energy production, monthly generation, and 7-day forecasts** using multiple models including **custom PVLib engine, PVGIS, and PVWatts**.

In Addition **solar power prediction tool** inspired by NREL’s PVWatts, built using **pvlib** and real-world solar datasets (NASA POWER).

This project estimates **solar energy generation (kWh)** for any location using physics-based modeling.


## 🌐 Live Demo
🔗 https://solarmitra.streamlit.app

---

## 🚀 Features

- 📍 Location-based solar prediction (map + lat/lon auto-detection)
- ⚡ Multi-model comparison:
  - Custom PVLib-based model
  - PVGIS
  - PVWatts
- 📊 Annual + Monthly energy production
- 📈 7-day solar forecast (weather-aware)
- 🌞 Irradiance analysis (PVGIS)
- 💰 Savings calculator (ROI, payback, CO₂ impact)
- 📄 Downloadable **premium PDF report**
- 🗺️ Interactive dashboard (Streamlit)

---

## 🧠 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **Solar Modeling:** PVLib  
- **Data Sources:** NASA / PVGIS  
- **Visualization:** Plotly  
- **PDF Reports:** ReportLab  

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

## ⚙️ API Endpoints

### `/predict`
- Custom solar model prediction  
- Returns:
  - Annual energy
  - Monthly production
  - Performance ratio
  - 7-day forecast  

### `/predict1`
- PVGIS-based simulation  
- Includes irradiance data  

### `/predict2`
- PVWatts-based simulation  

### `/savings`
- ROI and financial analysis  

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

- Location
- Latitude & Longitude
- Panel tilt & azimuth
- System size (kW)
- System losses (%)
- Weather dataset (NASA / CSV)

## 📊 Outputs

- Monthly energy generation (kWh)
- Annual energy output
- Performance insights
- 7 day forcast
- Model Comaprison
- Irradiance Graph
- Savings Insight


## 🔥 Unique Selling Points

- Combines 3 solar models in one dashboard
- Includes weather-based forecasting
- Provides financial insights + sustainability metrics
- Generates client-ready PDF reports


## 📜 License

- MIT License
