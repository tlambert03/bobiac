#!/bin/bash

# Exit if any command fails
set -e

# Flags
CLEAN=false
LAUNCH=false

# Parse options
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

# Clean build if -r passed
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

# Prepare static notebooks
echo "📁 Preparing static notebook downloads..."
mkdir -p _static/notebooks/
# update the notebook to modify cells depending on their tag
for notebook in $(find content/ -name "*.ipynb"); do
  out_name=$(basename "$notebook")
  python3 update_notebook.py "$notebook" "_static/notebooks/$out_name"
done
echo "✅ Cleaned notebooks copied to _static/notebooks/"

# Build the book
echo "🔧 Building Jupyter Book with Sphinx..."
sphinx-build -a . -b html _build/html
echo "📘 Book built successfully at _build/html/"

# Launch local server if -l passed
if [ "$LAUNCH" = true ]; then
  echo "🚀 Launching local server at http://localhost:8000 ..."
  cd _build/html
  python3 -m http.server &
  SERVER_PID=$!
  cd ../../
  sleep 1  # Give the server a moment to start
  xdg-open http://localhost:8000/index.html >/dev/null 2>&1 || open http://localhost:8000/index.html
  wait $SERVER_PID
fi