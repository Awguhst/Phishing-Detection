import streamlit as st
import pickle

# Load the model
loaded_model = pickle.load(open('./model/phishing.pkl', 'rb'))

# Customizing the app's theme and layout (using wide layout)
st.set_page_config(page_title="Phishing URL Detection", page_icon="🔒", layout="centered")

# Styling for the app (white background in a box)
st.markdown("""
    <style>
        /* Global Styles */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f7f9fb;
            color: #333;
        }
        .stButton>button {
            background-color: #0078D4;
            color: white;
            font-size: 5px; 
            font-weight: 600;
            padding: 6px 6px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 28px; 
        }
        .stButton>button:hover {
            background-color: #005a9e;
        }

        .stTextInput>div>input {
            border-radius: 8px;
            border: 1px solid #ddd;
            padding: 14px;
            font-size: 18px;
            width: 70%;
            box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.1);
            margin-right: 100; 
        }
        .stTextInput>div>input:focus {
            border-color: #0078D4;
            box-shadow: 0 0 5px rgba(0, 120, 212, 0.5);
        }

        /* Cards for results */
        .result-card {
            padding: 18px;
            border-radius: 12px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        .safe-card {
            background-color: #171a21;
            color: #00796b;
        }
        .phishing-card {
            background-color: #171a21;
            color: #d32f2f;
        }

        /* Heading styles */
        h1, h2, h3 {
            font-weight: 600;
            color: #444;
        }
        .title {
            font-size: 48px;
            text-align: center;
            color: #0078D4;
            margin-top: 30px;
        }
        .description {
            color: #0078D4;
            font-size: 20px;
            text-align: center;
            margin-top: 10px;
            font-weight: 400;
        }

        /* Spinner style */
        .stSpinner {
            color: #0078D4;
        }

        /* Spacing between sections */
        .section {
            margin-bottom: 70px;
        }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<div class="title">🔒 Phishing URL Detection</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="description">
        This application uses a <strong>machine learning model</strong> to predict if a URL is <strong>phishing</strong> or <strong>safe</strong>.
        Simply enter a URL, and it will analyze it for potential threats.
    </div>
""", unsafe_allow_html=True)

# Wrap the content in a centered box
with st.container():
    st.markdown('<div class="container-box">', unsafe_allow_html=True)

    # Create two columns: one for the input and one for the button
    col1, col2, col3 = st.columns([0.2, 4.8, 1])  # Adjust the ratios to control the width of the columns

    with col2:
        # URL input field with placeholder and tooltip
        url_input = st.text_input("Enter URL to Analyze:", "https://www.youtube.com/", placeholder="https://www.youtube.com/", help="Enter the full URL (e.g., https://example.com)")

    with col3:
        # Analyze button
        analyze_button = st.button("Analyze URL")

    # Prediction logic happens after the button is clicked, outside of the columns
    if analyze_button:
        if url_input:
            with st.spinner("Analyzing..."):
                prediction = loaded_model.predict([url_input])

            # Displaying results inside a card style layout
            if prediction == 1:
                st.markdown("""
                    <div class="result-card phishing-card">
                        <h3>Phishing URL 🚨</h3>
                        <p>This URL is highly suspicious. It may attempt to steal your personal information. Proceed with caution.</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="result-card safe-card">
                        <h3>Safe URL ✅</h3>
                        <p>This URL appears to be safe and does not pose an immediate threat. You can proceed with confidence.</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Please enter a URL to analyze.")

    st.markdown('</div>', unsafe_allow_html=True)
