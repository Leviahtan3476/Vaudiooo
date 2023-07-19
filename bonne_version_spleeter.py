
!apt install ffmpeg

!pip install spleeter

!git clone https://github.com/Deezer/spleeter
!conda env create -f spleeter/conda/spleeter-cpu.yaml
!conda activate spleeter-cpu

pip freeze

from IPython.display import Audio

from google.colab import files

uploaded = files.upload()

! rm -f song.mp3  # remove the song.mp3 if it exists
files.upload()
! echo "Moving song.mp3...."
! mv song.mp3 spleeter/audio_example.mp3

Audio('audio_example.mp3')

"""Les dernières versions de spleeter n'ont pas besoin du -i il faut donc l'enlever"""

!spleeter separate audio_example.mp3 -o output_2stem/

"""La commande ci dessous permet de transformer le .mp3 en .wav"""

!spleeter separate -o output/ audio_example.mp3

"""La commande ci dessous permet au .wav d'avoir une meilleure qualité audio"""

!ffmpeg -hide_banner -i output_2stem/audio_example/vocals.wav -vn -ar 44100 -ac 2 -b:a 256k output_2stem/audio_example/audio_example_vocals.mp3
!ffmpeg -hide_banner -i output_2stem/audio_example/accompaniment.wav -vn -ar 44100 -ac 2 -b:a 256k output_2stem/audio_example/audio_example_karaoke.mp3

!ls output/audio_example

import os

# Chemin d'accès au fichier
chemin_fichier = '/content/output_2stem/audio_example/accompaniment.wav'

# Nouveau nom de fichier
nouveau_nom = 'instrumental.wav'

# Renommer le fichier
os.rename(chemin_fichier, os.path.join(os.path.dirname(chemin_fichier), nouveau_nom))

import os

# Chemin d'accès au fichier
chemin_fichier = '/content/output/audio_example/accompaniment.wav'

# Nouveau nom de fichier
nouveau_nom = 'instrumental.wav'

# Renommer le fichier
os.rename(chemin_fichier, os.path.join(os.path.dirname(chemin_fichier), nouveau_nom))

Audio('output/audio_example/vocals.wav')

Audio('output/audio_example/instrumental.wav')

import zipfile
with zipfile.ZipFile('Stems.zip', 'w') as myzip:
    myzip.write('output/audio_example/instrumental.wav')
    myzip.write('output/audio_example/vocals.wav')

from google.colab import files

# Définir le nom du fichier à télécharger
nom_fichier = "Stems.zip"

# Télécharger le fichier
files.download(nom_fichier)

"""Code pour faire un stems de 5 pistes"""

!spleeter separate audio_example.mp3 -o output_5stems -p spleeter:5stems

!ls output_5stems/audio_example

!ffmpeg -hide_banner -i output_5stems/audio_example/vocals.wav -vn -ar 44100 -ac 2 -b:a 256k output_5stems/audio_example/audio_example_5s_vocals.mp3
!ffmpeg -hide_banner -i output_5stems/audio_example/drums.wav -vn -ar 44100 -ac 2 -b:a 256k output_5stems/audio_example/audio_example_5s_drums.mp3
...

!ls output_5stems/audio_example/*.mp3

"""Commande ci-dessous permet de créer un fichier ZIP des 5 stems .wav"""

import zipfile
with zipfile.ZipFile('Stems.zip', 'w') as myzip:
    myzip.write('output_5stems/audio_example/bass.wav')
    myzip.write('output_5stems/audio_example/drums.wav')
    myzip.write('output_5stems/audio_example/other.wav')
    myzip.write('output_5stems/audio_example/piano.wav')
    myzip.write('output_5stems/audio_example/vocals.wav')

from google.colab import files

# Définir le nom du fichier à télécharger
nom_fichier = "Stems.zip"

# Télécharger le fichier
files.download(nom_fichier)