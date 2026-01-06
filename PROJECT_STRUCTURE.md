# Project Structure

This document outlines the organized structure of the Learning App for Kids with ASD.

## Core Application Files

### Main Applications
- `learning_webapp.py` - Main Flask web application
- `run_learning_webapp.py` - Launcher for learning webapp (port 5002)
- `run_addition_app.py` - Addition practice app launcher (port 5001)
- `run_subtraction_app.py` - Subtraction practice app launcher (port 5003)

### Supporting Modules
- `emotion_tracker_webapp.py` - Advanced emotion tracking (DeepFace + MediaPipe)
- `emotion_tracker_simple.py` - Simple emotion tracking (simulation fallback)
- `frustration_webapp.py` - Frustration analysis and scoring
- `preferred_mode_analyzer.py` - Analyzes frustration to determine preferred mode
- `generate_its_reports.py` - Generates Interrupted Time Series plots
- `list_dependencies.py` - Lists all dependencies and tools

## Templates

All HTML templates are in the `templates/` directory:
- `learning_index.html` - Homepage for learning webapp
- `learning.html` - Main learning interface
- `addition_learning.html` - Addition learning examples
- `addition_practice_emotion.html` - Addition practice interface
- `subtraction_learning.html` - Subtraction learning examples
- `subtraction_practice_emotion.html` - Subtraction practice interface

## Interactive Tasks

All interactive kinesthetic task HTML files are in the `tasks/` directory:
- `kinesthetic_task_1.html` through `kinesthetic_task_10.html` - Main learning app tasks
- `addition_kinesthetic_1.html` through `addition_kinesthetic_5.html` - Addition practice tasks
- `subtraction_kinesthetic_1.html` through `subtraction_kinesthetic_5.html` - Subtraction practice tasks
- `drag_task.html` - Additional drag-and-drop task

## Data Files

### Input (Included in Repository)
- `questions.csv` - Sample questions for learning webapp

### Output (Generated, Gitignored)
- `learner_log*.csv` - Learning session logs
- `addition_practice_log*.csv` - Addition practice logs
- `subtraction_practice_log*.csv` - Subtraction practice logs
- `frustration_report*.csv` - Frustration analysis reports
- `preferred_modes.csv` - Preferred learning modes (template included)
- `inactivity_thresholds.json` - Computed inactivity thresholds
- `outputs/` - Generated ITS plots

## Configuration Files

- `requirements.txt` - Python package dependencies
- `.gitignore` - Git ignore rules
- `README.md` - Project documentation
- `LICENSE` - License file
- `PROJECT_STRUCTURE.md` - This file

## Removed Legacy Files

The following legacy files have been removed to keep the repository clean:
- `LearningApp.py` - Legacy tkinter application
- `learning_webapp_core.py` - Legacy core module
- `app.py` - Legacy addition app (replaced by `run_addition_app.py`)
- `subtraction_app.py` - Legacy subtraction app (replaced by `run_subtraction_app.py`)
- `Frustraiton.py` - Legacy frustration module (replaced by `frustration_webapp.py`)
- `Emoitiontracker.py` - Legacy emotion tracker (typo, replaced by `emotion_tracker_webapp.py`)
- `main_app_launcher.py` - Alternative launcher (not needed)
- `simple_launcher.py` - Alternative launcher (not needed)
- `start_app.py` - Alternative launcher (not needed)
- `test.py` - Test file
- `test_imports.py` - Test file
- `reload_python_env.py` - Utility script (not needed)

## File Organization Principles

1. **Separation of Concerns**: Core logic, templates, and tasks are in separate directories
2. **Clear Naming**: Files follow consistent naming conventions
3. **No User Data**: All user-generated data is gitignored
4. **Minimal Dependencies**: Only essential files are included
5. **Documentation**: README and structure docs are comprehensive

