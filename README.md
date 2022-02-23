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
<img width="197" alt="gui" src="https://user-images.githubusercontent.com/77780238/155394963-cfe0232e-ad15-48f5-858f-a454a8985249.png">
# Gesty kontrolujące windows'a:
### Przesuwa slide w prawo :
<img width="322" alt="slide_right" src="https://user-images.githubusercontent.com/77780238/155394996-53c5cbd5-0eb9-41c9-95c5-38a390cbf454.png">
### Przesuwa slide w lewo : 
<img width="319" alt="slide_left" src="https://user-images.githubusercontent.com/77780238/155395081-b4fe158c-e5aa-4f82-a54d-355306d829e7.png">
### Scroll'uje do góry :
![up](https://user-images.githubusercontent.com/77780238/155395383-7ec2305e-6d90-4847-b94c-405b85333dfe.png)
### Scroll'uje w dół
<img width="319" alt="down" src="https://user-images.githubusercontent.com/77780238/155395128-5c94575c-031f-4612-aade-125ea57cfb36.png">
### Robi screenshot'a
![screenshot](https://user-images.githubusercontent.com/77780238/155395142-55f35df1-fac3-44af-8dd9-9f2acccb4162.png)
### Włącza Whatsapp'a
![turn_on_whatsapp](https://user-images.githubusercontent.com/77780238/155395158-355cfcc1-c624-4550-ae4a-d874bf85463d.png)
### Zatrzymuje Video
<img width="313" alt="stop" src="https://user-images.githubusercontent.com/77780238/155395221-c8828608-15e0-4914-8df0-63e0996bedda.png">
### Zatrzymuje działanie programu
<img width="319" alt="close" src="https://user-images.githubusercontent.com/77780238/155395204-1a2003ff-4c0e-4749-aea1-352a0614312c.png">

## Wzorce
https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/
