import cv2
from ultralytics import YOLO
import math

# 1. LOAD MODEL HASIL TRAINING
# Ubah path di bawah ini sesuai lokasi best.pt Anda setelah training selesai
path_to_model = 'runs/detect/handsign_model/weights/best.pt'

try:
    model = YOLO(path_to_model)
except Exception as e:
    print(f"Error: Model tidak ditemukan di {path_to_model}. Pastikan training sudah selesai.")
    exit()

# Setup Webcam (0 biasanya adalah webcam default)
cap = cv2.VideoCapture(0)
cap.set(3, 640) # Lebar
cap.set(4, 480) # Tinggi

# Daftar Nama Kelas (Sesuaikan dengan data.yaml jika urutannya beda)
# Biasanya dataset ASL urut A-Z
classNames = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

while True:
    success, img = cap.read()
    if not success:
        break

    # 2. INFERENCE
    # stream=True membuat proses lebih efisien untuk video
    results = model(img, stream=True)

    # 3. VISUALISASI HASIL
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # a. Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            # Gambar kotak di sekitar tangan
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # b. Confidence Score (Seberapa yakin model?)
            conf = math.ceil((box.conf[0] * 100)) / 100

            # c. Class Name (Huruf apa?)
            cls = int(box.cls[0])
            if cls < len(classNames):
                current_class = classNames[cls]
            else:
                current_class = "Unknown"

            # Tampilkan Label
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            
            # Label di atas kotak
            cv2.putText(img, f'{current_class} {conf}', org, font, fontScale, color, thickness)

    # Tampilkan window webcam
    cv2.imshow('Webcam', img)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()