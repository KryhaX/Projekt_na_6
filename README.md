# Projekt_na_6 by Krystian Wierciak
# Golden Teacher
### GoldenTeacher, rozwiązanie dla wielu nauczycieli, lektorów, prelegentów... 
czy chociażby wykładowców na uczelni którzy prowadząc zajęcia dla większej publiki. Moje rozwiązanie jest w stanie im to
uprościć. Poprzez program GoldenTeacher wykładowcy są w stanie skupić pełną uwagę na uczniach , nie musząc co chwila
podchodzić do komputera aby zmienić slajd , zrobić screenshot'a , czy chociażby włączyć Whatsapp'a. 
## Od strony technicznej:
Posłużyłem się rozwiązaniem pewnego programisty który wytrenował model za pomocą uczenia maszynowego aby wykrywał i 
rozpoznawał różne gesty. Następnie po wykorzystaniu odpowiednich bibliotek udało mi się przypisać tym gestom 
odpowiednie funkcjonalności. Później stworzyłem interfejs aby każdy człowiek był w stanie wypróbować mój program. 
Starałem sie jak najlepiej ująć styl pisania tak jak jest w dokumentacji PEP 8.
* (https://www.python.org/dev/peps/pep-0008/)
# GUI
Gui jest świetne w swej prostocie , zawiera jedynie 3 przyciski z czego jedynie dwa ( close , On ) mogą realnie 
wpływać na działanie programu.Ten środkowy odwołuje się repozytorium na Github'ie aby łatwiej można  było rozpowszechniać
ten software.
# Graphic User Interface:
<img width="197" alt="gui" src="https://user-images.githubusercontent.com/77780238/155403110-1d2839be-2a13-4986-aa39-ce9f5c3d7b7f.png">
# Gesty kontrolujące windows'a:
### Przesuwa slide w Prawo :
<img width="322" alt="slide_right" src="https://user-images.githubusercontent.com/77780238/155403143-d146da13-4421-46fa-a2ee-4c6224318643.png">
### Przesuwa slide w Lewo :
<img width="319" alt="slide_left" src="https://user-images.githubusercontent.com/77780238/155403185-a5cbc4ca-d914-446e-b68d-881c852eeeeb.png">
### Scroll'uje do góry :

### Scroll'uje w dół
<img width="319" alt="down" src="https://user-images.githubusercontent.com/77780238/155403276-ffbce1aa-9710-41a4-b296-d4d944f8d90f.png">
### Robi screenshot'a

### Włącza Whatsapp'a
<img src="../../../Desktop/opis_gestow/turn_on_whatsapp.png"/>

### Zatrzymuje Video
<img src="../../../Desktop/opis_gestow/stop.png"/>

### Zatrzymuje działanie programu
<img src="../../../Desktop/opis_gestow/close.png"/>

## Wzorce
https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/
