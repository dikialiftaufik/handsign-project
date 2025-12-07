import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from ultralytics import YOLO

def main():
    # 1. LOAD MODEL
    # Kita menggunakan 'yolov8n.pt' (nano) karena paling ringan dan cepat untuk pemula/laptop standar.
    # Model ini akan mendownload weight pre-trained secara otomatis.
    print("Loading model...")
    model = YOLO('yolov8n.pt') 

    # 2. TRAINING
    # data='data.yaml' merujuk ke file konfigurasi yang didapat dari download dataset
    # epochs=50: Berapa kali model melihat seluruh data
    # imgsz=640: Ukuran gambar saat training
    print("Starting training...")
    results = model.train(
        data='data.yaml',  
        epochs=50,         
        imgsz=640,
        batch=16,
        name='handsign_model' # Nama folder hasil training nanti
    )

    # 3. VALIDASI & VISUALISASI AWAL
    # Mengevaluasi performa model pada data validasi
    metrics = model.val()
    print(f"Map50-95: {metrics.box.map}") # Mean Average Precision

if __name__ == '__main__':
    # Fix untuk multiprocessing di Windows
    main()