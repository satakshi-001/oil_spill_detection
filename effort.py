import streamlit as st

# PAGE CONFIGURATION

st.set_page_config(
    #browser tab title and icon
    page_title="SAR Oil Spill Detection",
    page_icon="🛰️",
    layout="wide",)

#title inside webpage
st.title("🛰️ SAR Oil Spill Detection System")

st.write("AI-assisted satellite SAR configuration for oil spill detection prototype")

#horizontal dividing line
st.divider()

#ENVIRONMENTAL CONDITIONS

st.header("🌊Environmental Conditions")

#creates columns for environmental conditions
col1, col2, col3 = st.columns(3)

with col1:
    #variable namely wind-speed is created to take a numeral input with default value, 10
    wind_speed = st.number_input("wind speed (m/s)", min_value=0.0, max_value=50.0, value=10.0)

with col2:
    wave_height = st.number_input("wave height (m)", min_value=0.0, max_value=20.0, value=2.0)

with col3:
    #dropdown menu for user with a list of options to select from
    rain = st.selectbox("Rain conditions", ["No Rain", "Light Rain", "Heavy Rain"])

st.divider()

#SAR CONFIGURATION ENGINE 

st.header("🛰️SAR Configuration Recommendation")

#defining a function to do the recommendation at one place
def recommend_sar(wind, waves, rain):

#prototype decision logic 
#this will later be replaced with a scientifically validated model
    
    if rain == "Heavy Rain":
        band = "C-band"
        polarization = "VV"
        reason = ("heavy rain can introduce additional noise. ""C-band VV is selected as the prototype configuration. ")

    elif wind < 3:
        band = "C-band"
        polarization = "VV"
        reason = ("Very low wind produces weak sea-surface roughness, making oil-water contrast more difficult to detect.")

    elif wind < 12 and waves < 4:
        band = "L-band"
        polarization = "HH"
        reason = ("higher sea-state conditions detected. " "L-band/HH is selected for this scenerio.")

        return band, polarization, reason

    band, polarization, reason = recommend_sar(wind_speed, wave_height, rain) 

    col1, col2 = st.columns(2)

#display a big value with lable to make results stand out visually
    with col1: st.metric("Recommended SAR Band", band)
    with col2: st.metric("Recommended Polarization", polarization)
#displays on informational box
    st.info(reason)
    st.divider()

    #SATELLITE IMAGE 

st.header("🛰️Satellite SAR image")

uploaded_file = st.file_uploader("Upload a SAR image", type=["png", "jpg", "jpeg", "tif", "tiff"])

if uploaded_file is not None:
    #boolean variable to check if the uploaded file is an image, True/False as an on/off switch
    st.image(uploaded_file,caption="uploaded SAR image", use_container_width=True)
    st.success("Image successfully uploaded.")

else:
    st.warning("Upload a SAR image to continue to the CNN detection stage.")

st.divider()

#DETECTION PLACEHOLDER

st.header("🧠 CNN Oil Spill Detection")

if uploaded_file is not None:
    st.info("CNN Model will be connected here in the next stage.")

    st.button("Run Oil Spill Detection")

else:
    st.write("Waiting for satellite image....")

st.divider()

#AIS PLACEHOLDER 

st.header("🛳️AIS vessel correlation")
st.write("if an oil spill is detected the system will correlate the spill location and acquisition time with nearby AIS vessels.")
st.info("AIS correlation module will be connected after the CNN module")



