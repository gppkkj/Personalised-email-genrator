from jinja2 import Template
import streamlit as st
from transformers import pipeline
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Load the Hugging Face text-generation model
generator = pipeline('text-generation', model='HuggingFaceH4/zephyr-7b-beta')

# Email template
email_template = """
Subject: {{ subject }}

Hi {{ name }},

I hope you are doing well! I wanted to reach out regarding {{ topic }}. 
{{ personalized_message }}

Looking forward to your response.

Best regards,  
{{ sender_name }}
"""

# Function to generate AI-based personalized message
def ai_generate_message(topic):
    prompt = f"Write a personalized email message about {topic}."
    result = generator(prompt, max_length=200)[0]['generated_text']
    return result.strip()

# Function to generate personalized email
def generate_email(name, topic, personalized_message, sender_name, subject):
    template = Template(email_template)
    return template.render(
        name=name,
        topic=topic,
        personalized_message=personalized_message,
        sender_name=sender_name,
        subject=subject
    )

# Streamlit UI
st.title("AI Personalized Email Generator 🚀 with Hugging Face")

name = st.text_input("Enter recipient's name:")
topic = st.text_input("Enter topic:")
sender_name = st.text_input("Enter your name:")
subject = st.text_input("Enter email subject:")

if st.button("Generate AI Message"):
    personalized_message = ai_generate_message(topic)
    st.text_area("AI-Generated Message:", personalized_message, height=200)

if st.button("Generate Final Email"):
    personalized_message = ai_generate_message(topic) if not personalized_message else personalized_message
    email = generate_email(name, topic, personalized_message, sender_name, subject)
    st.subheader("Generated Email:")
    st.code(email, language='text')
