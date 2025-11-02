import os
from glob import glob
from typing import List, Optional
from paddleocr import PaddleOCR

class PaddleOCRWrapper:
    def __init__(self, device: str = "gpu:0"):
        """Initialize PaddleOCR with specific device.
        
        Args:
            device (str): Device to use for inference ("gpu:0", "cpu", etc.)
        """
        self.ocr = PaddleOCR(
            device=device,
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False
        )
    
    def process_images(self, 
                      input_path: str, 
                      output_path: str,
                      file_formats: Optional[List[str]] = None) -> None:
        """Process images from input path and save results to output path.
        
        Args:
            input_path (str): Path to input directory or single image file
            output_path (str): Path to output directory
            file_formats (List[str], optional): List of file formats to process. 
                                              Defaults to ['.png', '.jpg', '.jpeg']
        """
        if file_formats is None:
            file_formats = ['.png', '.jpg', '.jpeg']
            
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Handle both single file and directory inputs
        if os.path.isfile(input_path):
            image_paths = [input_path]
        else:
            image_paths = []
            for fmt in file_formats:
                image_paths.extend(glob(os.path.join(input_path, f"*{fmt}")))
        
        for img_path in image_paths:
            file_name = os.path.splitext(os.path.basename(img_path))[0]
            result_dir = os.path.join(output_path, file_name)
            
            # Create directory for current image results
            os.makedirs(result_dir, exist_ok=True)
            
            # Run OCR inference
            result = self.ocr.predict(input=img_path)
            
            # Save results
            for res in result:
                res.save_to_img(result_dir)
                res.save_to_json(result_dir)
            print(f'Results saved to "{result_dir}"')

