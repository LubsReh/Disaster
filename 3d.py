import streamlit as st
from streamlit_globe import streamlit_globe

st.title("Death and Property loss per year")
dist = ["Alappuzha",
    "Ernakulam",
    "Thiruvananthapuram",
    "Kollam",
    "Pathanamthitta",
    "Kottayam",
    "Idukki",
    "Malappuram",
    "Palakkad",
    "Thrissur",
    "Kozhikode",
    "Wayanad",
    "Kannur",
    "Kasaragod"]
selected_dist = st.selectbox("Select a district", dist)

col1, col2 = st.columns(2)


if selected_dist == "Alappuzha":

    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [16453,17255, 17718, 16472, 22205]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})


if selected_dist == "Ernakulam":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [29944, 20958, 22605, 20614, 30287]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})

if selected_dist == "Thiruvananthapuram":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [33161, 33030, 34545, 31033, 41966]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})

if selected_dist == "Kollam":
   years = [2017, 2018, 2019, 2020, 2021]
   deaths = [20310, 20608, 21762, 20163,  27508]

   with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

   with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})

if selected_dist == "Pathanamthitta":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [12210 ,12802, 12802, 11666, 15058]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})

if selected_dist == "Kottayam":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [19892, 20300, 21053, 18788 , 25569]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})

if selected_dist == "Idukki":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [6897, 7201, 7080, 6795, 8819]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})

if selected_dist == "Malappuram":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [20829 ,19255, 22433, 3200, 4000]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})

if selected_dist == "Palakkad":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [18296, 18831,  19429, 18364 , 26311]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})

if selected_dist == "Thrissur":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [28841, 29453, 31071, 28472 , 37817]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})


if selected_dist == "Kozhikode":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [26398, 3000, 5000, 3200, 4000]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})


if selected_dist == "Wayanad":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [4492,3000, 5000, 3200, 4000]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})


if selected_dist == "Kannur":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [18346, 3000, 5000, 3200, 4000]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})


if selected_dist == "Kasaragod":
    years = [2017, 2018, 2019, 2020, 2021]
    deaths = [7273, 3000, 5000, 3200, 4000]

    with col1:
        st.header("Year vs Death")
        st.line_chart(data={'Years': years, 'Deaths': deaths})

    with col2:
        st.header("Year vs Property Loss")
        st.bar_chart(data={'Years': years, 'Deaths': deaths})





st.subheader("Kerala Flood 2018")
pointsData1=[{'lat': 8.50, 'lng': 76.70, 'size': 0.1, 'color': 'red'}]
labelsData1=[{'lat': 8.50, 'lng': 76.70, 'size': 0.1, 'color': 'red', 'text': 'Thiruvananthapuram'}]
pointsData2=[{'lat': 8.89, 'lng': 77.11, 'size': 0.2, 'color': 'red'}]
labelsData2=[{'lat': 8.89, 'lng': 77.11, 'size': 0.2, 'color': 'red', 'text': 'Kollam'}]
pointsData3=[{'lat': 9.28, 'lng': 76.45, 'size': 0.1, 'color': 'red'}]
labelsData3=[{'lat': 9.28, 'lng': 76.45, 'size': 0.1, 'color': 'red', 'text': 'Pathanamthitta'}]
pointsData4=[{'lat': 9.50, 'lng': 76.39, 'size': 0.2, 'color': 'red'}]
labelsData4=[{'lat': 9.50, 'lng': 76.39, 'size': 0.2, 'color': 'red', 'text': 'Alappuzha'}]
pointsData5=[{'lat': 9.58, 'lng': 76.57, 'size': 0.1, 'color': 'red'}]
labelsData5=[{'lat': 9.58, 'lng': 76.57, 'size': 0.1, 'color': 'red', 'text': 'Kottayam'}]
pointsData6=[{'lat': 10.20, 'lng': 77.00, 'size': 0.4, 'color': 'red'}]
labelsData6=[{'lat': 10.20, 'lng': 77.00, 'size': 0.4, 'color': 'red', 'text': 'Idukki'}]
pointsData7=[{'lat': 10.00, 'lng': 76.20, 'size': 0.1, 'color': 'red'}]
labelsData7=[{'lat': 10.00, 'lng': 76.20, 'size': 0.1, 'color': 'red', 'text': 'Ernakulam'}]
pointsData8=[{'lat': 11.10, 'lng': 76.23, 'size': 0.2, 'color': 'red'}]
labelsData8=[{'lat': 11.10, 'lng': 76.23, 'size': 0.2, 'color': 'red', 'text': 'Thrissur'}]
pointsData9=[{'lat': 10.78, 'lng': 76.63, 'size': 0.35, 'color': 'red'}]
labelsData9=[{'lat': 10.78, 'lng': 76.63, 'size': 0.35, 'color': 'red', 'text': 'Palakkad'}]
pointsData10=[{'lat': 11.0, 'lng': 76, 'size': 0.2, 'color': 'red'}]
labelsData10=[{'lat': 11.0, 'lng': 76, 'size': 0.2, 'color': 'red', 'text': 'Malappuram'}]
pointsData11=[{'lat': 11.25, 'lng': 75.77, 'size': 0.1, 'color': 'red'}]
labelsData11=[{'lat': 11.25, 'lng': 75.77, 'size': 0.1, 'color': 'red', 'text': 'Kozhikode'}]
pointsData12=[{'lat': 11.62, 'lng': 76.14, 'size': 0.2, 'color': 'red'}]
labelsData12=[{'lat': 11.62, 'lng': 76.14, 'size': 0.2, 'color': 'red', 'text': 'Wayanad'}]
pointsData13=[{'lat': 11.86, 'lng': 75.39, 'size': 0.1, 'color': 'red'}]
labelsData13=[{'lat': 11.86, 'lng': 75.39, 'size': 0.1, 'color': 'red', 'text': 'Kannur'}]
pointsData14=[{'lat': 12.48, 'lng': 74.90, 'size': 0.2, 'color': 'red'}]
labelsData14=[{'lat': 12.48, 'lng': 74.90, 'size': 0.2, 'color': 'red', 'text': 'Kasaragod'}]
pointsData = pointsData1 + pointsData2 + pointsData3 + pointsData4 +pointsData5 + pointsData6 +pointsData7 + pointsData8 +pointsData9 + pointsData10 +pointsData11 + pointsData12  + pointsData13 + pointsData14
labelsData = labelsData1 + labelsData2 + labelsData3 + labelsData4 +labelsData5 + labelsData6 +labelsData7 + labelsData8 +labelsData9 + labelsData10 +labelsData11 + labelsData12  + labelsData13 + labelsData14
streamlit_globe(pointsData=pointsData, labelsData=labelsData, daytime='day', width=800, height=600)

