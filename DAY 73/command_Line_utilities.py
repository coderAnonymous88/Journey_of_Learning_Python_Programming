import subprocess

# Define the command and URL (wrap URL in quotes if running via shell)
url = "https://www.insidewink.com/wp-content/uploads/2020/04/photo-1495107334309-fcf20504a5ab.jpeg"
filename = "Cinderella.jpeg"

command = [
    "curl.exe",
    "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "-o", filename,
    url
]

# Run the curl command via system terminal
result = subprocess.run(command, capture_output=True, text=True)

if result.returncode == 0:
    print("Download successful!")
else:
    print("Error during download:", result.stderr)