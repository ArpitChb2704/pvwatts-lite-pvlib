import reportlab
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim


# -------------------------------
# PDF FUNCTION
# -------------------------------
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_premium_pdf(data, filename="solar_report.pdf"):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    try:
        logo = Image("logo.png", width=120, height=60)
        elements.append(logo)
    except:
        pass

    elements.append(Spacer(1, 10))
    
    # -------------------------------
    # HEADER
    # -------------------------------
    elements.append(Paragraph("☀️ Solar Energy Report", styles["Title"]))
    elements.append(Paragraph("Powered by Your SOBO", styles["Normal"]))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"📍 Location: {data['location']}", styles["Normal"]))
    elements.append(Paragraph(f"⚙️ System Size: {data['system_size']} kW", styles["Normal"]))
    elements.append(Spacer(1, 10))

    # -------------------------------
    # ANNUAL COMPARISON
    # -------------------------------
    elements.append(Paragraph("Annual Production Comparison (kWh)", styles["Heading2"]))

    comp_table = [
        ["Model", "Annual kWh"],
        ["Custom Model", round(data["annual_custom"], 2)],
        ["PVGIS", round(data["annual_pvgis"], 2)],
        ["PVWatts", round(data["annual_pvwatts"], 2)]
    ]

    t = Table(comp_table)
    t.setStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ])

    elements.append(t)
    elements.append(Spacer(1, 10))

    # -------------------------------
    # PERFORMANCE
    # -------------------------------
    elements.append(Paragraph(f"Performance Ratio: {data['pr']}", styles["Normal"]))
    elements.append(Spacer(1, 10))

    # -------------------------------
    # MONTHLY TABLE
    # -------------------------------
    elements.append(Paragraph("Monthly Production", styles["Heading2"]))

    monthly_table = [["Month", "kWh"]]
    for k, v in data["monthly"].items():
        monthly_table.append([k, round(v, 2)])

    t = Table(monthly_table)
    t.setStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ])

    elements.append(t)
    elements.append(Spacer(1, 10))

    # -------------------------------
    # FORECAST
    # -------------------------------
    elements.append(Paragraph("7-Day Forecast", styles["Heading2"]))

    forecast_table = [["Date", "kWh", "Cloud %", "Temp °C"]]

    for row in data["forecast"]:
        forecast_table.append([
            row["date"],
            round(row["predicted_kwh"], 2),
            row["cloud_cover"],
            row["temperature"]
        ])

    t = Table(forecast_table)
    t.setStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ])

    elements.append(t)
    elements.append(Spacer(1, 10))

    # -------------------------------
    # SAVINGS
    # -------------------------------
    elements.append(Paragraph("Savings Summary", styles["Heading2"]))

    savings_table = [
        ["Metric", "Value"],
        ["Annual Savings (₹)", data["savings"]["annual_savings_rs"]],
        ["Payback (Years)", data["savings"]["payback_years"]],
        ["ROI (%)", data["savings"]["roi_percent"]],
        ["CO2 Saved (kg)", data["savings"]["co2_saved_kg"]],
        ["Trees Equivalent", round(data["savings"]["trees_equivalent"], 0)]
    ]

    t = Table(savings_table)
    t.setStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ])

    elements.append(t)

    doc.build(elements)

    return filename

# -------------------------------
# CONFIG
# -------------------------------
BASE_URL = "https://pvwatts-lite-pvlib.onrender.com"

st.set_page_config(page_title="Solar Production Dashboard", layout="wide")
col1, col2, col3 = st.columns([4, 5, 1])

with col2:
    st.image("logo.png", width=300)
st.title("☀️ Solar Power Production Dashboard")
st.title("Powered by Your SOBO")

# -------------------------------
# LOCATION INPUT
# -------------------------------
st.header("📍 Location Selection")

location_input = st.text_input("Enter Location (City / Address)")

geolocator = Nominatim(user_agent="solar_app")

lat, lon = None, None

if st.button("Search Location"):
    if location_input:
        location = geolocator.geocode(location_input)
        if location:
            lat, lon = location.latitude, location.longitude
            st.success(f"Location Found: {location.address}")

            st.session_state["lat"] = lat
            st.session_state["lon"] = lon
        else:
            st.error("Location not found")

# Retrieve stored lat/lon
lat = st.session_state.get("lat", None)
lon = st.session_state.get("lon", None)

if lat and lon:
    st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))

