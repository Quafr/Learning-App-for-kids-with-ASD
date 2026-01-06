#!/usr/bin/env python3
"""
Dependency Listing Script
Lists all Python libraries and tools used in this project
"""

import sys
import os

def main():
    # Set UTF-8 encoding for console output
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    
    print("=" * 70)
    print("LEARNING APP FOR KIDS WITH ASD - DEPENDENCIES AND TOOLS")
    print("=" * 70)
    print()
    
    # Core Python Libraries (Standard Library)
    print("STANDARD LIBRARY MODULES (Built-in Python):")
    print("-" * 70)
    stdlib_modules = [
        "os", "sys", "csv", "json", "time", "datetime", "threading",
        "subprocess", "socket", "argparse", "glob", "collections",
        "statistics", "math", "typing", "webbrowser", "random"
    ]
    for module in sorted(stdlib_modules):
        print(f"  • {module}")
    print()
    
    # External Dependencies
    print("EXTERNAL PYTHON PACKAGES (Install via pip):")
    print("-" * 70)
    
    dependencies = {
        "Core Web Framework": [
            ("Flask", "2.3.3", "Web application framework"),
            ("Werkzeug", "2.3.7", "WSGI utilities (Flask dependency)"),
            ("Jinja2", "3.1.2", "Template engine (Flask dependency)")
        ],
        "Data Processing": [
            ("pandas", "2.1.1", "Data manipulation and analysis"),
            ("numpy", ">=1.24.0", "Numerical computing")
        ],
        "Computer Vision & Emotion Tracking": [
            ("opencv-python", "4.8.1.78", "Computer vision library for camera access"),
            ("deepface", "0.0.79", "Facial recognition and emotion detection"),
            ("mediapipe", "0.10.7", "Media processing framework")
        ],
        "Audio Processing": [
            ("pygame", "2.5.2", "Audio playback (optional, for sound features)")
        ],
        "HTTP & Networking": [
            ("requests", "2.31.0", "HTTP library for API calls")
        ],
        "Data Visualization & Analysis": [
            ("matplotlib", "3.7.2", "Plotting and visualization"),
            ("seaborn", "0.12.2", "Statistical data visualization"),
            ("scipy", "1.11.1", "Scientific computing")
        ]
    }
    
    total_packages = 0
    for category, packages in dependencies.items():
        print(f"\n  {category}:")
        for pkg_name, version, description in packages:
            print(f"    • {pkg_name:20s} {version:15s} - {description}")
            total_packages += 1
    print()
    
    # Development Tools
    print("DEVELOPMENT TOOLS & ASSISTIVE TECHNOLOGIES:")
    print("-" * 70)
    tools = [
        ("Python", "3.7+", "Programming language"),
        ("Flask", "Web framework", "Backend server"),
        ("HTML5/CSS3/JavaScript", "Modern web standards", "Frontend interface"),
        ("Webcam", "Hardware", "For emotion tracking (optional)"),
        ("Git", "Version control", "Code management"),
        ("Virtual Environment", "venv/conda", "Dependency isolation")
    ]
    for tool, version, description in tools:
        print(f"  • {tool:25s} {version:20s} - {description}")
    print()
    
    # Features & Technologies
    print("KEY TECHNOLOGIES & FEATURES:")
    print("-" * 70)
    technologies = [
        "Real-time emotion detection (DeepFace + MediaPipe)",
        "Adaptive learning modes (Visual, Auditory, Kinesthetic)",
        "Frustration analysis and mode switching",
        "Interactive drag-and-drop tasks (HTML5)",
        "Text-to-speech (Browser Web Speech API)",
        "Local data processing (privacy-first)",
        "CSV data logging",
        "Interrupted Time Series (ITS) analysis",
        "Flask RESTful API",
        "Responsive web design"
    ]
    for tech in technologies:
        print(f"  • {tech}")
    print()
    
    print("=" * 70)
    print(f"Total External Packages: {total_packages}")
    print("=" * 70)
    print()
    print("INSTALLATION:")
    print("  pip install -r requirements.txt")
    print()
    print("NOTE: Some packages (deepface, mediapipe) may require")
    print("      additional system dependencies. See package documentation.")
    print("=" * 70)

if __name__ == "__main__":
    main()

