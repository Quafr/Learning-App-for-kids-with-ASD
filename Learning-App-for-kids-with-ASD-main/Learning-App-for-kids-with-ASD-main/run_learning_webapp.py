"""
Autism Learning WebApp Launcher
Launches the Flask webapp version of AutismApp with all original logic preserved
"""

import os
import sys
import webbrowser
import threading
import time

def main():
	print("Autism Learning WebApp")
	print("========================")
	print("Starting the web application...")
	print("Features included:")
	print("   • Real-time emotion tracking")
	print("   • Frustration analysis and mode switching")
	print("   • Visual learning mode")
	print("   • Auditory learning mode") 
	print("   • Kinesthetic learning mode")
	print("   • CSV data logging")
	print("   • Accessible, learner-friendly UI")
	print()
	
	# Change to the current directory to ensure proper imports
	os.chdir(os.path.dirname(os.path.abspath(__file__)))
	
	try:
		# Import the learning webapp
		print("Loading webapp modules...")
		import learning_webapp
		print("WebApp loaded successfully.")
		print()
		
		# Auto-open browser after a short delay
		def open_browser():
			time.sleep(1.5)
			webbrowser.open('http://localhost:5002')
		
		browser_thread = threading.Thread(target=open_browser)
		browser_thread.daemon = True
		browser_thread.start()
		
		# Run the Flask app
		print("Starting Flask server on http://localhost:5002")
		print("Browser will open automatically...")
		print()
		learning_webapp.app.run(debug=False, host='0.0.0.0', port=5002, use_reloader=False)
		
	except Exception as e:
		print(f"Error starting the webapp: {e}")
		print()
		print("Troubleshooting tips:")
		print("   1. Make sure you have installed the requirements:")
		print("      pip install -r requirements.txt")
		print("   2. Check that your camera is not being used by another app")
		print("   3. Make sure Python has camera permissions")
		print("   4. Try running: python learning_webapp.py directly")
		print()
		sys.exit(1)

if __name__ == "__main__":
	main()
