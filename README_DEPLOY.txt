REGISTAR — PAKET ZA OBJAVU

Folder je spreman za GitHub Pages ili bilo koji statični hosting.

STRUKTURA FOLDERA

registar/
  index.html
  style.css
  REGISTAR_LEDGER.csv
  entries/
    001.html
    TEMPLATE_TEXT.html
    TEMPLATE_IMAGE.html
    TEMPLATE_AUDIO.html
    TEMPLATE_VIDEO.html
    TEMPLATE_MIXED.html
  media/
    README_MEDIA.txt
  tools/
    close_entry.py
    verify_ledger.py

PRAVILO STATUSA

Upis i događaj nisu isto.

STATUS ZAPISA: ZATVOREN
STATUS DOGAĐAJA: NERAZREŠEN

To znači: HTML fajl može biti zaključen, ali događaj ne mora biti objašnjen.

HASH FAJLA

Vidljivo polje HASH FAJLA potvrđuje verziju fajla, ne poreklo događaja.
Polje HASH FAJLA je isključeno iz sopstvenog hash-a normalizacijom.
Pun hash se čuva u REGISTAR_LEDGER.csv.

BRZO DODAVANJE UNOSA

1. Dupliraj template iz entries/.
   Primer:
   cp entries/TEMPLATE_IMAGE.html entries/004.html

2. Zameni sva 000 polja novim brojem, npr. 004.
   Zameni GGGG-MM-DD, FORMAT, TIP, SERIJU i tekst.

3. Medijske fajlove stavi u /media.
   Primer:
   media/004.jpg

4. Dodaj red u index.html.
   Najnoviji unos ide na vrh <tbody> bloka.

5. Zatvori unos:
   python3 tools/close_entry.py 004

6. Proveri knjigu upisa:
   python3 tools/verify_ledger.py

7. Commit u git:
   git add .
   git commit -m "zatvoren unos 004"
   git push

TEMPLATE REDOVI ZA INDEX

TEKST:
<tr>
  <td><a href="entries/000.html">000</a></td>
  <td>GGGG&#8209;MM&#8209;DD</td>
  <td>TEKST</td>
  <td>KARTICA OPAŽAJA</td>
  <td class="note">KRATKA NAPOMENA</td>
</tr>

SLIKA:
<tr>
  <td><a href="entries/000.html">000</a></td>
  <td>GGGG&#8209;MM&#8209;DD</td>
  <td>SLIKA</td>
  <td>VIZUELNI TRAG</td>
  <td class="note">KRATKA NAPOMENA</td>
</tr>

ZVUK:
<tr>
  <td><a href="entries/000.html">000</a></td>
  <td>GGGG&#8209;MM&#8209;DD</td>
  <td>ZVUK</td>
  <td>ZVUČNI TRAG</td>
  <td class="note">KRATKA NAPOMENA</td>
</tr>

VIDEO:
<tr>
  <td><a href="entries/000.html">000</a></td>
  <td>GGGG&#8209;MM&#8209;DD</td>
  <td>VIDEO</td>
  <td>POKRETNI TRAG</td>
  <td class="note">KRATKA NAPOMENA</td>
</tr>

PRAVILA ZA MEDIJE

Slike: jpg, png, webp.
Zvuk: mp3.
Video: mp4.
Bez razmaka u imenima fajlova.

Preporučeno imenovanje:
004.jpg
005.mp3
006.mp4
007-a.jpg
007-b.mp3

OBJAVA NA GITHUB PAGES

1. Napravi novi GitHub repository.
2. Uploaduj SADRŽAJ ovog foldera, ne spoljašnji zip.
3. index.html mora ostati u root-u repository-ja.
4. Settings > Pages > Deploy from branch > main / root.
5. Otvori Pages URL.

NE RADITI

Ne dodavati thumbnails u index.html.
Ne koristiti plave linkove.
Ne objašnjavati rad na index strani.
Ne menjati zatvorene unose usputno.
Ako zatvoren unos mora da se promeni, napravi novi unos umesto ispravke starog.
