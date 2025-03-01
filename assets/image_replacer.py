import re
import argparse
from pathlib import Path
from typing import List


def find_image_files(images_dir: Path) -> List[str]:
    """Find all image files in the images directory and sort them numerically."""
    if not images_dir.exists() or not images_dir.is_dir():
        raise ValueError(f"Images directory not found: {images_dir}")
    
    image_files = []
    for ext in ['png', 'jpg', 'jpeg', 'gif', 'svg']:
        image_files.extend(list(images_dir.glob(f"*.{ext}")))
    
    # Sort numerically by the filename (without extension)
    return sorted(image_files, key=lambda x: int(x.stem) if x.stem.isdigit() else float('inf'))


def replace_images_in_file(file_path: Path, image_files: List[Path], images_dir_name: str) -> int:
    """Replace image URLs in a file with local image references."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Different patterns for Markdown and HTML
    if file_path.suffix == '.md':
        # Match Markdown image syntax: ![alt text](url)
        pattern = r'!\[.*?\]\((https?://[^\s)]+)\)'
        replacement_format = r'![](./{}/{})'
    else:  # HTML
        # Match HTML img tags: <img src="url" ...>
        pattern = r'<img[^>]*src=["\'](https?://[^\s"\'>]+)["\'][^>]*>'
        replacement_format = r'<img src="./{}/{}" alt="">'
    
    matches = re.findall(pattern, content)
    if not matches:
        return 0
    
    # Replace each match with a local image reference
    new_content = content
    for i, match in enumerate(matches):
        if i >= len(image_files):
            print(f"Warning: Not enough local images to replace all URLs in {file_path}")
            break
            
        local_image_path = replacement_format.format(
            images_dir_name, 
            image_files[i].name
        )
        
        if file_path.suffix == '.md':
            # Use the full local_image_path instead of constructing it again
            new_content = new_content.replace(f'![alt]({match})', local_image_path)
            new_content = new_content.replace(f'![]({match})', local_image_path)
        else:  # HTML
            # This is a simplified replacement for HTML - in real use you might need a more robust HTML parser
            new_content = re.sub(
                r'<img[^>]*src=["\']' + re.escape(match) + r'["\'][^>]*>', 
                local_image_path, 
                new_content
            )
    
    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return len(matches) if len(matches) <= len(image_files) else len(image_files)


def main():
    parser = argparse.ArgumentParser(description='Replace image URLs with local image references')
    parser.add_argument('directory', help='Directory containing .md and .html files')
    args = parser.parse_args()
    
    base_dir = Path(args.directory)
    if not base_dir.exists() or not base_dir.is_dir():
        print(f"Error: Directory not found: {base_dir}")
        return
    
    images_dir = base_dir / 'images'
    try:
        image_files = find_image_files(images_dir)
        if not image_files:
            print(f"No image files found in {images_dir}")
            return
        print(f"Found {len(image_files)} image files")
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # Process all .md and .html files in the directory
    total_replacements = 0
    for file_ext in ['.md', '.html']:
        for file_path in base_dir.glob(f'**/*{file_ext}'):
            # Skip files in the images directory
            if 'images' in file_path.parts:
                continue
                
            try:
                replacements = replace_images_in_file(file_path, image_files, 'images')
                if replacements > 0:
                    print(f"Replaced {replacements} image URLs in {file_path}")
                    total_replacements += replacements
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    print(f"Total replacements: {total_replacements}")


if __name__ == "__main__":
    main()
