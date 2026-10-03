# Xəritədə Dijkstra və A* Vizualizatoru

Bu Python layihəsi OpenStreetMap-dən real avtomobil yollarını yükləyir və həmin şəbəkədə iki ən qısa yol alqoritmini yan-yana müqayisə edir:

- **Dijkstra** — hədəfin yerini nəzərə almadan ən aşağı məsafəli yolları ardıcıl araşdırır.
- **A\*** — faktiki yol məsafəsinə əlavə olaraq hədəfə olan düzxətli məsafəni istifadə edir və çox vaxt daha az düyün araşdırır.

Nəticə qaranlıq temalı, animasiyalı pəncərədə göstərilir. Hər paneldə alqoritmin araşdırdığı yollar və sonda tapdığı optimal marşrut görünür.

## Xüsusiyyətlər

- İstənilən OpenStreetMap regionu üçün yol şəbəkəsinin yüklənməsi
- Yalnız tam əlaqəli yol komponentinin istifadə olunması
- Dijkstra və A* üçün düzgün prioritet növbəsi (heap) məntiqi
- Paralel yol hissələri olduqda ən qısa hissənin seçilməsi
- Başlanğıc və hədəf üçün uzaq, müqayisə etməyə uyğun nöqtələrin avtomatik seçilməsi
- Araşdırılan düyün sayı və ümumi marşrut məsafəsinin konsolda göstərilməsi
- Performanslı `LineCollection` əsaslı animasiya

## Tələblər

- Python 3.9 və ya daha yeni versiya
- İnternet bağlantısı — OpenStreetMap məlumatını yükləmək üçün

Paketləri quraşdırın:

```bash
pip install -r requirements.txt
```

## İşə salma

```bash
python main.py
```

Proqram region adı soruşacaq. Məsələn:

```text
Baku, Azerbaijan
```

Digər nümunələr:

- `Sabayil, Baku, Azerbaijan`
- `Kadikoy, Istanbul, Turkey`
- `Manhattan, New York, USA`
- `Mitte, Berlin, Germany`

Boş Enter düyməsi sıxıldıqda standart olaraq `Mitte, Berlin, Germany` istifadə edilir.

## Nəticənin oxunuşu

| Element | Mənası |
| --- | --- |
| Yaşıl nöqtə | Başlanğıc nöqtəsi |
| Çəhrayı nöqtə | Hədəf nöqtəsi |
| Sarı/mavi xətlər | Müvafiq alqoritmin axtarış zamanı araşdırdığı yollar |
| Parlaq yaşıl xətt | Tapılmış optimal marşrut |

Soldakı panel Dijkstra, sağdakı panel isə A* nəticəsini göstərir. Panel başlığında hər alqoritmin araşdırdığı düyün sayı yazılır. Konsolda isə marşrut məsafəsi kilometrlə görünür.

## Layihə strukturu

```text
xerite/
├── main.py          # Alqoritmlər, xəritə yükləmə və animasiya
├── requirements.txt # Python asılılıqları
├── .gitignore       # Keş və kompilyasiya faylları üçün istisnalar
└── README.md        # Layihə sənədi
```

## Qeyd

Böyük şəhər və ya ölkə adı daxil etmək xəritənin yüklənməsini və animasiyanı yavaşıda bilər. Daha rahat istifadə üçün şəhər, rayon və ya məhəllə səviyyəsində region seçin.
