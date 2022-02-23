# Projekt_na_6 by Krystian Wierciak
# Golden Teacher
### GoldenTeacher - rozwiązanie dla wielu nauczycieli, lektorów, prelegentów... 
czy chociażby wykładowców na uczelni którzy, prowadzą zajęcia dla większej publiki. Moje rozwiązanie jest w stanie im to
uprościć. Poprzez program GoldenTeacher wykładowcy są w stanie skupić pełną uwagę na uczniach, nie musząc co chwila
podchodzić do komputera, aby zmienić slajd , zrobić screenshot'a czy chociażby włączyć Whatsapp'a. 
## Od strony technicznej:
Posłużyłem się rozwiązaniem pewnego programisty, który wytrenował model za pomocą uczenia maszynowego, aby wykrywał i 
rozpoznawał różne gesty. Następnie, po wykorzystaniu odpowiednich bibliotek udało mi się przypisać tym gestom 
odpowiednie funkcjonalności. Później stworzyłem interfejs, aby każdy człowiek był w stanie wypróbować mój program. 
Starałem sie jak najlepiej ująć styl pisania tak jak jest w dokumentacji PEP 8.
* (https://www.python.org/dev/peps/pep-0008/)
# GUI
Gui jest świetne w swej prostocie , zawiera jedynie 3 przyciski z czego jedynie dwa ( close , On ) mogą realnie 
wpływać na działanie programu.Ten środkowy odwołuje się repozytorium na Github'ie aby łatwiej można  było rozpowszechniać
ten software.
# Graphic User Interface:
<img width="197" alt="gui" src="https://user-images.githubusercontent.com/77780238/155403110-1d2839be-2a13-4986-aa39-ce9f5c3d7b7f.png">

# Gesty :

### Przesuwa slide w Prawo :

<img width="322" alt="slide_right" src="https://user-images.githubusercontent.com/77780238/155403143-d146da13-4421-46fa-a2ee-4c6224318643.png">

### Przesuwa slide w Lewo :

<img width="319" alt="slide_left" src="https://user-images.githubusercontent.com/77780238/155403185-a5cbc4ca-d914-446e-b68d-881c852eeeeb.png">

### Scroll'uje do góry :

![upgesture](https://user-images.githubusercontent.com/77780238/155404258-cc0f7fb4-7789-4626-924b-85293b61fedb.png)


### Scroll'uje w dół

<img width="319" alt="down" src="https://user-images.githubusercontent.com/77780238/155403276-ffbce1aa-9710-41a4-b296-d4d944f8d90f.png">

### Robi screenshot'a

![screenshot](https://user-images.githubusercontent.com/77780238/155403755-3f7fe50e-8828-4fc3-8653-fa32f2ac40cf.png)

### Włącza Whatsapp'a

![turn_on_whatsapp](https://user-images.githubusercontent.com/77780238/155404355-dfc6c875-b1d5-4373-a5bd-523a9cf74686.png)


### Pauzuje Video

<img width="313" alt="stop" src="https://user-images.githubusercontent.com/77780238/155404400-2dcf0ae5-4471-41e4-925c-df27dfded689.png">


### Zatrzymuje działanie programu

<img width="319" alt="close" src="https://user-images.githubusercontent.com/77780238/155404419-f367ad8d-1575-4597-80b1-5efb1a2c4df6.png">


## Wzorce
https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/
