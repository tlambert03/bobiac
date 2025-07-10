// Force all external links to open in a new tab
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('a[href^="http"]').forEach(link => {
        console.log("Modifying link:", link.href);
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // handle Markdown links to download of files with specified extensions
    const markdownLinks = document.querySelectorAll('a');
    markdownLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            const href = link.getAttribute('href');
            if (href) {
                const fileExtensions = [
                    '.pdf', '.tif', '.tiff', '.png',
                    '.jpg', '.jpeg', '.zip', '.ipynb'
                ];
                if (fileExtensions.some(ext => href.endsWith(ext))) {
                    event.preventDefault(); // Prevent navigation
                    const downloadLink = document.createElement('a');
                    downloadLink.href = href;
                    downloadLink.download = href.split('/').pop();
                    document.body.appendChild(downloadLink); // Ensure it's in DOM
                    downloadLink.click();
                    document.body.removeChild(downloadLink); // Clean up
                }
            }
        });
    });
});

// Function to download all course data files
async function downloadScript() {
    // Fetch the directory listing from _static/data
    const response = await fetch('../_static/data/');
    const html = await response.text();
    
    // Parse HTML to find all .zip files
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const links = doc.querySelectorAll('a[href$=".zip"]');
    
    // Extract zip filenames
    const zipFiles = Array.from(links).map(link => {
        const href = link.getAttribute('href');
        return href.split('/').pop(); // Get just the filename
    }).filter(filename => filename.endsWith('.zip'));
    
    if (zipFiles.length === 0) {
        alert('No zip files found in the data directory.');
        return;
    }
    
    // Create a zip file containing all data files
    const JSZip = window.JSZip || await import('https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js').then(m => m.default);
    const zip = new JSZip();
    const dataFolder = zip.folder("bobiac_data");
    
    // Fetch and add each file to the zip
    for (const filename of zipFiles) {
        try {
            const fileResponse = await fetch(`../_static/data/${filename}`);
            const fileBlob = await fileResponse.blob();
            dataFolder.file(filename, fileBlob);
        } catch (error) {
            console.error(`Failed to fetch ${filename}:`, error);
        }
    }
    
    // Generate and download the combined zip
    const zipBlob = await zip.generateAsync({type: "blob"});
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(zipBlob);
    link.download = 'bobiac_data.zip';
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(link.href);
}