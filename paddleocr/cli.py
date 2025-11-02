import argparse
from paddle_ocr_wrapper import PaddleOCRWrapper

def main():
    parser = argparse.ArgumentParser(description='PaddleOCR wrapper for batch processing')
    parser.add_argument('--input', '-i', required=True, 
                       help='Input image file or directory path')
    parser.add_argument('--output', '-o', required=True,
                       help='Output directory path')
    parser.add_argument('--device', '-d', default='gpu:0',
                       help='Device to use for inference (default: gpu:0)')
    parser.add_argument('--formats', '-f', nargs='+', 
                       default=['.png', '.jpg', '.jpeg'],
                       help='File formats to process (default: .png .jpg .jpeg)')
    
    args = parser.parse_args()
    
    # Initialize OCR wrapper
    ocr_wrapper = PaddleOCRWrapper(device=args.device)
    
    # Process images
    ocr_wrapper.process_images(
        input_path=args.input,
        output_path=args.output,
        file_formats=args.formats
    )

if __name__ == '__main__':
    main()