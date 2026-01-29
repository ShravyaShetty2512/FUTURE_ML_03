import streamlit as st

st.set_page_config(page_title="Customer Support Bot", page_icon="🤖")

st.title("💬 Customer Support Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

def bot_reply(text):
    text = text.lower()

    if text in ["hi", "hello", "hey", "hi there"]:
        return "👋 Hi! Welcome to Customer Support. How can I help you today?"

    elif "order" in text:
        return "📦 Your order is currently being processed. You’ll receive tracking details within 24 hours."

    elif "refund" in text or "return" in text:
        return "💳 Refunds are processed within 5–7 business days after the product is returned."

    elif "contact" in text or "human" in text:
        return "📞 You can reach our support team at support@company.com"

    else:
        return "🤔 Sorry, I didn’t quite understand that. Can you please rephrase?"

# When user sends a message
if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    reply = bot_reply(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)


