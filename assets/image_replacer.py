#!/usr/bin/env python3
import os
import re
import argparse
from pathlib import Path
from urllib.parse import urlparse

def is_url(path):
    """Check if a string is a URL."""
    try:
        result = urlparse(path)
        return all([result.scheme, result.netloc])
    except:
        return False

def get_file_extension(path):
    """Extract file extension from path, defaulting to .jpg if none found."""
    _, ext = os.path.splitext(path)
    if ext:
        return ext.lower()
    return ".jpg"  # Default extension if none is found

def find_image_paths(content, file_type):
    """Find all image paths in the content based on file type."""
    if file_type == 'md':
        # Match markdown image syntax: ![alt text](path/to/image)
        return re.findall(r'!\[.*?\]\((.*?)\)', content)
    elif file_type == 'html':
        # Match HTML img tags: <img src="path/to/image" ... >
        return re.findall(r'<img[^>]*src=[\'"]([^\'"]+)[\'"]', content)
    return []

def replace_image_paths(content, file_type, base_github_url):
    """Replace image paths with GitHub raw URLs based on order of appearance."""
    if file_type == 'md':
        # Find all markdown image patterns
        image_patterns = list(re.finditer(r'!\[.*?\]\((.*?)\)', content))
        
        # Replace each pattern with a numbered image path
        new_content = content
        offset = 0  # Track offset due to string length changes
        
        for i, match in enumerate(image_patterns, 1):
            original_path = match.group(1)
            if not is_url(original_path):
                # Get original extension
                ext = get_file_extension(original_path)
                
                # Create new path with sequential numbering and original extension
                new_path = f"{base_github_url}/{i}{ext}"
                
                # Get the full match and calculate positions with offset
                full_match = match.group(0)
                start_pos = match.start() + offset
                end_pos = match.end() + offset
                
                # Create replacement text preserving alt text
                alt_text = full_match.split('](')[0][2:]
                replacement = f"![{alt_text}]({new_path})"
                
                # Replace in the content
                new_content = new_content[:start_pos] + replacement + new_content[end_pos:]
                
                # Update offset
                offset += len(replacement) - len(full_match)
        
        return new_content
    
    elif file_type == 'html':
        # Find all HTML img tag patterns
        image_patterns = list(re.finditer(r'<img[^>]*src=[\'"]([^\'"]+)[\'"]', content))
        
        # Replace each pattern with a numbered image path
        new_content = content
        offset = 0  # Track offset due to string length changes
        
        for i, match in enumerate(image_patterns, 1):
            original_path = match.group(1)
            if not is_url(original_path):
                # Get original extension
                ext = get_file_extension(original_path)
                
                # Create new path with sequential numbering and original extension
                new_path = f"{base_github_url}/{i}{ext}"
                
                # Get the full match and calculate positions with offset
                full_match = match.group(0)
                start_pos = match.start() + offset
                end_pos = match.end() + offset
                
                # Create replacement text
                replacement = full_match.replace(original_path, new_path)
                
                # Replace in the content
                new_content = new_content[:start_pos] + replacement + new_content[end_pos:]
                
                # Update offset
                offset += len(replacement) - len(full_match)
        
        return new_content
    
    return content

def process_directory(directory):
    """Process all markdown and HTML files in the directory."""
    # Use the specified GitHub repository with correct URL format
    github_repo = "FistOfHit/SixRackUnits"
    dir_name = os.path.basename(directory)
    
    # Construct the URL with the correct format including refs/heads/main
    year = dir_name.split('_')[1]
    base_github_url = f"https://raw.githubusercontent.com/{github_repo}/refs/heads/main/newsletters/{year}/{dir_name}/images"
    
    for file_path in Path(directory).glob('*'):
        if file_path.is_file():
            file_ext = file_path.suffix.lower()
            
            if file_ext in ['.md', '.html']:
                print(f"Processing {file_path}")
                
                # Read file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Determine file type
                file_type = 'md' if file_ext == '.md' else 'html'
                
                # Replace image paths
                new_content = replace_image_paths(
                    content, 
                    file_type, 
                    base_github_url
                )
                
                # Write updated content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"Updated {file_path}")

def main():
    parser = argparse.ArgumentParser(description='Replace image paths with GitHub raw URLs')
    parser.add_argument('directory', help='Directory containing markdown and HTML files')
    
    args = parser.parse_args()
    
    process_directory(args.directory)
    print("Image replacement complete!")

if __name__ == "__main__":
    main()
