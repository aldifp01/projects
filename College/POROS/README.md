# FREEPASS OPS

## TASK
---
1. Buat sebuah file yaml docker-compose untuk (pilih salah satu)
 * Web Environment : Harus memiliki service berupa 1 Load Balancer, 1 Database Server, 1 Web Server
 * Streaming Data : Harus memiliki service berupa 1 Kafka Server, 1 Zookeeper Server, serta tools lain untuk memproses data yang diperoleh tersebut
Ketentuan : cukup pilih salah satu, kemudian pastikan semua service bisa berjalan dan diakses dari luar container dan file docker-compose yang telah dibuat harus bisa digunakan user tanpa harus melakukan konfigurasi apapun lagi. Untuk web environment cukup buat halaman website sederhana saja tidak perlu membuat landing page.

2. Buatlah sebuah Dockerfile untuk membuat Docker Image yang berisikan minimal 2 service.\
Ketentuan : Hasil image di-push ke Docker Hub, image dan service bisa digunakan user tanpa harus melakukan konfigurasi apapun lagi. Untuk servicenya sendiri boleh menggunakan dari opsi nomor satu yang tidak diambil, misalnya nomor 1 mengambil web environment maka untuk nomor 2 boleh service untuk streaming data dan begitu juga sebaliknya.

3. Buatkan sebuah Vagrantfile dengan provider VirtualBox dan provision menggunakan shell berisi minimal 2 service lain apapun.\
Ketentuan : OS yang digunakan wajib GNU/Linux non-GUI, VM dan semua service harus bisa berjalan & diakses dari luar VM

4. Buatkan sebuah Packer template dengan builder VirtualBox dan provision menggunakan Ansible berisi minimal 2 service apapun selain pada no 3.\
Ketentuan : OS yang digunakan wajib GNU/Linux non-GUI, VM dan semua service harus bisa berjalan & diakses dari luar VM

5. Challenger harus menyelesaikan minimal 3/4 task yang ada untuk mendapatkan freepass

6. Buat dokumentasi dalam markdown dengan nama ```README.md``` dengan lengkap dan rapi yang harus berisikan:
    - Nama challenger
    - Penjelasan singkat tentang task yang dikerjakan
    - Penjelasan singkat tentang source code yang dibuat
    - Foto/Screenshot WIP (Work in Progress)

7. Manfaatkan fitur Firewall/SELinux sebaik-baiknya

8. Untuk service berupa database, minimal ada 1 user (non root) dengan 1 database berisi 1 tabel berisi >= 4 query yang merupakan operasi CRUD

9. Halaman website & database SQL dibuat di luar container/virtual machine (manfaatkan fitur dump, backup, restore, move, copy, volumes, dsb)

10. Challenger tidak boleh mengubah apapun di dalam container/virtual machine setelah container/virtual machine berjalan (Output apa adanya tanpa sentuhan apapun lagi). Semua perubahan harus dilakukan pada source code sebelum dijalankan.

11. Upload source code dan write up ke repositori GitHub atau alternatif lainnya.

---

#### Catatan:
> Challenger diperbolehkan mencari referensi untuk mengerjakan task freepass di internet. 
> Challenger diharapkan tidak mengerjakan task bersama-sama dengan challenger lain apalagi memplagiasi karya orang lain!
