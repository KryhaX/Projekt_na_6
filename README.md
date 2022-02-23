# Projekt_na_6 by Krystian Wierciak
# Golden Teacher
### GoldenTeacher, rozwiązanie dla wielu nauczycieli, lektorów, prelegentów... 
czy chociażby wykładowców na uczelni którzy prowadząc zajęcia dla większej publiki. Moje rozwiązanie jest w stanie im to
uprościć. Poprzez program GoldenTeacher wykładowcy są w stanie skupić pełną uwagę na uczniach , nie musząc co chwila
podchodzić do komputera aby zmienić slajd , zrobić screenshot'a , czy chociażby włączyć Whatsapp'a. 
##Od strony technicznej:
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
![](../../../Desktop/opis_gestow/gui.png)
#Gesty kontrolujące windows'a:
###Przesuwa slide w prawo :
![](../../../Desktop/opis_gestow/slide_right.png)
### Przesuwa slide w lewo : 
![](../../../Desktop/opis_gestow/slide_left.png)
###Scroll'uje do góry :
![](../../../Desktop/opis_gestow/up.png)
### Scroll'uje w dół
![](../../../Desktop/opis_gestow/down.png)
### Robi screenshot'a
![](../../../Desktop/opis_gestow/screenshot.png)
### Włącza Whatsapp'a
![](../../../Desktop/opis_gestow/turn_on_whatsapp.png)
### Zatrzymuje Video
![](../../../Desktop/opis_gestow/stop.png)
### Zatrzymuje działanie programu
![](../../../Desktop/opis_gestow/close.png)
## Wzorce
https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/