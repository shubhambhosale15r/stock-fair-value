import streamlit as st

# Function to calculate Fair Price
def calculate_fair_price(book_value_per_share, roe, pe_ratio):
    eps = book_value_per_share * (roe / 100)  # Convert ROE to decimal
    fair_price = eps * pe_ratio
    return fair_price

# Streamlit UI
st.set_page_config(page_title="Stock Fair Price Calculator", page_icon="💸", layout="centered")

# Header Section with Style
st.markdown(
    """
    <style>
    .main-title {
        font-size:36px; 
        color: #4CAF50; 
        font-family: 'Trebuchet MS', sans-serif;
        text-align: center; 
        margin-bottom: 20px;
    }
    .sub-title {
        font-size:20px;
        color: #555555;
        font-family: 'Trebuchet MS', sans-serif;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Add Titles
st.markdown("<div class='main-title'>📈 Stock Fair Price Calculator</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Estimate the fair value of a stock using Book Value, ROE, and P/E Ratio</div>", unsafe_allow_html=True)

# Input Section with Sidebar
st.sidebar.title("Inputs")
st.sidebar.markdown("Provide the following details to calculate the fair price:")

# Input Fields
book_value_per_share = st.sidebar.number_input("Book Value per Share (₹):", min_value=0.0, value=0.0, step=0.01)
roe = st.sidebar.number_input("ROE (Return on Equity, %):", min_value=0.0, value=0.0, step=0.01)
pe_ratio = st.sidebar.number_input("P/E Ratio:", min_value=0.0, value=0.0, step=0.01)

# Action Button
if st.sidebar.button("Calculate Fair Price"):
    fair_price = calculate_fair_price(book_value_per_share, roe, pe_ratio)

    # Display Result with Style
    st.markdown(
        f"""
        <div style="
            text-align:center; 
            border: 2px solid #4CAF50; 
            padding: 15px; 
            margin: 20px auto; 
            max-width: 400px; 
            border-radius: 10px;
            background-color: #e8f5e9;
            ">
            <h2 style="color: #4CAF50;">Fair Price</h2>
            <h1 style="color: #212121;">₹{fair_price:.2f}</h1>
        </div>
        """, unsafe_allow_html=True
    )

# Footer Section
st.markdown(
    """
    ---
    <footer style="
        text-align:center;
        font-family: 'Trebuchet MS', sans-serif;
        margin-top: 50px;
        color: #555555;
    ">
    
    </footer>
    """, unsafe_allow_html=True
)
