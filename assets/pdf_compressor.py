#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess
from pathlib import Path
from typing import Optional, Union


def get_file_size_mb(file_path: str) -> float:
    """
    Return the file size in megabytes.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        float: Size of the file in megabytes
    """
    return os.path.getsize(file_path) / (1024 * 1024)


def compress_pdf(input_path: str, output_path: Optional[str] = None, 
                compression_level: Optional[int] = None) -> Optional[str]:
    """
    Compress a PDF file using Ghostscript.
    
    Args:
        input_path (str): Path to the input PDF file
        output_path (Optional[str]): Path for the output PDF file (default: input_path with '_compressed' suffix)
        compression_level (Optional[int]): Compression level (0-4, where 0 is lowest quality, 4 is highest)
        
    Returns:
        Optional[str]: Path to the compressed file, or None if compression failed
        
    Raises:
        FileNotFoundError: If the input file doesn't exist
        ValueError: If an invalid compression level is provided
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Determine output path if not specified
    if output_path is None:
        input_file = Path(input_path)
        output_path = str(input_file.with_stem(f"{input_file.stem}_compressed"))
    
    # If compression level is not specified, use default
    if compression_level is None:
        compression_level = 2  # Default medium compression
    
    # Define quality settings for different compression levels
    quality_settings = {
        0: ["/default", "/screen"],  # Lowest quality, highest compression
        1: ["/ebook"],               # Low quality
        2: ["/printer"],             # Medium quality
        3: ["/prepress"],            # High quality
        4: ["/default", "/prepress"] # Highest quality, lowest compression
    }
    
    # Ensure compression level is valid
    if compression_level not in quality_settings:
        raise ValueError(f"Invalid compression level: {compression_level}. Must be 0-4.")
    
    # Build Ghostscript command
    gs_command = [
        "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=" + quality_settings[compression_level][0],
        "-dNOPAUSE", "-dQUIET", "-dBATCH",
        f"-sOutputFile={output_path}", input_path
    ]
    
    # Execute Ghostscript
    try:
        subprocess.run(gs_command, check=True)
        
        # Print compression results
        original_size = get_file_size_mb(input_path)
        compressed_size = get_file_size_mb(output_path)
        reduction = (1 - compressed_size / original_size) * 100
        
        print(f"Original size: {original_size:.2f}MB")
        print(f"Compressed size: {compressed_size:.2f}MB")
        print(f"Reduction: {reduction:.2f}%")
        
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"Error compressing PDF: {e}")
        if os.path.exists(output_path):
            os.remove(output_path)
        return None


def main() -> None:
    """
    Parse command line arguments and process the PDF file.
    """
    parser = argparse.ArgumentParser(description="Compress PDF files")
    parser.add_argument(
        "input_path", 
        help="Path to the input PDF file"
    )
    parser.add_argument(
        "-o", "--output", 
        help="Path for the output PDF file"
    )
    parser.add_argument(
        "-c", "--compression-level", 
        type=int, 
        choices=range(5),
        help="Compression level (0-4, where 0 is highest compression, 4 is highest quality)"
    )
    
    args = parser.parse_args()
    
    try:
        compress_pdf(
            args.input_path,
            args.output,
            args.compression_level
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
