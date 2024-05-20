# PyLoL

_IN ENGLISH 🇬🇧_

PyLol is a set of tools to automate tasks for League of Legends, developed by [@kitsuiwebster](https://github.com/kitsuiwebster).

## Accept a game automatically 🖱️

This script uses `pyautogui` to locate and click the "Accept" button in the League of Legends client automatically. Follow the steps below to set up and run the script on a Windows machine.

### Prerequisites 🛠️

1. Ensure Python is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. Install pip, the package installer for Python.

    To proceed, open a terminal and run this command:

    ```sh
    py get-pip.py
    ```

3. Install `pyautogui` and `Pillow` (used by `pyautogui` for image processing). You can install these packages using pip:

    ```sh
    pip install pyautogui Pillow
    ```

### Setup 💻

1. **Clone the repository**:

    Open a terminal with administrative rights. I recommend using [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701?rtc=1&hl=fr-fr&gl=FR) for a better experience, as it can sometimes fail with Command Prompt (cmd), and its UX is better than native PowerShell.

    ```sh
    git clone https://github.com/kitsuiwebster/pylol.git
    ```

2. **Navigate to the project directory**:

    ```sh
    cd pylol
    ```

### Running the Script 🚀

1. **Run the script**:

    ```sh
    python accept_game.py
    ```

### Explanation ℹ️

Once the script has started, it continuously looks for the "Accept" button in the League of Legends client. The script will never stop running until you press `Ctrl + C` in the terminal. This feature allows the script to handle scenarios where a match is found but someone dodges the game, enabling it to accept the game again, infinitely.

🎮 Good luck and have fun ! But please respect yourself and don't pick Garen.

### Need help? 🚨

Never hesitate contacting me for any help needed, any suggestion or anything: `kitsuiwebster` on Discord.

_EN FRANÇAIS 🇫🇷_

PyLol est un ensemble d'outils pour automatiser des tâches dans League of Legends, développé par [@kitsuiwebster](https://github.com/kitsuiwebster).

## Accepter une partie automatiquement 🖱️

Ce script utilise `pyautogui` pour localiser et cliquer sur le bouton "Accepter" dans le client de League of Legends automatiquement. Suivez les étapes ci-dessous pour configurer et exécuter le script sur une machine Windows.

### Prérequis 🛠️

1. Assurez-vous que Python est installé sur votre système. Vous pouvez télécharger Python depuis [python.org](https://www.python.org/downloads/).
2. Installez pip, le gestionnaire de packages pour Python.

    Pour cela, ouvrez un terminal et entrez cette commande.

    ```sh
    py get-pip.py
    ```

3. Installez `pyautogui` et `Pillow` (utilisé par `pyautogui` pour le traitement d'image). Vous pouvez installer ces packages en utilisant pip :

    ```sh
    pip install pyautogui Pillow
    ```

### Configuration 💻

1. **Clonez le dépôt** :

    Ouvrez un terminal avec des droits d'administrateur. Je recommande d'utiliser [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701?rtc=1&hl=fr-fr&gl=FR) pour une meilleure expérience, car ça peut parfois échouer avec l'invite de commande (cmd), et l'expérience utilisateur de Windows Terminal est meilleure que celle du PowerShell natif.

    ```sh
    git clone https://github.com/kitsuiwebster/pylol.git
    ```

2. **Naviguez vers le répertoire du projet** :

    ```sh
    cd pylol
    ```

### Exécution du Script 🚀

1. **Exécutez le script** :

    ```sh
    python accept_game.py
    ```

### Explication ℹ️

Une fois le script lancé, il recherche continuellement le bouton "Accepter" dans le client de League of Legends. Le script ne s'arrêtera jamais tant que vous n'appuyez pas sur `Ctrl + C` dans le terminal. Cette fonctionnalité permet au script de gérer des scénarios où une partie est trouvée mais quelqu'un esquive la partie, lui permettant d'accepter à nouveau la partie, indéfiniment.

🎮 Bonne chance et amusez-vous bien ! Mais s'il vous plaît, respectez-vous et ne choisissez pas Garen.

### Besoin d'aide ? 🚨

N'hésitez jamais à me contacter pour toute aide nécessaire, toute suggestion ou quoi que ce soit : `kitsuiwebster` sur Discord.
