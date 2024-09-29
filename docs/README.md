---
title: "README"
author: "Jan Unger"
date: "2024-09-29"
---

# Projektorientierte Spieleentwicklung mit Python (MINT)

bearbeitet am 29. September 2024

- [Projektorientierte Spieleentwicklung mit Python (MINT)](#projektorientierte-spieleentwicklung-mit-python-mint)
  - [Übersicht](#übersicht)
  - [Struktur](#struktur)
  - [Nutzung - Git und Conda](#nutzung---git-und-conda)
    - [Conda-Umgebung erstellen, aktualisieren und aktivieren](#conda-umgebung-erstellen-aktualisieren-und-aktivieren)
  - [Lizenz](#lizenz)
  - [Installation](#installation)
    - [Erstellen und Klonen des Repositories](#erstellen-und-klonen-des-repositories)
    - [Erstellen der Conda-Umgebung](#erstellen-der-conda-umgebung)
    - [Aktivieren der Umgebung](#aktivieren-der-umgebung)
    - [Installation von Pygame mit AVX2-Unterstützung](#installation-von-pygame-mit-avx2-unterstützung)
  - [Nutzung von GitHub Features](#nutzung-von-github-features)
    - [Integration von CI/CD mit GitHub Actions](#integration-von-cicd-mit-github-actions)
    - [Vorteile von CI/CD](#vorteile-von-cicd)
    - [Erläuterung der Workflow-Schritte](#erläuterung-der-workflow-schritte)


## Übersicht

Dieses Projekt zielt darauf ab, das Erlernen und Anwenden von Python-Programmierung durch die Entwicklung von Spielen zu fördern. Der Fokus liegt auf projektorientiertem Lernen in den MINT-Fächern (Mathematik, Informatik, Naturwissenschaften, Technik).

## Struktur

- **docs/**: Dokumentationen wie Benutzerhandbuch, Entwicklerdokumentation, Struktogramme, MindMaps und Lizenzinformationen.
- **src/**: Quellcode der Spiele, unterteilt nach Schwierigkeitsgraden (Anfänger, Fortgeschrittene, Profi).
- **assets/**: Gemeinsame Ressourcen wie Bilder, Sounds, Modelle und Texturen.
- **tests/**: Unit-Tests, organisiert nach Schwierigkeitsgraden.
- **scripts/**: Hilfsskripte zur Automatisierung von Aufgaben.
- **README.md**: Hauptdokumentation des Projekts.
- **LICENSE**: Lizenzinformationen (MIT-Lizenz).
- **requirements.txt**: Python-Abhängigkeiten.

## Nutzung - Git und Conda

1. **Einrichten der Entwicklungsumgebung**
   ```
   cd Spieleentwicklung_Python
   ./scripts/setup_environment.sh
   ```

2. **Projekt entwickeln**
   Navigieren Sie zu einem der Projekte im `src/` Verzeichnis und beginnen Sie mit der Entwicklung.

3. **Versionierung mit Git**
   - Initialisieren des Git-Repositories:
     ```
     git init
     git add .
     git commit -m "Initial commit"
     # Voraussetzung: GitHub
     git push -u origin main
     ```


### Conda-Umgebung erstellen, aktualisieren und aktivieren

```bash
# Umgebung erstellen oder aktualisieren
conda env create -f environment.yml # das erste mal
conda env update --file environment.yml --prune

# Umgebung aktivieren
conda activate meinenv

# Conda-Kanäle konfigurieren
conda config --add channels conda-forge
conda config --set channel_priority strict
conda update --all

# Pygame überprüfen und testen
# pip install pygame  
pip show pygame
conda list pytorch

# Jupyter Lab starten oder Python-Skript ausführen
jupyter lab
python3 ./script.py

# Dokumentation konvertieren
make
make clean

# Umgebung deaktivieren
conda deactivate
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der [LICENSE](LICENSE) Datei.

## Installation

### Erstellen und Klonen des Repositories

Führen Sie die folgenden Schritte aus, um das Git-Repository zu initialisieren und mit GitHub zu verbinden:

```bash
# Git-Konfiguration überprüfen
git config --list

# README.md erstellen und initialen Commit durchführen
echo "# Spieleentwicklung mit Python" >> README.md
git init
git add README.md
git commit -m "Initialer Commit"

# GitHub-Repository verbinden und pushen
git branch -M main
git remote add origin git@github.com:ju1-eu/spieleentwicklung-mit-python.git
git push -u origin main

# Tagging der Version 1.0
git tag -a v1.0 -m "Version 1.0: Initiale Veröffentlichung"
git push origin v1.0

# Nutzung von Git und GitHub für Zusammenarbeit

## a) Branching-Strategie

# Neuen Feature-Branch erstellen und pushen
git checkout -b feature/neues-feature
git add .
git commit -m "Beschreibung des Features"
git push -u origin feature/neues-feature

# Pull Request auf GitHub erstellen:
# 1. Gehe zu deinem Repository auf GitHub.
# 2. Klicke auf "Compare & pull request" für den neuen Branch.
# 3. Füge eine Beschreibung hinzu und klicke auf "Create pull request".
```

### Erstellen der Conda-Umgebung

Richten Sie eine Conda-Umgebung ein, um die benötigten Abhängigkeiten zu verwalten:

```bash
# Conda aktualisieren
conda update -n base -c defaults conda
conda update --all
conda init zsh
source ~/.zshrc
conda --version

# Aufräumen
conda clean --all

# Umgebung aktualisieren oder erstellen
conda env update -f environment.yml
# Um eine Umgebung zu entfernen:
# conda env remove -n meinenv
# Um eine Umgebung neu zu erstellen:
# conda env create -f environment.yml

# Installation von Jupyter Notebook Erweiterungen
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Konvertieren von Jupyter Notebooks in *.py
jupyter nbconvert --to python src/test_installation.ipynb 
jupyter nbconvert --to markdown src/test_installation.ipynb 
jupyter nbconvert --to html src/test_installation.ipynb 
jupyter nbconvert --to pdf src/test_installation.ipynb 
```

Jupyter Notebook als Python-Skript exportieren mittels Git Hook

```bash
# Git Hook
cd .git/hooks
vim pre-commit
   #!/bin/sh
   jupyter nbconvert --to script ../../src/test_installation.ipynb 
   git add ../../src/test_installation.ipynb 

chmod +x pre-commit
```

### Aktivieren der Umgebung

Aktivieren und verwalten Sie die Conda-Umgebung wie folgt:

```bash
# Liste der Umgebungen anzeigen
conda env list

# Umgebung aktivieren
conda activate meinenv

# Überprüfen des Python-Pfades und der Version
which python3
python3 --version
conda info
conda update --all

# Umgebung entfernen oder deaktivieren
# conda env remove -n meinenv
# conda deactivate
```

### Installation von Pygame mit AVX2-Unterstützung

Um Pygame mit AVX2-Unterstützung zu installieren, folgen Sie diesen Schritten:

1. **SDL-Entwicklerbibliotheken installieren:**

    ```bash
    brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf portmidi
    ```

2. **Umgebungsvariablen für SDL-Pfade setzen:**

    ```bash
    export LDFLAGS="-L/usr/local/opt/sdl2/lib"
    export CPPFLAGS="-I/usr/local/opt/sdl2/include"
    ```

3. **AVX2-Erkennung aktivieren:**

    ```bash
    export PYGAME_DETECT_AVX2=1
    ```

4. **Pygame neu installieren:**

    ```bash
    pip install --upgrade pip
    pip install --no-binary :all: pygame
    ```

## Nutzung von GitHub Features

- **Issues:** Für Bug-Tracking und Feature-Anfragen.
- **Pull Requests:** Für Code-Reviews und Zusammenarbeit.
- **Projects:** Für die Organisation von Aufgaben im Kanban-Stil.

### Integration von CI/CD mit GitHub Actions

Continuous Integration (CI) und Continuous Deployment (CD) sind essenzielle Praktiken in der modernen Softwareentwicklung. Sie ermöglichen es Teams, Code schneller und zuverlässiger zu entwickeln, zu testen und bereitzustellen. GitHub Actions bietet eine leistungsstarke und flexible Möglichkeit, CI/CD-Pipelines direkt in GitHub-Repositories zu implementieren.

### Vorteile von CI/CD

- **Frühzeitige Fehlererkennung**
- **Verbesserte Codequalität**
- **Schnellere Bereitstellung von Updates**
- **Erhöhte Entwicklerproduktivität**

Implementieren Sie CI/CD mit GitHub Actions, um automatische Tests und Deployments durchzuführen.

**Beispiel `.github/workflows/python-app.yml`:**

```yaml
name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: macos-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Conda
      uses: conda-incubator/setup-miniconda@v2
      with:
        environment-file: environment.yml
        activate-environment: meinenv
        python-version: 3.12
    - name: Install pip dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
```

### Erläuterung der Workflow-Schritte

1. **Trigger:** Der Workflow wird bei Pushes und Pull Requests auf den `main`-Branch ausgelöst.
2. **Runner:** Der Job läuft auf einem macOS-System.
3. **Checkout:** Der Repository-Code wird ausgecheckt.
4. **Conda Setup:** Conda wird mit einer spezifischen Umgebung und Python-Version eingerichtet.
5. **Dependency Installation:** Pip-Abhängigkeiten werden installiert.
6. **Tests:** Pytest wird ausgeführt, um die Tests durchzuführen.

**Anpassungsmöglichkeiten**

- **Für Node.js-Projekte:** Ersetzen Sie das Conda-Setup und pip durch Node.js-Setup und npm/yarn.
- **Für Deployment:** Fügen Sie einen Schritt hinzu, der den Code auf einen Server oder Cloud-Dienst deployed.

**Sicherheitshinweis**

Beim Einsatz von GitHub Actions ist es wichtig, sensible Daten wie API-Schlüssel oder Zugangsdaten als [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) zu speichern. Diese können dann sicher in Ihren Workflows verwendet werden, ohne sie im Code preiszugeben.

**Hinweis:** Stellen Sie sicher, dass Sie eine `requirements.txt`-Datei haben, wenn Sie zusätzliche `pip`-Pakete verwenden.

**Weitere Ressourcen**

- [GitHub Actions Dokumentation](https://docs.github.com/en/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
