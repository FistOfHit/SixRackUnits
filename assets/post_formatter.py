#!/usr/bin/env python3
import argparse
import sys
import re
from pathlib import Path
from typing import Optional, List, Tuple

DEFAULT_HEADER_URL = "https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/header.png"
DEFAULT_FOOTER_URL = "https://raw.githubusercontent.com/FistOfHit/SixRackUnits/refs/heads/main/assets/logo.png"
SUBSTACK_URL = "https://sixrackunits.substack.com"


def validate_markdown(path: Path) -> None:
    """
    Validates the markdown file for common formatting issues.
    
    Args:
        path (Path): Path to the Markdown file to validate
    """
    content = path.read_text(encoding='utf-8')
    issues = []
    
    # Check for broken image links
    image_pattern = r'!\[.*?\]\((.*?)\)'
    images = re.findall(image_pattern, content)
    for img in images:
        if not img.startswith(('http://', 'https://')):
            if not Path(img).exists():
                issues.append(f"Warning: Local image path may be invalid: {img}")
    
    # Check for broken links
    link_pattern = r'\[.*?\]\((.*?)\)'
    links = re.findall(link_pattern, content)
    for link in links:
        if not link.startswith(('http://', 'https://', '#', 'mailto:')):
            if not Path(link).exists():
                issues.append(f"Warning: Local link path may be invalid: {link}")
    
    # Check for consistent header formatting
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('#'):
            # Check if there's a space after the # symbols
            if not re.match(r'^#+\s', line):
                issues.append(f"Line {i+1}: Header missing space after # symbols: {line}")
    
    # Check for empty sections
    header_lines = [i for i, line in enumerate(lines) if line.startswith('#')]
    for i in range(len(header_lines) - 1):
        current = header_lines[i]
        next_header = header_lines[i + 1]
        if next_header - current <= 1:
            issues.append(f"Warning: Empty section after header on line {current+1}")
    
    # Check for consistent list formatting
    for i, line in enumerate(lines):
        if re.match(r'^\s*[\*\-\+]\s', line):
            if not re.match(r'^\s*[\*\-\+]\s+', line):
                issues.append(f"Line {i+1}: List item missing space after bullet: {line}")
    
    # Check if the table of contents is present
    if not has_toc(content):
        issues.append("Warning: No table of contents found. Consider adding one with --add-toc")
    
    # Report issues
    if issues:
        print("\nMarkdown validation found the following issues:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("Markdown validation: No issues found.")


def extract_headers(content: str) -> List[Tuple[int, str, str]]:
    """
    Extract headers from markdown content.
    
    Args:
        content (str): Markdown content
        
    Returns:
        List[Tuple[int, str, str]]: List of tuples containing (header_level, header_text, header_id)
    """
    headers = []
    lines = content.split('\n')
    
    for line in lines:
        # Match headers (# Header)
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            
            # Create GitHub-style header ID (lowercase, spaces to hyphens, remove punctuation)
            header_id = text.lower()
            header_id = re.sub(r'[^\w\s-]', '', header_id)  # Remove punctuation
            header_id = re.sub(r'\s+', '-', header_id)      # Replace spaces with hyphens
            
            headers.append((level, text, header_id))
    
    return headers


def has_footer(content: str, footer_url: str) -> bool:
    """
    Check if the content already has the specified footer.
    
    Args:
        content (str): Markdown content
        footer_url (str): URL for the footer image
        
    Returns:
        bool: True if footer exists, False otherwise
    """
    footer = f"[![]({footer_url})]({SUBSTACK_URL})"
    return content.strip().endswith(footer)


def has_header(content: str, header_url: str) -> bool:
    """
    Check if the content already has the specified header.
    
    Args:
        content (str): Markdown content
        header_url (str): URL for the header image
        
    Returns:
        bool: True if header exists, False otherwise
    """
    header = f"[![]({header_url})]({SUBSTACK_URL})"
    return content.strip().startswith(header)


def add_header_footer(file_path: str, header_url: Optional[str] = None, 
                     footer_url: Optional[str] = None) -> None:
    """
    Adds a header and footer to a Markdown file.
    
    Args:
        file_path (str): Path to the Markdown file to modify
        header_url (Optional[str]): URL for the header image, uses default if None
        footer_url (Optional[str]): URL for the footer image, uses default if None
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
    """
    # Validate the file path
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File '{file_path}' not found.")
    
    if not path.suffix.lower() in ['.md', '.markdown']:
        raise ValueError(f"File '{file_path}' is not a Markdown file.")
    
    header_img_url = header_url or DEFAULT_HEADER_URL
    footer_img_url = footer_url or DEFAULT_FOOTER_URL
    
    # Create markdown links
    header = f"[![]({header_img_url})]({SUBSTACK_URL})\n\n"
    footer = f"\n\n[![]({footer_img_url})]({SUBSTACK_URL})"
    
    content = path.read_text(encoding='utf-8')    
    
    # Check if the header already exists
    if has_header(content, header_img_url):
        print(f"Header already exists in '{file_path}'")
    else:
        content = header + content

    # Check if the footer already exists
    if has_footer(content, footer_img_url):
        print(f"Footer already exists in '{file_path}'")
    else:
        content = content + footer

    path.write_text(content, encoding='utf-8')

    print(f"Successfully processed '{file_path}'")
    
    # Validate the markdown after modifications
    validate_markdown(path)


def create_backup(file_path: str) -> None:
    """
    Creates a backup of the file before modifying it.
    
    Args:
        file_path (str): Path to the file to backup
    """
    path = Path(file_path)
    backup_path = path.with_suffix(f"{path.suffix}.bak")
    path.copy(backup_path)
    print(f"Created backup at '{backup_path}'")


def process_toc(file_path: str) -> None:
    """
    Adds a table of contents to a Markdown file if not already present.
    
    Args:
        file_path (str): Path to the Markdown file to modify
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File '{file_path}' not found.")
    
    content = path.read_text(encoding='utf-8')
    
    # Check if TOC already exists
    toc_patterns = [
        r'#\s+Table\s+of\s+Contents',
        r'#\s+Contents',
        r'#\s+TOC',
    ]
    
    for pattern in toc_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            print(f"Table of contents already exists in '{file_path}'")
            return
    
    # Extract headers
    headers = []
    lines = content.split('\n')
    
    # Find the title of the document (first h1)
    title = None
    for line in lines:
        match = re.match(r'^#\s+(.+)$', line)
        if match:
            title = match.group(1).strip()
            break
    
    for line in lines:
        # Match headers (# Header)
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            
            # Create GitHub-style header ID
            header_id = text.lower()
            header_id = re.sub(r'[^\w\s-]', '', header_id)  # Remove punctuation
            header_id = re.sub(r'\s+', '-', header_id)      # Replace spaces with hyphens
            
            headers.append((level, text, header_id))
    
    # Filter out any h1 headers that might be titles or TOC
    content_headers = [h for h in headers if not (h[0] == 1 and h[1] == title) and h[1].lower() != "table of contents"]
    
    if not content_headers:
        print(f"No headers found to create table of contents in '{file_path}'")
        return
    
    # Generate TOC
    toc = ["# Table of Contents\n"]
    for level, text, header_id in content_headers:
        if text.lower() == "table of contents":
            continue
            
        indent = "  " * (level - 1)
        
        # Make all TOC entries bold
        toc.append(f"{indent}- [**{text}**](#{header_id})")
    
    toc_content = "\n".join(toc) + "\n\n"
    
    # Find position to insert TOC
    first_h1_index = -1
    for i, line in enumerate(lines):
        if re.match(r'^#\s+', line):
            first_h1_index = i
            break
    
    if first_h1_index >= 0:
        # Insert after the first header and any blank lines that follow it
        insert_pos = first_h1_index + 1
        while insert_pos < len(lines) and not lines[insert_pos].strip():
            insert_pos += 1
        
        # Insert TOC
        lines.insert(insert_pos, "\n" + toc_content)
        updated_content = "\n".join(lines)
    else:
        # No h1 header found, insert at the beginning
        updated_content = toc_content + content
    
    path.write_text(updated_content, encoding='utf-8')
    print(f"Added table of contents to '{file_path}'")


def has_toc(content: str) -> bool:
    """
    Check if the content already has a table of contents.
    
    Args:
        content (str): Markdown content
        
    Returns:
        bool: True if TOC exists, False otherwise
    """
    # Look for common TOC headers
    toc_patterns = [
        r'#\s+Table\s+of\s+Contents',
        r'#\s+Contents',
        r'#\s+TOC',
    ]
    
    for pattern in toc_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    
    return False


def main() -> None:
    """Parse command line arguments and process the file."""
    parser = argparse.ArgumentParser(
        description='Add header and footer image links to a Markdown file.'
    )
    parser.add_argument(
        'file_path', 
        help='Path to the Markdown file to modify'
    )
    parser.add_argument(
        '--header-url',
        help='Custom URL for the header image',
        default=DEFAULT_HEADER_URL
    )
    parser.add_argument(
        '--footer-url',
        help='Custom URL for the footer image',
        default=DEFAULT_FOOTER_URL
    )
    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Only validate the markdown without adding header/footer'
    )
    parser.add_argument(
        '--backup',
        action='store_true',
        help='Create a backup of the file before modifying'
    )
    parser.add_argument(
        '--add-toc',
        action='store_true',
        help='Add a table of contents if not present',
        default=True
    )
    
    args = parser.parse_args()
    
    try:
        path = Path(args.file_path)
        if not path.exists():
            raise FileNotFoundError(f"File '{args.file_path}' not found.")
        
        if args.backup:
            create_backup(args.file_path)
        
        if args.validate_only:
            validate_markdown(path)
            return
        
        if args.add_toc:
            process_toc(args.file_path)
        
        add_header_footer(args.file_path, args.header_url, args.footer_url)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
