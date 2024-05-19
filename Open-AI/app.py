import streamlit as st
import requests

# Define the API endpoint and headers
url = "https://open-ai21.p.rapidapi.com/conversationgpt35"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": "cc21a6d84amsh4554f8ab718a355p193f27jsn9af80c2a90fc",
    "X-RapidAPI-Host": "open-ai21.p.rapidapi.com",
}

# Streamlit UI elements
st.title("SHANU-GPT")

# Input text box for user messages
user_message = st.text_input("You:", "")

# Function to send a message to the API and get the chatbot's response
def send_message(message):
    payload = {
        "messages": [{"role": "user", "content": message}],
        "web_access": False,
        "stream": False
    }
    response = requests.post(url, json=payload, headers=headers)
    bot_response = response.json().get("BOT", "")
    return bot_response

# Main Streamlit app loop
if st.button("Send"):
    if user_message:
        # Get chatbot's response
        chatbot_response = send_message(user_message)
        
        # Display the chatbot's response with formatting
        st.subheader("BOT : ")
        st.write(chatbot_response)
