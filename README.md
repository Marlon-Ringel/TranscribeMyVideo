#TranscribeMyVideo
TranscribeMyVideo ist eine Webanwendung zur Unterstützung der Transkription von Videodateien. TranscribeMyVideo erlaubt es Nutzern, eine Videodatei hochzuladen, für die automatisch ein Transkript erstellt wird. Anschließend hat der Nutzer die Möglichkeit, dieses zu korrigieren und es als PDF-Datei herunterzuladen.

##Voraussetzungen
Um TranscribeMyVideo lokal ausführen zu können, müssen folgende Voraussetzungen erfüllt sein:

Linux basiertes Betriebssystem (Getestet unter Ubuntu 22.04.5 LTS) https://wiki.ubuntu.com/Releases
Python Interpreter (Getestet mit Python Version 3.10.12)
https://www.python.org/
ffmpeg Version 4.4.2
https://www.ffmpeg.org/download.html
apt install ffmpeg 

Weiter werden folgende python libraries benötigt: 

Flask: https://flask.palletsprojects.com/en/3.0.x/
pip install Flask

Bootstrap-Flask: https://bootstrap-flask.readthedocs.io/en/stable/
pip install bootstrap-flask

Filetype: https://pypi.org/project/filetype/
pip install filetype

Moviepy: https://pypi.org/project/moviepy/
pip install moviepy

Openai Whisper: https://github.com/openai/whisper
pip install -U openai-whisper

PyFPDF: https://pyfpdf.readthedocs.io/en/latest/
pip install fpdf

##Ausführen der Anwendung
Sind diese Voraussetzungen erfüllt, kann TranscribeMyVideo wie folgt ausgeführt werden:

“python3 <Pfad zum Anwendungsverzeichnis>main.py”

Anschließend sollte TranscribeMyVideo über einen beliebigen Webbrowser unter „http://127.0.0.1:5000/“ verfügbar sein. Genaue Anweisungen zur Bedienung der Anwendung werden dem Nutzer während der Ausführung der Anwendung bereitgestellt.
