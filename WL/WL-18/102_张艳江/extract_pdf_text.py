#!/usr/bin/env python3

import sys
from pdfminer.high_level import extract_text

def main():
    if len(sys.argv) != 3:
        print("Usage: {} <input_pdf> <output_txt>".format(sys.argv[0]))
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_txt = sys.argv[2]
    
    try:
        text = extract_text(input_pdf)
        with open(output_txt, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Text extracted successfully to {output_txt}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()