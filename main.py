import streamlit as st
import os
import json

st.set_page_config(page_title="ASR LibriStutter", layout="wide")

files = os.listdir("asr_outputs")
file_to_name = {
    "whisper_tiny.json": "Whisper (Tiny)",
    "whisper_tiny_gpt-4o_1refs.json": "Whisper (Tiny) &rarr; GPT-4o (1 Refs)",
    "whisper_tiny_gpt-4o_5refs.json": "Whisper (Tiny) &rarr; GPT-4o (5 Refs)",
    "whisper_tiny_gpt-4o_10refs.json": "Whisper (Tiny) &rarr; GPT-4o (10 Refs)",
    "whisper_tiny_llama_2_1refs.json": "Whisper (Tiny) &rarr; Llama 2 (1 Refs)",
    "whisper_tiny_llama_2_5refs.json": "Whisper (Tiny) &rarr; Llama 2 (5 Refs)",
    "whisper_tiny_llama_2_10refs.json": "Whisper (Tiny) &rarr; Llama 2 (10 Refs)",
    "whisper_small.json": "Whisper (Small)",
    "whisper_small_gpt-4o_1refs.json": "Whisper (Small) &rarr; GPT-4o (1 Refs)",
    "whisper_small_gpt-4o_5refs.json": "Whisper (Small) &rarr; GPT-4o (5 Refs)",
    "whisper_small_gpt-4o_10refs.json": "Whisper (Small) &rarr; GPT-4o (10 Refs)",
    "whisper_base.json": "Whisper (Base)",
    "whisper_base_gpt-4o_1refs.json": "Whisper (Base) &rarr; GPT-4o (1 Refs)",
    "whisper_base_gpt-4o_5refs.json": "Whisper (Base) &rarr; GPT-4o (5 Refs)",
    "whisper_base_gpt-4o_10refs.json": "Whisper (Base) &rarr; GPT-4o (10 Refs)",
    "whisper_medium.json": "Whisper (Medium)",
    "whisper_medium_gpt-4o_1refs.json": "Whisper (Medium) &rarr; GPT-4o (1 Refs)",
    "whisper_medium_gpt-4o_5refs.json": "Whisper (Medium) &rarr; GPT-4o (5 Refs)",
    "whisper_medium_gpt-4o_10refs.json": "Whisper (Medium) &rarr; GPT-4o (10 Refs)",
    "whisper_medium_llama_2_1refs.json": "Whisper (Medium) &rarr; Llama 2 (1 Refs)",
    "whisper_medium_llama_2_5refs.json": "Whisper (Medium) &rarr; Llama 2 (5 Refs)",
    "whisper_medium_llama_2_10refs.json": "Whisper (Medium) &rarr; Llama 2 (10 Refs)",
}

st.write("**Automatic Speech Recognition (ASR) Outputs on LibriStutter**")

displaying_files = st.sidebar.multiselect(
    "Select files to display",
    files,
    default=[
        "whisper_small.json",
        "whisper_base.json",
        "whisper_medium.json",
        "whisper_medium_gpt-4o_1refs.json",
        "whisper_medium_gpt-4o_5refs.json",
        "whisper_medium_gpt-4o_10refs.json",
        "whisper_medium_llama_2_1refs.json",
        "whisper_medium_llama_2_5refs.json",
        "whisper_medium_llama_2_10refs.json",
    ],
    format_func=lambda x: file_to_name[x],
)

sample_id = st.sidebar.selectbox("Select sample", range(10))

data = {
    file_to_name[file]: json.load(open(f"asr_outputs/{file}"))[sample_id]["transcript"] for file in displaying_files
}

items = list(data.items())

ground_truth_value = json.load(open(f"asr_outputs/{displaying_files[0]}"))[sample_id]["ground_truth"]
st.markdown(
    f"""
    <div style="border: 2px solid; border-radius: 6px; padding: 20px 20px 20px 20px; margin: 10px 0; background-color: #cce7ff;">
        <h5 style="margin: 0;">Ground truth</h4>
        <p style="margin: 0;">{ground_truth_value}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

num_cols = 3
num_rows = (len(items) + num_cols - 1) // num_cols
for row in range(num_rows):
    cols = st.columns(num_cols)
    for col in range(num_cols):
        idx = row * num_cols + col
        if idx < len(items):
            key, value = items[idx]
            cols[col].markdown(
                f"""
            <div style="border: 2px solid #ddd; border-radius: 6px; padding: 20px 20px 20px 20px; margin: 10px 0; width: 100%;">
                <h5 style="margin: 0;">{key}</h4>
                <p style="margin: 0;">{value}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
