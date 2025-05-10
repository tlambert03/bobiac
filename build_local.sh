#!/bin/bash

# Exit immediately if a command fails
set -e

# Flags
CLEAN=false
LAUNCH=false

# Parse command-line options
while getopts "rl" opt; do
  case $opt in
    r)
      CLEAN=true
      ;;
    l)
      LAUNCH=true
      ;;
  esac
done

# Clean build if -r is passed
if [ "$CLEAN" = true ]; then
  echo "🧹 Cleaning _build/ directory..."
  rm -rf _build/
  echo "📁 Verifying _build/ is empty..."
  if [ ! -d "_build" ]; then
    echo "✅ _build/ has been removed successfully."
  else
    echo "❌ _build/ still exists or wasn't removed properly:"
    ls -la _build/
  fi
fi

# Build the book
echo "🔧 Building Jupyter Book with Sphinx..."
python3 -m sphinx -a . -b html _build/html
echo "📘 Book built successfully at _build/html/"

# Prepare built notebook downloads in _build/html/notebooks/
echo "📁 Preparing downloadable notebooks..."
for notebook in $(find content/ -name "*.ipynb"); do
  rel_path="${notebook#content/}"  # remove 'content/' prefix
  out_path="_build/html/notebooks/$rel_path"
  out_dir=$(dirname "$out_path")
  mkdir -p "$out_dir"
  echo "📓 Processing $rel_path..."
  python3 "$(dirname "$0")/update_notebook.py" "$notebook" "$out_path"
done

echo "✅ Updated notebooks copied to _build/html/notebooks/"

# Launch local server if -l passed
if [ "$LAUNCH" = true ]; then
  echo "🛑 Checking for existing server on port 8000..."
  PID=$(lsof -ti tcp:8000)
  if [ -n "$PID" ]; then
    echo "⚠️ Port 8000 in use by PID $PID — killing it..."
    kill -9 "$PID"
    echo "✅ Previous server on port 8000 killed."
  fi

  echo "🚀 Launching local server at http://localhost:8000 ..."
  cd _build/html
  python3 -m http.server 8000 &
  SERVER_PID=$!
  cd ../../
  sleep 1  # Give the server time to start
  python -m webbrowser http://localhost:8000/index.html
  wait $SERVER_PID
fi