# -------------------------------
# SYSTEM INPUTS
# -------------------------------
st.header("⚙️ System Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    system_size = st.number_input("System Size (kW)", value=4)

with col2:
    tilt = st.number_input("Tilt (deg)", value=25)

with col3:
    azimuth = st.number_input("Azimuth (deg)", value=180)

shading = st.slider("Shading Factor", 0.0, 1.0, 0.95)

st.subheader("Losses (%)")
col1, col2, col3, col4 = st.columns(4)

soiling = col1.number_input("Soiling", value=2)
inverter = col2.number_input("Inverter", value=3)
wiring = col3.number_input("Wiring", value=2)
misc = col4.number_input("Misc", value=1)

losses = [soiling, inverter, wiring, misc]

# -------------------------------
# RUN SIMULATION
# -------------------------------
if st.button("🚀 Run Simulation") and lat and lon:

    payload = {
        "lat": lat,
        "lon": lon,
        "system_size_kw": system_size,
        "tilt": tilt,
        "azimuth": azimuth,
        "shading_factor": shading,
        "losses": losses
    }

    res_predict = requests.post(f"{BASE_URL}/predict", json=payload).json()
    res_pvgis = requests.post(f"{BASE_URL}/predict1", json=payload).json()
    res_pvwatts = requests.post(f"{BASE_URL}/predict2", json=payload).json()

    # ✅ STORE IN SESSION
    st.session_state["res_predict"] = res_predict
    st.session_state["res_pvgis"] = res_pvgis
    st.session_state["res_pvwatts"] = res_pvwatts

    # -------------------------------
    # API CALLS
    # -------------------------------
    res_predict = requests.post(f"{BASE_URL}/predict", json=payload).json()
    res_pvgis = requests.post(f"{BASE_URL}/predict1", json=payload).json()
    res_pvwatts = requests.post(f"{BASE_URL}/predict2", json=payload).json()

    # -------------------------------
    # ANNUAL COMPARISON
    # -------------------------------
    st.header("📊 Annual Production Comparison")

    annual_data = pd.DataFrame({
        "Model": ["Custom", "PVGIS", "PVWatts"],
        "Annual kWh": [
            res_predict["annual_energy_kwh"],
            res_pvgis["annual_energy_kwh"],
            res_pvwatts["annual_energy_kwh"]
        ]
    })

    st.dataframe(annual_data)

    fig = px.bar(annual_data, x="Model", y="Annual kWh")
    st.plotly_chart(fig, use_container_width=True)

    # -------------------------------
    # MONTHLY DATA (/predict)
    # -------------------------------
    st.header("📅 Monthly Production")

    monthly = res_predict["monthly_energy_kwh"]

    df_month = pd.DataFrame(list(monthly.items()), columns=["Month", "kWh"])
    st.dataframe(df_month)

    fig = px.line(df_month, x="Month", y="kWh", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    # -------------------------------
    # 7 DAY FORECAST
    # -------------------------------
    st.header("📈 7-Day Forecast")

    forecast = res_predict.get("forecast_7_days", [])

    if forecast:

        df_forecast = pd.DataFrame(forecast)

        # Rename columns for clean UI
        df_forecast = df_forecast.rename(columns={
            "date": "Date",
            "predicted_kwh": "KWh",
            "cloud_cover": "Cloud (%)",
                "temperature": "Temp (°C)"
            })

        st.dataframe(df_forecast)

            # Energy graph
        fig1 = px.line(df_forecast, x="Date", y="KWh", markers=True,
                        title="Daily Energy Forecast")
        st.plotly_chart(fig1, use_container_width=True)

            # Weather correlation graph (optional but 🔥)
        fig2 = px.bar(df_forecast, x="Date", y="Cloud (%)",
                        title="Cloud Cover Impact")
        st.plotly_chart(fig2, use_container_width=True)

    else:
        st.info("No forecast data available")

    # -------------------------------
    # IRRADIANCE GRAPH (PVGIS)
    # -------------------------------
    st.header("🌞 Irradiance (PVGIS)")

    irr = res_pvgis["monthly_energy_kwh"]

    df_irr = pd.DataFrame(irr)

    fig = px.line(df_irr, x="month", y="H(i)_m", markers=True,
                  labels={"H(i)_m": "Irradiance"})
    st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# SAVINGS CALCULATOR
# -------------------------------
st.header("💰 Savings Calculator")

col1, col2, col3 = st.columns(3)

connected_load = col1.number_input("Connected Load (kW)", value=4)
monthly_units = col2.number_input("Monthly Units", value=500)
monthly_bill = col3.number_input("Monthly Bill (₹)", value=2000)

col4, col5 = st.columns(2)

installation_cost = col4.number_input("Installation Cost (₹)", value=150000)
cost_per_kw = col5.number_input("Cost per Unit (₹)", value=6)

if st.button("Calculate Savings"):

    payload = {
        "connected_load_kw": connected_load,
        "monthly_units": monthly_units,
        "monthly_bill": monthly_bill,
        "installation_cost": installation_cost,
        "cost_per_kw": cost_per_kw
    }

    res = requests.post(f"{BASE_URL}/savings", json=payload).json()

    st.subheader("📊 Results")

    st.metric("Annual Savings (₹)", res["annual_savings_rs"])
    st.metric("Payback Period (years)", res["payback_years"])
    st.metric("ROI (%)", res["roi_percent"])

    st.write(f"🌱 CO₂ Saved: {res['co2_saved_kg']} kg")
    st.write(f"🌳 Trees Equivalent: {res['trees_equivalent']:.0f}")

res_predict = st.session_state.get("res_predict", None)
res_pvgis = st.session_state.get("res_pvgis", None)
res_pvwatts = st.session_state.get("res_pvwatts", None)

if res_predict and res_pvgis and res_pvwatts:

    if st.button("📄 Generate Premium Report"):

        savings_payload = {
            "connected_load_kw": system_size,
            "monthly_units": 500,
            "monthly_bill": 2000,
            "installation_cost": 150000,
            "cost_per_kw": 6
        }

        savings = requests.post(f"{BASE_URL}/savings", json=savings_payload).json()

        pdf_data = {
            "location": location_input,
            "system_size": system_size,
            "annual_custom": res_predict["annual_energy_kwh"],
            "annual_pvgis": res_pvgis["annual_energy_kwh"],
            "annual_pvwatts": res_pvwatts["annual_energy_kwh"],
            "pr": res_predict.get("performance_ratio", "N/A"),
            "monthly": res_predict["monthly_energy_kwh"],
            "forecast": res_predict["forecast_7_days"],
            "savings": savings
        }

        file_path = generate_premium_pdf(pdf_data)

        with open(file_path, "rb") as f:
            st.download_button(
                "⬇️ Download Premium PDF",
                f,
                file_name="solar_report.pdf",
                mime="application/pdf"
            )