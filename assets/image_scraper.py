#!/usr/bin/env python3
import os
import re
import requests
import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse
from typing import List, Optional


def extract_image_urls(markdown_content: str) -> List[str]:
    """
    Extract all image URLs from markdown content.
    
    Args:
        markdown_content (str): The markdown text to parse
        
    Returns:
        List[str]: List of image URLs found in the markdown
    """
    # Match only ![alt](url) pattern
    md_pattern = r'!\[.*?\]\((https?://[^)]+)\)'
    
    md_urls = re.findall(md_pattern, markdown_content)
    
    return md_urls


def download_image(url: str, output_path: str) -> Optional[str]:
    """
    Download an image from URL to the specified path.
    
    Args:
        url (str): URL of the image to download
        output_path (str): Base path where the image will be saved (without extension)
        
    Returns:
        Optional[str]: Path to the downloaded file, or None if download failed
    """
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


def process_markdown_file(markdown_path: str) -> Optional[List[str]]:
    """
    Process a markdown file, extract and download all images.
    
    Args:
        markdown_path (str): Path to the markdown file to process
        
    Returns:
        Optional[List[str]]: List of paths to downloaded files, or None if no images were found
        
    Raises:
        FileNotFoundError: If the markdown file doesn't exist
    """
    markdown_path = Path(markdown_path)
    
    if not markdown_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {markdown_path}")
    
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
        return None
    
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


def main() -> None:
    """
    Parse command line arguments and process the markdown file.
    """
    parser = argparse.ArgumentParser(description='Extract and download images from markdown files')
    parser.add_argument(
        'markdown_file', 
        help='Path to the markdown file'
    )
    
    args = parser.parse_args()
    
    try:
        process_markdown_file(args.markdown_file)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
