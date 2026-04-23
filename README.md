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

  <img width="1457" height="827" alt="image" src="https://github.com/user-attachments/assets/cfa29ab7-13aa-45eb-ac75-15c6914c5553" />
<img width="1462" height="676" alt="Screenshot 2026-04-23 at 12 26 23 PM" src="https://github.com/user-attachments/assets/fab7686d-ee32-47dd-a332-9f9b5db8eb56" />
<img width="1470" height="682" alt="Screenshot 2026-04-23 at 12 26 39 PM" src="https://github.com/user-attachments/assets/b19cbdbf-7e24-401f-a434-8cbb3d83bf71" />
<img width="1436" height="506" alt="Screenshot 2026-04-23 at 12 26 52 PM" src="https://github.com/user-attachments/assets/d1e7e26d-11b1-430a-9a78-313845557489" />
<img width="1425" height="437" alt="Screenshot 2026-04-23 at 12 27 08 PM" src="https://github.com/user-attachments/assets/207c7865-dd5e-457d-859a-bff9f4ed083e" />
<img width="593" height="829" alt="Screenshot 2026-04-23 at 12 29 01 PM" src="https://github.com/user-attachments/assets/ab1850cd-f7cf-4b45-908b-388936cfdce5" />



