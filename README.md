Berikut adalah contoh `README.md` yang menjelaskan program `rebuild` dan cara instalasi menggunakan skrip `reverseshell_installer.sh`.

### `README.md`

```markdown
# ReverseShellBuilder (Rebuild)

ReverseShellBuilder (Rebuild) adalah alat yang digunakan untuk membuat berbagai jenis payload reverse shell dan menjalankannya pada listener tertentu. Alat ini mendukung berbagai jenis listener seperti `nc`, `ncat`, `socat`, `rustcat`, dan banyak lagi. Anda dapat menggunakan alat ini untuk mendengarkan koneksi dari sistem target setelah reverse shell berhasil dieksekusi.

## Fitur
- Menyediakan berbagai jenis payload reverse shell untuk listener yang berbeda.
- Mendukung banyak tool listener seperti `nc`, `ncat`, `socat`, `rustcat`, `pwncat`, dan lainnya.
- Menyediakan pilihan untuk membuat shell TTY interaktif.
- Menyimpan dan memuat sesi yang sudah ada.

## Instalasi

Untuk menginstal **ReverseShellBuilder**, Anda dapat menggunakan skrip instalasi otomatis yang telah disediakan, `reverseshell_installer.sh`. Skrip ini akan mendownload alat ini, memindahkannya ke `/usr/bin/`, serta memastikan bahwa semua dependensi yang diperlukan terinstal.

### Langkah-langkah Instalasi

1. **Download Skrip Installer**

   Pertama, download dan beri izin eksekusi pada skrip `reverseshell_installer.sh`:

   ```bash
   wget https://example.com/path/to/reverseshell_installer.sh
   chmod +x reverseshell_installer.sh
   ```

2. **Jalankan Skrip Installer**

   Setelah memberi izin eksekusi, jalankan skrip installer dengan hak akses root:

   ```bash
   sudo ./reverseshell_installer.sh
   ```

   Skrip ini akan melakukan hal berikut:
   - Memeriksa apakah alat yang dibutuhkan (`xterm`, `netcat`, `ncat`, `socat`, `busybox`, `rustcat`, `pwncat`) sudah terinstal.
   - Menginstal alat yang belum terinstal.
   - Mendownload dan memindahkan file `rebuild` ke `/usr/bin/`.
   - Memastikan file `rebuild` dapat dieksekusi.

### Persyaratan Sistem
- Sistem berbasis Linux (Debian/Ubuntu sangat disarankan).
- Akses root untuk instalasi dan konfigurasi.
- Koneksi internet untuk mendownload alat dan dependensi yang diperlukan.

### Menggunakan ReverseShellBuilder

Setelah instalasi selesai, Anda dapat menjalankan **ReverseShellBuilder** dengan perintah berikut:

```bash
rebuild
```

Program akan menampilkan antarmuka yang memungkinkan Anda untuk:
1. Mengonfigurasi alamat IP dan port untuk listener.
2. Memilih listener yang ingin Anda gunakan.
3. Melihat dan memilih berbagai payload reverse shell untuk digunakan.

### Uninstalasi

Untuk menghapus **ReverseShellBuilder**, Anda dapat menjalankan skrip uninstaller berikut:

1. **Download Skrip Uninstaller**

   ```bash
   wget https://example.com/path/to/uninstaller.sh
   chmod +x uninstaller.sh
   ```

2. **Jalankan Skrip Uninstaller**

   Jalankan skrip uninstaller dengan hak akses root untuk menghapus alat:

   ```bash
   sudo ./uninstaller.sh
   ```

   Skrip ini akan menghapus file `rebuild` dari `/usr/bin` tanpa mempengaruhi alat atau dependensi lainnya.

## Contributing

Jika Anda ingin berkontribusi pada proyek ini, Anda dapat melakukannya dengan mengirimkan pull request di GitHub. Pastikan untuk mengikuti pedoman pengembangan yang jelas.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
```

### Penjelasan:
- **Deskripsi Program**: Menjelaskan apa itu `ReverseShellBuilder` dan fitur-fiturnya.
- **Instruksi Instalasi**: Menyediakan langkah-langkah untuk menginstal program menggunakan skrip `reverseshell_installer.sh`.
- **Persyaratan Sistem**: Menjelaskan apa yang dibutuhkan untuk menjalankan program (misalnya sistem berbasis Linux, akses root).
- **Instruksi Penggunaan**: Memberikan informasi tentang cara menjalankan program dan menggunakan fungsinya.
- **Uninstalasi**: Menyediakan cara untuk menghapus program jika diperlukan.
- **Kontribusi**: Menyertakan informasi tentang bagaimana orang bisa berkontribusi pada proyek (ini opsional dan bisa diubah sesuai kebutuhan).
- **Lisensi**: Menyebutkan lisensi proyek (misalnya MIT License).

Skrip dan instruksi ini akan membantu pengguna memahami cara menginstal dan menggunakan alat dengan mudah. Jangan ragu untuk menyesuaikan URL dan informasi lebih lanjut jika diperlukan!
