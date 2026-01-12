#!/usr/bin/env python3
"""
Simple LLM Install - Local LLM Setup Made Easy
GitHub: https://github.com/yourusername/simple-llm-install
"""

import requests
import subprocess
import sys
import os

def check_ollama_installed():
    """Check if Ollama is installed"""
    try:
        result = subprocess.run(["ollama", "--version"], 
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def check_ollama_running():
    """Check if Ollama service is running"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return response.status_code == 200
    except:
        return False

def list_models():
    """List all available Ollama models"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=10)
        if response.status_code == 200:
            models = response.json().get('models', [])
            return models
        return []
    except:
        return []

def display_models():
    """Display available models"""
    models = list_models()
    if not models:
        print("❌ No models found")
        return False
    
    print("\n📋 Available Models:")
    print("-" * 50)
    for i, model in enumerate(models, 1):
        name = model.get('name', 'Unknown')
        size_gb = round(model.get('size', 0) / (1024*1024*1024), 1)
        print(f"{i}. {name} ({size_gb} GB)")
    return True

def pull_model(model_name):
    """Pull a model from Ollama library"""
    print(f"\n📥 Downloading {model_name}...")
    try:
        process = subprocess.Popen(
            ["ollama", "pull", model_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Stream output
        for line in process.stdout:
            print(f"   {line.strip()}")
        
        process.wait()
        return process.returncode == 0
    except Exception as e:
        print(f"❌ Error downloading model: {e}")
        return False

def chat_with_model(model_name):
    """Simple chat interface with the selected model"""
    print(f"\n💬 Chatting with {model_name}")
    print("Type 'quit' to exit, 'models' to see available models")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == 'quit':
                break
            elif user_input.lower() == 'models':
                display_models()
                continue
            
            if not user_input:
                continue
            
            # Send request to Ollama
            payload = {
                "model": model_name,
                "prompt": user_input,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "num_predict": 2048
                }
            }
            
            print("🤖 Thinking...")
            response = requests.post(
                "http://localhost:11434/api/generate",
                json=payload,
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"\nAssistant: {result.get('response', 'No response')}")
            else:
                print(f"❌ Error: {response.status_code}")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def show_instructions():
    """Show installation instructions"""
    print("""
🚀 Simple LLM Install - Quick Start Guide

PREREQUISITES:
1. Install Ollama first: https://ollama.ai/
   - Windows: Download the installer
   - macOS: brew install ollama
   - Linux: curl -fsSL https://ollama.ai/install.sh | sh

2. Start Ollama service:
   ollama serve

POPULAR MODELS:
- llama2: General purpose (3.8GB)
- mistral: Efficient model (4.1GB)  
- codellama: Coding assistant (3.8GB)
- llama2:13b: Larger version (7.3GB)

USAGE:
1. Run this script: python simple_llm.py
2. Choose a model to use
3. Start chatting!

This script provides a simple interface to run LLMs locally using Ollama.
No automatic downloads - you have full control!
    """)

def main():
    print("=" * 50)
    print("🤖 Simple LLM Install")
    print("=" * 50)
    
    # Check if Ollama is installed
    if not check_ollama_installed():
        print("❌ Ollama is not installed")
        show_instructions()
        return
    
    # Check if Ollama service is running
    if not check_ollama_running():
        print("❌ Ollama service is not running")
        print("💡 Start Ollama with: ollama serve")
        print("\n🔧 Starting Ollama service...")
        
        try:
            # Try to start Ollama in the background
            subprocess.Popen(["ollama", "serve"])
            print("⏳ Waiting for Ollama to start...")
            
            # Wait a bit for service to start
            import time
            time.sleep(3)
            
            if not check_ollama_running():
                print("❌ Could not start Ollama automatically")
                print("💡 Please run 'ollama serve' manually in another terminal")
                return
        except Exception as e:
            print(f"❌ Error starting Ollama: {e}")
            return
    
    print("✅ Ollama is installed and running")
    
    # Show available models
    models = list_models()
    if not models:
        print("\n📭 No models available")
        print("💡 You need to download models first")
        
        model_choice = input("Download a model? (y/n): ").lower().strip()
        if model_choice == 'y':
            model_name = input("Enter model name (e.g., llama2): ").strip()
            if model_name:
                if pull_model(model_name):
                    print(f"✅ Successfully downloaded {model_name}")
                    models = list_models()  # Refresh model list
                else:
                    print("❌ Failed to download model")
                    return
        else:
            show_instructions()
            return
    
    # Let user select a model
    display_models()
    
    try:
        choice = input("\nSelect model (number) or enter model name: ").strip()
        
        if choice.isdigit():
            # User entered a number
            choice_num = int(choice)
            if 1 <= choice_num <= len(models):
                model_name = models[choice_num-1].get('name')
            else:
                print("❌ Invalid selection")
                return
        else:
            # User entered a model name
            model_name = choice
        
        print(f"✅ Selected model: {model_name}")
        
        # Start chat interface
        chat_with_model(model_name)
        
    except ValueError:
        print("❌ Please enter a valid number or model name")
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()
