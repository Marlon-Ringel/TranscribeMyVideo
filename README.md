# TranscribeMyVideo

TranscribeMyVideo ist eine Webanwendung zur Unterstützung der Transkription von Videodateien. 
TranscribeMyVideo erlaubt es Nutzern, eine Videodatei hochzuladen, für die automatisch ein Transkript erstellt wird. 
Anschließend hat der Nutzer die Möglichkeit, dieses zu korrigieren und es als PDF-Datei herunterzuladen.

## Voraussetzungen
Um TranscribeMyVideo (lokal) ausführen zu können, müssen folgende Voraussetzungen erfüllt sein:

Linux basiertes Betriebssystem (Getestet unter [Ubuntu](https://wiki.ubuntu.com/Releases) 22.04.5 LTS)

[Python](https://www.python.org/) Interpreter (Getestet mit Python Version 3.10.12)

[ffmpeg](https://www.ffmpeg.org/download.html) Version 4.4.2
<br/>Unter Ubuntu 22.04.5 LTS installierbar mit: 
```bash
apt install ffmpeg 
```

### Python Libraries
Weiter werden folgende Python Libraries benötigt: 

#### [Flask](https://flask.palletsprojects.com/en/3.0.x/) 
```bash
pip install Flask
```
#### [Bootstrap-Flask](https://bootstrap-flask.readthedocs.io/en/stable/)
```bash
pip install bootstrap-flask
```
#### [Filetype](https://pypi.org/project/filetype/)
```bash
pip install filetype
```
#### [Moviepy](https://pypi.org/project/moviepy/)
```bash
pip install moviepy
```
#### [Openai Whisper](https://github.com/openai/whisper) 
```bash
pip install -U openai-whisper
```
#### [PyFPDF](https://pyfpdf.readthedocs.io/en/latest/)
```bash
pip install fpdf
```
## Ausführen der Anwendung
Sind alle Voraussetzungen erfüllt, kann TranscribeMyVideo wie folgt über das Terminal ausgeführt werden:
```bash
“python3 <Pfad zum Anwendungsverzeichnis>main.py”
```
Anschließend ist TranscribeMyVideo über einen beliebigen Webbrowser unter „127.0.0.1:5000/“ verfügbar. 
Genaue Anweisungen zur Bedienung der Anwendung werden dem Nutzer während der Ausführung der Anwendung bereitgestellt.

## Anpassen des verwendeten KI-Modells 
TranscribeMyVideo verwendet das Sprache-zu-Text-System, Whisper für die Transkription der Videodatei. 
Dabei wird aus Performancegründen das Whisper „base“ Modell verwendet. Dies kann in der Datei „transcriptionService.py“ angepasst werden. 
