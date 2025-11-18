import streamlit as st

# Function to calculate Fair Price
def calculate_fair_price(book_value, pe_ratio_avg, actual_eps):
    theoretical_eps = book_value / pe_ratio_avg
    ratio = actual_eps / theoretical_eps
    fair_price = ratio * book_value
    return fair_price, theoretical_eps, ratio

# Streamlit UI Config
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
st.markdown("<div class='sub-title'>Estimate the fair value of a stock using Theoretical EPS and Book Value</div>", unsafe_allow_html=True)

# Sidebar Inputs
st.sidebar.title("Inputs")
st.sidebar.markdown("Provide the following details to calculate the fair price:")

book_value_per_share = st.sidebar.number_input("Book Value per Share (₹):", min_value=0.0, value=0.0, step=0.01)
pe_ratio_avg = st.sidebar.number_input("3-Year Average P/E Ratio:", min_value=0.1, value=10.0, step=0.1)
actual_eps = st.sidebar.number_input("Actual EPS (₹):", min_value=0.01, value=1.0, step=0.01)
margin_of_safety = st.sidebar.number_input("Margin of Safety (%):", min_value=0.0, max_value=100.0, value=20.0, step=0.1)

# Action Button
if st.sidebar.button("Calculate Fair Price"):
    fair_price, theoretical_eps, ratio = calculate_fair_price(book_value_per_share, pe_ratio_avg, actual_eps)
    final_buy_price = fair_price - (fair_price * (margin_of_safety / 100))
    stop_loss_price = final_buy_price - (final_buy_price * (margin_of_safety / 100))

    # Input Summary
    st.markdown(f"""
        ### 🔍 Input Summary
        - **Book Value per Share**: ₹{book_value_per_share}
        - **3-Year Avg. P/E Ratio**: {pe_ratio_avg}
        - **Actual EPS**: ₹{actual_eps}
        - **Theoretical EPS**: ₹{theoretical_eps:.2f}
        - **EPS Ratio (Theoretical / Actual)**: {ratio:.2f}
        - **Margin of Safety**: {margin_of_safety}%
    """)

    # Result Card
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
            <h3 style="color: #4CAF50;">Final Buy Price (After Margin of Safety)</h3>
            <h1 style="color: #d32f2f;">₹{final_buy_price:.2f}</h1>
            <h1 style="color: #d32f2f;">Stoploss Price ₹{stop_loss_price:.2f}</h1>
        </div>
        """, unsafe_allow_html=True
    )

# Footer
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
