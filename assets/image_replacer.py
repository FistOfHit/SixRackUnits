#!/usr/bin/env python3
import os
import re
import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse
from typing import List


def is_url(path: str) -> bool:
    """
    Check if a string is a URL.
    
    Args:
        path (str): The string to check
        
    Returns:
        bool: True if the string is a URL, False otherwise
    """
    try:
        result = urlparse(path)
        return all([result.scheme, result.netloc])
    except:
        return False


def get_file_extension(path: str) -> str:
    """
    Extract file extension from path, defaulting to .jpg if none found.
    
    Args:
        path (str): The file path to extract extension from
        
    Returns:
        str: The file extension (including the dot) or .jpg if none found
    """
    _, ext = os.path.splitext(path)
    if ext:
        return ext.lower()
    return ".jpg"  # Default extension if none is found


def find_image_paths(content: str, file_type: str) -> List[str]:
    """
    Find all image paths in the content based on file type.
    
    Args:
        content (str): The file content to search
        file_type (str): The type of file ('md' or 'html')
        
    Returns:
        List[str]: List of image paths found in the content
    """
    if file_type == 'md':
        # Match markdown image syntax: ![alt text](path/to/image)
        return re.findall(r'!\[.*?\]\((.*?)\)', content)
    elif file_type == 'html':
        # Match HTML img tags: <img src="path/to/image" ... >
        return re.findall(r'<img[^>]*src=[\'"]([^\'"]+)[\'"]', content)
    return []


def replace_image_paths(content: str, file_type: str, base_github_url: str) -> str:
    """
    Replace image paths with GitHub raw URLs based on order of appearance.
    
    Args:
        content (str): The file content to process
        file_type (str): The type of file ('md' or 'html')
        base_github_url (str): The base GitHub URL for raw content
        
    Returns:
        str: The updated content with replaced image paths
    """
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


def process_directory(directory: str) -> None:
    """
    Process all markdown and HTML files in the directory.
    
    Args:
        directory (str): Path to the directory containing files to process
        
    Raises:
        FileNotFoundError: If the directory doesn't exist
    """
    dir_path = Path(directory)
    if not dir_path.exists() or not dir_path.is_dir():
        raise FileNotFoundError(f"Directory not found: {directory}")
    
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


def main() -> None:
    """
    Parse command line arguments and process the directory.
    """
    parser = argparse.ArgumentParser(description='Replace image paths with GitHub raw URLs')
    parser.add_argument(
        'directory', 
        help='Directory containing markdown and HTML files'
    )
    
    args = parser.parse_args()
    
    try:
        process_directory(args.directory)
        print("Image replacement complete!")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()