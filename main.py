import streamlit as st
import re
import time

# Set page configuration
st.set_page_config(
    page_title="Bullseye - Data Deletion",
    page_icon="🎯",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-message {
        background-color: #D4EDDA;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        text-align: center;
        margin: 1rem 0;
    }
    .container {
        max-width: 600px;
        margin: 0 auto;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background-color: #f8f9fa;
    }
    </style>
""", unsafe_allow_html=True)

# Function to validate email
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Function to validate phone number (basic validation)
def is_valid_phone(phone):
    # Remove spaces, dashes, etc.
    phone = re.sub(r'[\s\-\(\)\+]', '', phone)
    # Check if it's all digits and reasonable length
    return phone.isdigit() and 7 <= len(phone) <= 15

# Main app container
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">🎯 Bullseye Deletion Section</h1>', unsafe_allow_html=True)

# Description
st.markdown("""
    Use this form to request deletion of your data from our systems.
    Please provide either your email address or phone number associated with your account.
""")

# Form for user input
with st.form("deletion_form"):
    contact_option = st.radio("Select contact information type:", ["Email Address", "Phone Number"])
    
    if contact_option == "Email Address":
        contact_info = st.text_input("Enter your email address:")
    else:
        contact_info = st.text_input("Enter your phone number:")
    
    submit_button = st.form_submit_button("Submit Deletion Request")

# Handle form submission
if submit_button:
    if not contact_info:
        st.error("Please enter your contact information.")
    elif contact_option == "Email Address" and not is_valid_email(contact_info):
        st.error("Please enter a valid email address.")
    elif contact_option == "Phone Number" and not is_valid_phone(contact_info):
        st.error("Please enter a valid phone number.")
    else:
        # Show processing indicator
        with st.spinner("Processing your request..."):
            time.sleep(1.5)  # Simulate processing time
        
        # Show success message with icon
        st.markdown("""
            <div class="success-message">
                <h3>✅ Request Received Successfully!</h3>
                <p>We'll delete your data within 5-7 days.<br>
                Thank you for choosing Bullseye.</p>
            </div>
        """, unsafe_allow_html=True)

# Privacy notice
st.markdown("""
    ---
    **Privacy Notice**: Your contact information is only used to process your deletion 
    request and will not be used for any other purpose.
""")

st.markdown('</div>', unsafe_allow_html=True)
