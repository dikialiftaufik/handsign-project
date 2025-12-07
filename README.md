🖐️ ASL Alphabet Detection using YOLOv8

Proyek Computer Vision untuk mendeteksi alfabet Bahasa Isyarat Amerika (ASL) A-Z secara real-time menggunakan webcam. Proyek ini dibangun menggunakan framework Ultralytics YOLOv8.


📂 Struktur Proyek

├── datasets/
│   ├── train/
│   │   ├── images/      
│   │   └── labels/      
│   └── valid/
│       ├── images/
│       └── labels/
│   └── test/
│       ├── images/
│       └── labels/
├── data.yaml            <-- File konfigurasi dataset
├── train_model.py       <-- Script training
└── detect_webcam.py     <-- Script testing




🚀 Cara Menjalankan (Step-by-Step)

1. Clone Repository & Setup Environment

# Clone repository ini
git clone https://github.com/dikialiftaufik/handsign-project.git
cd handsign-project

# Buat Virtual Environment (Windows)
python -m venv venv
venv\Scripts\activate

# Buat Virtual Environment (Mac/Linux)
python3 -m venv venv
source venv/bin/activate



2. Install Library

pip install ultralytics opencv-python matplotlib



3. Persiapan Dataset

Visit Roboflow Universe: [ASL Letters by David Lee](https://universe.roboflow.com/david-lee-d0rhs/american-sign-language-letters/dataset/6).

Download dataset dengan format YOLOv8.

Ekstrak dan letakkan folder train, valid, test ke dalam folder datasets/ di root proyek.

Pastikan file data.yaml sudah dikonfigurasi dengan benar, ganti code di line 1-3 menjadi berikut:
train: datasets/train/images
val: datasets/valid/images
test: datasets/test/images


4. Training Model (Opsional)

Jika ingin melatih model dari awal:

python train_model.py


Catatan: Proses ini memakan waktu lama tergantung spesifikasi hardware (GPU/CPU).


5. Menjalankan Deteksi Real-Time

Jalankan:

python detect_webcam.py


Tekan 'q' untuk keluar dari aplikasi.

🤖 Model Performance

Epochs: 50

Model Base: YOLOv8 Nano (n)

Dataset: ASL Letters (Roboflow)
