
Messages redis
=====================

Demande 1 prise de vue déclanchée par un bouton joystick :
pub sc:take_photo 1

Demande 5 prises de vue en rafale déclanchée par un autre bouton joystick :
pub sc:take_photo 5

Quand une photo est téléchargée de l'appareil photo :
pub sc:photo_taken images/DSC234774.jpeg

Quand 5 photos sont prises en rafale  :
pub sc:photo_taken images/DSC234775.jpeg
pub sc:photo_taken images/DSC234776.jpeg
pub sc:photo_taken images/DSC234777.jpeg
pub sc:photo_taken images/DSC234778.jpeg
pub sc:photo_taken images/DSC234779.jpeg




