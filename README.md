file best.pt merupakan hasil model YOLOv8 yang sudah dilatih dengan jumlah epoch sebanyak 50. Untuk dapat menggunakan model tersebut menggunakan kamera secara real-time diperlukan beberapa langkah seperti:
1. ikuti langkah untuk menginstall package YOLOv8 pada ultralytics https://github.com/ultralytics/ultralytics
2. buka file real-time.py lalu sesuaikan syntax ini dengan lokasi path dari file best.pt 
model = YOLO('runs/detect/train22/weights/best.pt')
3. jalankan program lalu ambil atau pilih objek yang ingin dideteksi (untuk studi kasus program ini dikhususkan untuk crack detection pada sebuah struktur)
4. gambar hasil deteksi retakan menggunakan kamera secara real-time![Screenshot 2023-08-15 130350](https://github.com/yosiasruliano98/Crack-Detection-YOLOv8/assets/139975558/f3df43d4-d944-4a0a-9f29-fc8b12fd7ca4)
