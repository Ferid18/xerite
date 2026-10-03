<div align="center">

# 🗺️ Pathfinding Visualizer: Dijkstra vs A* on Real Maps

**OpenStreetMap məlumatları üzərində real şəhər küçələrində Dijkstra və A\* (A-Star) alqoritmlərinin canlı vizualizasiyası və müqayisəsi.**

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OSMnx](https://img.shields.io/badge/OSMnx-Geospatial-orange.svg?style=for-the-badge)](https://osmnx.readthedocs.io/)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Data-lightgrey.svg?style=for-the-badge)](https://networkx.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

<br/>

⭐ **Layihə xoşunuza gəldisə, zəhmət olmasa repozitoriyaya bir ulduz (Star) ataraq dəstək olun!** ⭐

[Xüsusiyyətlər](#-əsas-xüsusiyyətlər) •
[Quraşdırma](#-quraşdırma) •
[İstifadə Qaydası](#-istifadə-qaydası) •
[Layihə Strukturu](#-layihə-strukturu) •
[Alqoritmik İzah](#-alqoritmlərin-müqayisəsi-və-riyazi-əsası) •
[Müəllif](#-müəllif-və-əlaqə)

</div>

---

## 📌 Layihə Haqqında

Bu layihə istənilən şəhərin və ya rayonun real yol infrastrukturunu qraf modeli şəklində OpenStreetMap-dən çəkir və ən populyar iki qısa yol axtarış alqoritmini (Dijkstra və A\*) **yan-yana, sinxron və animasiyalı** şəkildə qarşılaşdırır.

Vizual dizayn müasir, qaranlıq (Dark Cyberpunk / Sci-Fi) üslubda tərtib edilmişdir. Hər iki alqoritmin kəşf etdiyi yollar addım-addım vizuallaşdırılır, axtarış başa çatdıqda isə tapılmış optimal marşrut parlaq neon yaşıl xətlə ekranda vurğulanır.

---

## ✨ Əsas Xüsusiyyətlər

- **🌍 Qlobal Region Seçimi:** Proqram açıldıqda konsola daxil etdiyiniz istənilən şəhər/region adını dinamik yükləyir (Məs: `Baku, Azerbaijan`, `Kadıköy, Istanbul`, `Berlin, Germany`).
- **🔗 Əlaqəli Qraf Təhlükəsizliyi (Strongly Connected Components):** Yüklənmiş qrafın daxilində dalan və ya təcrid olunmuş adacıqları təmizləyərək hər iki nöqtə arasında mütləq yolun tapılmasını təmin edir.
- **⚡ Canlı Animasiya (Dual Engine):** `matplotlib.animation` vasitəsilə eyni anda iki fərqli axtarış strategiyasının necə yayıldığını addım-addım göstərir.
- **🎯 Yolun Vurğulanması (Optimal Path Highlight):** Alqoritmlər hədəfə çatdıqda tapılmış ən qısa trayektoriya dərhal parlaq yaşıl neon xətlə çəkilir.
- **📊 Real Zamanlı Statistika:** Titul panelində hər iki alqoritmin neçə tili (edge) ziyarət etdiyi canlı göstərilir.

---

## 📂 Layihə Strukturu

Layihənin qovluq və fayl arxitekturası:

```text
dijkstra-vs-astar/
├── assets/
│   └── preview.gif              # Önizləmə animasiyası və ya skrinşotlar
├── src/
│   ├── algorithms/
│   │   ├── __init__.py
│   │   ├── dijkstra.py          # Dijkstra prioritet növbə məntiqi
│   │   └── astar.py             # A* evristik axtarış məntiqi
│   ├── graph_loader.py          # OSMnx vasitəsilə xəritə və qraf emalı
│   └── visualizer.py            # Matplotlib animasiya və Dark UI mühərriki
├── interactive_path.py          # Əsas icra skripti (Quickstart)
├── requirements.txt             # Tələb olunan Python paketləri
├── LICENSE                      # MIT Lisenziyası
└── README.md                    # Layihə sənədləşməsi
```

---

## 🛠️ Quraşdırma

### 1. Repozitoriyanı klonlayın
```bash
git clone https://github.com/Ferid18/dijkstra-vs-astar.git
cd dijkstra-vs-astar
```

### 2. Virtual mühit yaradın və aktivləşdirin (Tövsiyə olunur)
```bash
# Windows üçün:
python -m venv venv
venv\Scripts\activate

# macOS / Linux üçün:
python3 -m venv venv
source venv/bin/activate
```

### 3. Asılılıqları quraşdırın
```bash
pip install -r requirements.txt
```

> **Qeyd:** Əgər `requirements.txt` yoxdursa, birbaşa aşağıdakı əmrlə quraşdıra bilərsiniz:
> ```bash
> pip install osmnx networkx matplotlib
> ```

---

## 🚀 İstifadə Qaydası

Skripti işə salın:

```bash
python interactive_path.py
```

İcra zamanı proqram sizdən xəritəsini görmək istədiyiniz regionu soruşacaq:

```text
Region daxil edin (məs: 'Mitte, Berlin, Germany' və ya 'Baku, Azerbaijan'):
```

### Nümunə girişlər:
* `Baku, Azerbaijan` — Bakı şəhəri mərkəzi
* `Kadıköy, Istanbul, Turkey` — İstanbul Kadıköy ərazisi
* `Mitte, Berlin, Germany` *(Boş buraxıb Enter vursanız, standart olaraq Berlin seçilir)*
* `Manhattan, New York, USA`

---

## 🧠 Alqoritmlərin Müqayisəsi və Riyazi Əsası

### 1. Dijkstra Alqoritmi
Dijkstra alqoritmi təyinat nöqtəsinin harada olduğunu nəzərə almadan başlanğıcdan etibarən bütün istiqamətlərə bərabər dalğa şəklində yayılır.
$$\text{Cost Function: } f(n) = g(n)$$
* $g(n)$ — Başlanğıc nöqtədən cari $n$ düyününə qədər olan faktiki məsafə (çəki).

### 2. $A^*$ (A-Star) Alqoritmi
$A^*$ alqoritmi Dijkstra-nın təkmilləşdirilmiş formasıdır. O, faktiki məsafəyə əlavə olaraq cari nöqtədən hədəfə olan təxmini düz xətt məsafəsini (Evklid evristikasını) hesablayır və birbaşa hədəfə doğru meyil edir.
$$\text{Cost Function: } f(n) = g(n) + h(n)$$
* $h(n)$ — $n$ düyünündən hədəf nöqtəsinə qədər olan Evklid məsafəsi:
$$h(n) = \sqrt{(x_{\text{goal}} - x_n)^2 + (y_{\text{goal}} - y_n)^2}$$

### Müqayisə Cədvəli

| Parametr | Dijkstra Alqoritmi | $A^*$ (A-Star) Alqoritmi |
| :--- | :--- | :--- |
| **Axtarış Tipi** | Kor / Bərabər paylanan (Uniform-cost) | Məlumatlı / Yönləndirilmiş (Informed / Heuristic) |
| **Ziyarət Edilən Yol Sayı** | Çox yüksək (bütün qonşuları araşdırır) | Minimum (yalnız hədəf sektorundakı yollar) |
| **Yaddaş İstifadəsi** | Prioritet növbəsində daha çox düyün saxlayır | Çox daha az düyün saxlayır |
| **Zaman Mürəkkəbliyi** | $\mathcal{O}(E + V \log V)$ | Evristikaya bağlı olaraq orta halda xeyli sürətli |
| **Optimal Nəticə?** | Bəli, zəmanətli ən qısa yol | Bəli ($h(n)$ heç vaxt real xərci aşmadığı halda) |

---

## 💡 Tez-tez Verilən Suallar və Sazlama (Troubleshooting)

<details>
<summary><b>1. "Geometry is invalid" və ya xəritə yüklənərkən xəta çıxarsa nə etməli?</b></summary>
Çox böyük ərazilər daxil etdikdə (məsələn, bütöv bir ölkə adı) OpenStreetMap serverləri sorğunu rədd edə bilər. Şəhərin konkret rayon və ya məhəllə adını qeyd etməyiniz tövsiyə olunur (məsələn, <code>Azerbaijan</code> əvəzinə <code>Sabayil, Baku, Azerbaijan</code>).
</details>

<details>
<summary><b>2. Animasiyanın sürətini necə dəyişə bilərəm?</b></summary>
Kod daxilindəki <code>step = 25</code> dəyişənini artıraraq (məsələn, <code>50</code>) animasiyanı daha sürətli, azaldaraq (məsələn, <code>10</code>) daha asta və detallı izləyə bilərsiniz.
</details>

---

## 🤝 Töhfə (Contributing)

Layihəni təkmilləşdirmək istəyirsinizsə:
1. Bu repozitoriyanı **Fork** edin
2. Yeni budaq yaradın (`git checkout -b feature/YeniXusiyyet`)
3. Dəyişikliklərinizi commit edin (`git commit -m 'Yeni xüsusiyyət əlavə edildi'`)
4. Budağınıza push edin (`git push origin feature/YeniXusiyyet`)
5. Bir **Pull Request** açın

---

## 👤 Müəllif və Əlaqə

- **GitHub:** [@Ferid18](https://github.com/Ferid18)
- Layihə ilə bağlı sualınız və ya təklifiniz varsa, [Issues](https://github.com/Ferid18/dijkstra-vs-astar/issues) bölməsində yaza bilərsiniz.

---

<div align="center">
    Layihəni bəyəndinizsə ulduz verməyi unutmayın! ⭐<br>
    Copyright © 2026 Ferid18. Bütün hüquqlar qorunur.
</div>
