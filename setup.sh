#!/bin/bash

echo "🧹 Cleaning old environment (if exists)..."
rm -rf .venv

echo "🐍 Creating fresh virtual environment..."
python3 -m venv .venv

echo "🔄 Activating virtual environment..."
source .venv/bin/activate

echo "⬇️ Installing latest clean dependencies..."
pip install --upgrade pip
pip install streamlit langchain langchain-openai openai python-dotenv tiktoken

echo "🛠 Installing optional dev utilities (watchdog)..."
pip install watchdog

echo "✅ Environment setup complete!"

echo "🚀 Launching Nina app..."
streamlit run app.py