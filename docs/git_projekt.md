---
title: "git_projekt"
author: "Jan Unger"
date: "2024-09-28"
---

# Git

bearbeitet am 28. September 2024

- [Git](#git)
  - [**1. Git-Konfigurationsbefehle verstehen**](#1-git-konfigurationsbefehle-verstehen)
  - [**2. Umsetzung der Git-Konfiguration**](#2-umsetzung-der-git-konfiguration)
    - [**d. Überprüfe die Git-Konfiguration**](#d-überprüfe-die-git-konfiguration)
  - [**3. SSH-Schlüssel für GitHub einrichten (Empfohlen)**](#3-ssh-schlüssel-für-github-einrichten-empfohlen)
    - [**a. Überprüfe, ob bereits ein SSH-Schlüssel existiert**](#a-überprüfe-ob-bereits-ein-ssh-schlüssel-existiert)
    - [**b. Generiere einen neuen SSH-Schlüssel**](#b-generiere-einen-neuen-ssh-schlüssel)
    - [**c. Füge den SSH-Schlüssel zum SSH-Agent hinzu**](#c-füge-den-ssh-schlüssel-zum-ssh-agent-hinzu)
    - [**d. Füge den öffentlichen SSH-Schlüssel zu GitHub hinzu**](#d-füge-den-öffentlichen-ssh-schlüssel-zu-github-hinzu)
  - [**4. GitHub-Repository erstellen und verbinden**](#4-github-repository-erstellen-und-verbinden)
    - [**a. GitHub-Repository erstellen**](#a-github-repository-erstellen)
    - [**b. Lokales Git-Repository initialisieren und verbinden**](#b-lokales-git-repository-initialisieren-und-verbinden)
  - [**5. Jupyter Notebook als Python-Skript exportieren**](#5-jupyter-notebook-als-python-skript-exportieren)
    - [**Automatisches Exportieren bei jedem Commit (Optional)**](#automatisches-exportieren-bei-jedem-commit-optional)
  - [**6. Weitere nützliche Git-Befehle und Best Practices**](#6-weitere-nützliche-git-befehle-und-best-practices)
    - [**a. Git-Aliase nutzen**](#a-git-aliase-nutzen)
    - [**b. Branching und Pull Requests**](#b-branching-und-pull-requests)
    - [**c. Globale `.gitignore` erweitern**](#c-globale-gitignore-erweitern)
    - [**d. Farben und Lesbarkeit optimieren**](#d-farben-und-lesbarkeit-optimieren)
    - [**e. Commit-Nachrichten formatieren**](#e-commit-nachrichten-formatieren)

## **1. Git-Konfigurationsbefehle verstehen**

Eine kurze Übersicht der wichtigsten Einstellungen:

- **Benutzeridentifikation**: Setzt deinen Namen und deine E-Mail-Adresse, die bei jedem Commit verwendet werden.
- **Standard-Branch**: Setzt den Standard-Branch-Namen auf `main` statt `master`.
- **Globale `.gitignore`**: Legt eine globale `.gitignore`-Datei fest, die bestimmte Dateien und Verzeichnisse in allen Repositories ignoriert.
- **Git-Aliase**: Erstellt Kurzbefehle für häufig verwendete Git-Befehle.
- **Farben aktivieren**: Verbessert die Lesbarkeit der Git-Ausgabe durch Farbgebung.
- **Standard-Editor**: Setzt den Standard-Editor für Git-Commits (z.B. Visual Studio Code).
- **Pull-Strategie**: Ändert die Pull-Strategie auf `rebase`, um eine sauberere Commit-Historie zu ermöglichen.
- **Automatisches Entfernen von gemergten Branches**: Entfernt lokale Branches, die bereits gemergt wurden.
- **Whitespace-Änderungen anzeigen**: Hebt Änderungen in Leerzeichen hervor.

## **2. Umsetzung der Git-Konfiguration**

1. **Erstelle eine neue Datei namens `git_setup.sh`:**

   ```bash
   vim git_setup.sh
   ```

2. **Füge die Git-Konfigurationsbefehle in die Datei ein:**

   ```bash
   #!/bin/bash

   # Benutzeridentifikation
   git config --global user.name "Jan Unger"
   git config --global user.email "esel573@gmail.com"

   # Standard-Branch auf 'main' setzen
   git config --global init.defaultBranch main

   # Globale .gitignore festlegen
   touch ~/.gitignore_global
   echo -e "# macOS\n.DS_Store\n\n# Python\n__pycache__/\n*.py[cod]\n*.pyo\n*.pyd\n*.env\n.env\n*.egg\n*.egg-info/\ndist/\nbuild/" > ~/.gitignore_global
   git config --global core.excludesfile ~/.gitignore_global

   # Git-Aliase einrichten
   git config --global alias.st status
   git config --global alias.co checkout
   git config --global alias.br branch
   git config --global alias.ci commit
   git config --global alias.lg "log --oneline --graph --decorate --all"

   # Farben aktivieren
   git config --global color.ui auto

   # Standard-Editor festlegen (Beispiel: VS Code: code --wait)
   git config --global core.editor "vim"

   # Pull-Strategie auf Rebase setzen
   git config --global pull.rebase true

   # Automatisches Entfernen von gemergten Branches
   git config --global fetch.prune true

   # Whitespace-Änderungen anzeigen
   git config --global core.whitespace trailing-space,space-before-tab
   ```

3. **Speichere die Datei und mache das Skript ausführbar:**

   - **Mache das Skript ausführbar:**

     ```bash
     chmod +x git_setup.sh
     ./git_setup.sh
     ```

### **d. Überprüfe die Git-Konfiguration**

```bash
git config --list
```

## **3. SSH-Schlüssel für GitHub einrichten (Empfohlen)**

Um die Sicherheit und Benutzerfreundlichkeit zu erhöhen, ist es empfehlenswert, SSH-Schlüssel für die Authentifizierung mit GitHub zu verwenden.

### **a. Überprüfe, ob bereits ein SSH-Schlüssel existiert**

```bash
ls -al ~/.ssh
```

Suche nach Dateien wie `id_rsa.pub` oder `id_ed25519.pub`. Wenn keine SSH-Schlüssel vorhanden sind, erstelle einen neuen.

### **b. Generiere einen neuen SSH-Schlüssel**

1. **Erstelle einen neuen SSH-Schlüssel mit deiner GitHub-E-Mail-Adresse:**

   ```bash
   ssh-keygen -t ed25519 -C "esel573@gmail.com"
   ```

   **Hinweis:** Wenn dein System keine Unterstützung für Ed25519 bietet, verwende RSA:

   ```bash
   ssh-keygen -t rsa -b 4096 -C "esel573@gmail.com"
   ```

2. **Folge den Anweisungen im Terminal:**
   - Drücke `Enter`, um den Schlüssel im Standardverzeichnis zu speichern (`~/.ssh/id_ed25519`).
   - Optional: Lege ein sicheres Passwort fest oder drücke einfach `Enter`, um kein Passwort zu verwenden.

### **c. Füge den SSH-Schlüssel zum SSH-Agent hinzu**

1. **Starte den SSH-Agenten im Hintergrund:**

   ```bash
   eval "$(ssh-agent -s)"
   ```

2. **Füge deinen SSH-Schlüssel zum Agenten hinzu:**

   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

   **Hinweis:** Passe den Pfad an, falls du RSA verwendet hast (`~/.ssh/id_rsa`).

### **d. Füge den öffentlichen SSH-Schlüssel zu GitHub hinzu**

1. **Kopiere den Inhalt deines öffentlichen SSH-Schlüssels in die Zwischenablage:**

   ```bash
   pbcopy < ~/.ssh/id_ed25519.pub
   ```

   **Hinweis:** Falls du RSA verwendet hast, ersetze `id_ed25519.pub` durch `id_rsa.pub`.

2. **Gehe zu GitHub:**
   - Melde dich bei [GitHub](https://github.com/) an.
   - Navigiere zu **Settings** > **SSH and GPG keys**.
   - Klicke auf **"New SSH key"**.
   - Füge den kopierten Schlüssel in das Feld **"Key"** ein und gib ihm einen aussagekräftigen Titel.
   - Klicke auf **"Add SSH key"**.

3. **Überprüfe die SSH-Verbindung zu GitHub:**

   ```bash
   ssh -T git@github.com
   ```

   **Erwartete Ausgabe:**

   ```
   Hi JanUnger! You've successfully authenticated, but GitHub does not provide shell access.
   ```

## **4. GitHub-Repository erstellen und verbinden**

Falls du dies noch nicht getan hast, erstelle ein Repository auf GitHub und verbinde es mit deinem lokalen Projekt.

### **a. GitHub-Repository erstellen**

1. **Gehe zu [GitHub](https://github.com/) und melde dich an.**
2. **Klicke auf das Plus-Symbol (`+`) oben rechts und wähle "New repository".**
3. **Fülle die erforderlichen Informationen aus:**
   - **Repository-Name:** `mechanik` (oder ein anderer Name deiner Wahl).
   - **Beschreibung:** Optional, z.B. "Simulation der Rollreibung".
   - **Sichtbarkeit:** Wähle zwischen "Public" oder "Private".
   - **README hinzufügen:** Aktiviere **"Initialize this repository with a README"**.
4. **Klicke auf "Create repository".**

### **b. Lokales Git-Repository initialisieren und verbinden**

1. **Navigiere zu deinem Projektordner im Terminal:**

   ```bash
   echo "# mechanik" >> README.md
   git init
   git add README.md
   git commit -m "first commit"
   git branch -M main
   git remote add origin git@github.com:ju1-eu/mechanik.git
   git push -u origin main
   ```

## **5. Jupyter Notebook als Python-Skript exportieren**

Um dein Jupyter Notebook (`mein_notebook.ipynb`) als Python-Skript zu exportieren, verwende den folgenden Befehl:

```bash
jupyter nbconvert --to script mein_notebook.ipynb
```

Dies erstellt eine Datei namens `mein_notebook.py` im selben Verzeichnis.

### **Automatisches Exportieren bei jedem Commit (Optional)**

Um sicherzustellen, dass dein Python-Skript immer auf dem neuesten Stand ist, kannst du einen Git Hook einrichten, der das Notebook automatisch bei jedem Commit exportiert.

1. **Navigiere zum Git-Hooks-Verzeichnis:**

   ```bash
   cd .git/hooks
   ```

2. **Erstelle einen `pre-commit` Hook:**

   ```bash
   vim pre-commit
   ```

3. **Füge folgendes Skript hinzu:**

   ```bash
   #!/bin/sh
   jupyter nbconvert --to script ../mein_notebook.ipynb
   git add ../mein_notebook.py
   ```

   **Hinweis:** Passe den Pfad zu deinem Notebook entsprechend an.

4. **Speichere die Datei und mache den Hook ausführbar:**

   - **Speichern und Beenden in `vim`:** Drücke `Ctrl + O`, dann `Enter`, und dann `Ctrl + X`.
   - **Mache den Hook ausführbar:**

     ```bash
     chmod +x pre-commit
     ```

Jetzt wird bei jedem Commit dein Notebook automatisch als Python-Skript exportiert und hinzugefügt.

## **6. Weitere nützliche Git-Befehle und Best Practices**

### **a. Git-Aliase nutzen**

Dank der zuvor eingerichteten Aliase kannst du häufig verwendete Git-Befehle kürzer schreiben:

- **Status anzeigen:**

  ```bash
  git st
  ```

- **Checkout zu einem Branch:**

  ```bash
  git co branch-name
  ```

- **Branch erstellen und wechseln:**

  ```bash
  git co -b neuer-branch
  ```

- **Commit erstellen:**

  ```bash
  git ci -m "Nachricht"
  ```

- **Commit-Historie anzeigen:**

  ```bash
  git lg
  ```

### **b. Branching und Pull Requests**

Für eine saubere Entwicklung ist es empfehlenswert, neue Features in separaten Branches zu entwickeln und diese über Pull Requests zu mergen.

1. **Neuen Branch erstellen:**

   ```bash
   git checkout -b feature/neues-feature
   ```

2. **Änderungen vornehmen und committen:**

   ```bash
   git add .
   git commit -m "Beschreibung der Änderungen"
   ```

3. **Branch zu GitHub pushen:**

   ```bash
   git push -u origin feature/neues-feature
   ```

4. **Pull Request auf GitHub erstellen:**
   - Gehe zu deinem Repository auf GitHub.
   - Du siehst eine Meldung, dass ein neuer Branch gepusht wurde. Klicke auf **"Compare & pull request"**.
   - Füge eine Beschreibung hinzu und klicke auf **"Create pull request"**.

### **c. Globale `.gitignore` erweitern**

Falls du zusätzliche Dateien oder Verzeichnisse global ignorieren möchtest, bearbeite die globale `.gitignore`-Datei:

```bash
vim ~/.gitignore_global
```

Füge weitere Einträge hinzu:

```
# macOS
.DS_Store
*~

# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.env
.env
*.egg
*.egg-info/
dist/
build/

# Virtuelle Umgebungen
meinenv/
venv/
.env/

# Jupyter Notebook Checkpoints
.ipynb_checkpoints/
.virtual_documents/

# LaTeX
*.aux
*.log
*.out
*.toc

# Editor spezifisch
.vscode/
.idea/
```

### **d. Farben und Lesbarkeit optimieren**

Mit aktiviertem Farbmodus sind Git-Ausgaben besser lesbar:

```bash
git config --global color.ui auto
```

### **e. Commit-Nachrichten formatieren**

Verwende klare und präzise Commit-Nachrichten, die den Zweck der Änderungen beschreiben. Zum Beispiel:

```bash
git commit -m "Füge Rollreibungssimulation mit Tkinter hinzu"
```
