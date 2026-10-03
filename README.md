<div align="center">
# 🗺️ Pathfinding Visualizer: Dijkstra vs A* on Real Maps

**OpenStreetMap məlumatları üzərində real şəhər küçələrində Dijkstra və A\* (A-Star) alqoritmlərinin canlı vizualizasiyası və müqayisəsi.**

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OSMnx](https://img.shields.io/badge/OSMnx-Geospatial-orange.svg?style=for-the-badge)](https://osmnx.readthedocs.io/)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Data-lightgrey.svg?style=for-the-badge)](https://networkx.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

<br/>
⭐ **Layihə xoşunuza gəldisə, zəhmət olmasa repozitoriyaya bir ulduz (Star) ataraq dəstək olun!** ⭐

[Xüsusiyyətlər](#-əsas-xüsusiyyətlər) • [Quraşdırma](#-quraşdırma) • [İstifadə Qaydası](#-istifadə-qaydası) • [Layihə Strukturu](#-layihə-strukturu) • [Alqoritmik İzah](#-alqoritmlərin-müqayisəsi-və-riyazi-əsası) • [Müəllif](#-müəllif-və-əlaqə)
</div>

---

## 📌 Layihə Haqqında
Bu layihə istənilən şəhərin və ya rayonun real yol infrastrukturunu qraf modeli şəklində OpenStreetMap-dən çəkir və ən populyar iki qısa yol axtarış alqoritmini (Dijkstra və A\*) **yan-yana, sinxron və animasiyalı** şəkildə qarşılaşdırır. Vizual dizayn müasir, qaranlıq (Dark Cyberpunk / Sci-Fi) üslubda tərtib edilmişdir. Hər iki alqoritmin kəşf etdiyi yollar addım-addım vizuallaşdırılır, axtarış başa çatdıqda isə tapılmış optimal marşrut parlaq neon yaşıl xətlə ekranda vurğulanır.

---

## ✨ Əsas Xüsusiyyətlər
- **🌍 Qlobal Region Seçimi:** Proqram açıldıqda konsola daxil etdiyiniz istənilən şəhər/region adını dinamik yükləyir (Məs: `Baku, Azerbaijan`, `Kadıköy, Istanbul`, `Berlin, Germany`).
- **🔗 Əlaqəli Qraf Təhlükəsizliyi (Strongly Connected Components):** Yüklənmiş qrafın daxilində dalan və ya təcrid olunmuş adacıqları təmizləyərək hər iki nöqtə arasında mütləq yolun tapılmasını təmin edir.
- **⚡ Canlı Animasiya:** Alqoritmlərin axtarış prosesi (node exploration) qaranlıq xəritə üzərində vizual olaraq göstərilir.
- **📊 Performans Müqayisəsi:** Hər iki alqoritm axtarışı bitirdikdən sonra sərf olunan zaman, ziyarət edilən qovşaq (node) sayı və tapılan marşrutun ümumi məsafəsi konsolda müqayisə edilir.

---

## 🚀 Quraşdırma

Layihəni öz kompüterinizdə işlətmək üçün aşağıdakı addımları izləyin:

1. Repozitoriyanı klonlayın:
```bash
git clone [https://github.com/Ferid18/xerite.git](https://github.com/Ferid18/xerite.git)
cd xerite
