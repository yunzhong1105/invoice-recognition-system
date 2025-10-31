#!/bin/bash

# Create or clear the training records file
echo "" > train_records.txt

# Function to print separator
print_separator() {
    printf '%*s\n' 80 '' | tr ' ' '=' | tee -a train_records.txt
}

# Function to run training and handle errors
run_training() {
    print_separator
    echo "Starting training with model: $1, epochs: $2, image size: $3, batch: $4" | tee -a train_records.txt
    print_separator
    
    # Run training and capture all output
    {
        yolo detect train data=full_2025.yaml model=$1 epochs=$2 imgsz=$3 device=0 batch=$4 2>&1
    } | tee -a train_records.txt
    
    if [ ${PIPESTATUS[0]} -ne 0 ]; then
        echo "Training failed for model: $1" | tee -a train_records.txt
        return 1
    else
        echo "Training completed successfully for model: $1" | tee -a train_records.txt
        return 0
    fi
}

# Train different model variants with different settings
# run_training "yolov10m.pt" 100 640 16
# run_training "yolov10m.pt" 200 640 16
# run_training "yolov10m.pt" 300 640 16
# run_training "yolov10m.pt" 100 1280 4
# run_training "yolov10m.pt" 200 1280 4
# run_training "yolov10m.pt" 300 1280 4

# run_training "yolov10l.pt" 100 640 8
# run_training "yolov10l.pt" 200 640 8
# run_training "yolov10l.pt" 300 640 8
# run_training "yolov10l.pt" 100 640 16
# run_training "yolov10l.pt" 200 640 16
# run_training "yolov10l.pt" 300 640 16
run_training "yolov10l.pt" 100 1280 4
# run_training "yolov10l.pt" 200 1280 4
# run_training "yolov10l.pt" 300 1280 4