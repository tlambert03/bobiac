#!/bin/bash

# Exit if any command fails
set -e

# Check for -r (clean build)
CLEAN=false
while getopts "r" opt; do
  case $opt in
    r)
      CLEAN=true
      ;;
  esac
done

if [ "$CLEAN" = true ]; then
  echo "🧹 Cleaning _build/ directory..."
  rm -rf _build/
fi

echo "📁 Preparing static notebook downloads..."
mkdir -p _static/notebooks/
find content/ -name "*.ipynb" -exec cp {} _static/notebooks/ \;
echo "✅ Notebooks copied to _static/notebooks/"

echo "🔧 Building Jupyter Book with Sphinx..."
sphinx-build -a . -b html _build/html

echo "📘 Book built successfully at _build/html/"