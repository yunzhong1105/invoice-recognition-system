from paddle_ocr_wrapper import PaddleOCRWrapper

def main():
    # 初始化 OCR，使用 GPU
    ocr = PaddleOCRWrapper(device="gpu:0")
    
    # 使用您目錄中的實際數據路徑
    input_path = "/home/yunzhong1105/paddleocr/angle test/images"
    output_path = "/home/yunzhong1105/paddleocr/test_results"
    
    # 處理圖片
    ocr.process_images(
        input_path=input_path,
        output_path=output_path,
        file_formats=['.png']  # 根據您原始程式碼中的使用情況，設定為 .png
    )

if __name__ == "__main__":
    main()