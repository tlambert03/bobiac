# Check if OpenGL is available
echo "🔍 Verifying OpenGL setup..."
if ! glxinfo | grep -q "OpenGL version"; then
  echo "❌ OpenGL is not available! Exiting build."
  exit 1
else
  glxinfo | grep "OpenGL version"
  echo "✅ OpenGL is available."
fi

# Build the book
echo "🔧 Building Jupyter Book with Sphinx..."
DISPLAY=${DISPLAY:-:99} python3 -m sphinx -a . -b html _build/html
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