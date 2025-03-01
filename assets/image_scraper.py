#!/usr/bin/env python3
import os
import re
import requests
from pathlib import Path
import argparse
from urllib.parse import urlparse

def extract_image_urls(markdown_content):
    """Extract all image URLs from markdown content."""
    # Match only ![alt](url) pattern
    md_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
    
    md_urls = re.findall(md_pattern, markdown_content)
    
    return md_urls

def download_image(url, output_path):
    """Download an image from URL to the specified path."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Get file extension from URL or default to .jpg
        parsed_url = urlparse(url)
        path = parsed_url.path
        extension = os.path.splitext(path)[1].lower()
        if not extension or extension not in ['.jpg', '.jpeg', '.png', '.gif', '.svg']:
            # Try to determine from content-type
            content_type = response.headers.get('content-type', '')
            if 'png' in content_type:
                extension = '.png'
            elif 'gif' in content_type:
                extension = '.gif'
            elif 'svg' in content_type:
                extension = '.svg'
            else:
                extension = '.jpg'  # Default to jpg
        
        # Write the file
        with open(output_path + extension, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return output_path + extension
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def process_markdown_file(markdown_path):
    """Process a markdown file, extract and download all images."""
    markdown_path = Path(markdown_path)
    
    # Create 'images' directory in the same location as the markdown file
    output_dir = markdown_path.parent / "images"
    os.makedirs(output_dir, exist_ok=True)
    
    # Read markdown content
    with open(markdown_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract image URLs
    image_urls = extract_image_urls(content)
    
    if not image_urls:
        print(f"No image URLs found in {markdown_path}")
        return
    
    print(f"Found {len(image_urls)} images in {markdown_path}")
    
    # Download images
    downloaded_files = []
    for i, url in enumerate(image_urls, 1):
        output_path = os.path.join(output_dir, str(i))
        print(f"Downloading image {i}/{len(image_urls)}: {url}")
        downloaded_file = download_image(url, output_path)
        if downloaded_file:
            downloaded_files.append(downloaded_file)
    
    print(f"Downloaded {len(downloaded_files)} images to {output_dir}/")
    return downloaded_files

def main():
    parser = argparse.ArgumentParser(description='Extract and download images from markdown files')
    parser.add_argument('markdown_file', help='Path to the markdown file')
    args = parser.parse_args()
    
    process_markdown_file(args.markdown_file)

if __name__ == "__main__":
    main()
