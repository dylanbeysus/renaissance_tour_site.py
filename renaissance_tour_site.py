import streamlit as st

st.set_page_config(page_title="Renaissance World Tour 2024", layout="wide")

# --- Title & Banner ---
st.title("🎤 Renaissance World Tour 2024")
st.markdown("### 🌍 Stadium Residencies | March – October 2024 | Côte d’Ivoire & USA Focused")

st.image("https://i.imgur.com/kYd4oWx.jpg", use_column_width=True)

# --- Tour Overview ---
st.header("✨ About the Tour")
st.write("""
The Renaissance World Tour 2024 is a global celebration of performance, power, and art — featuring 
carefully spaced stadium residencies across all continents, with a spotlight on Côte d’Ivoire and the USA.

Each city hosts multiple shows, providing fans a truly immersive experience.
""")

# --- Tour Schedule ---
st.header("🗓️ Full Tour Schedule")

tour_data = {
    "Africa": [
        "May 1 – Abidjan, Côte d’Ivoire – Stade Félix Houphouët-Boigny",
        "May 4 – Abidjan, Côte d’Ivoire – Stade Félix Houphouët-Boigny",
        "May 10 – Lagos, Nigeria – National Stadium",
        "May 15 – Accra, Ghana – Accra Sports Stadium",
    ],
    "North America": [
        "June 10 – Los Angeles, CA – SoFi Stadium",
        "June 15 – Houston, TX – NRG Stadium",
        "June 22 – New York, NY – MetLife Stadium",
    ],
    "Europe": [
        "July 5 – Paris, France – Stade de France",
        "July 10 – London, UK – Wembley Stadium",
    ],
    "Asia": [
        "August 5 – Tokyo, Japan – Tokyo Dome",
        "August 12 – Seoul, South Korea – Olympic Stadium",
    ],
    "Latin America": [
        "August 20 – Rio de Janeiro, Brazil – Maracanã Stadium",
    ],
    "Oceania": [
        "August 28 – Sydney, Australia – Accor Stadium",
    ]
}

for region, dates in tour_data.items():
    st.subheader(f"🌍 {region}")
    for date in dates:
        st.markdown(f"- {date}")

# --- Footer ---
st.markdown("---")
st.markdown("© 2024 Renaissance Tour by Beyoncé. Website powered by Streamlit.")
