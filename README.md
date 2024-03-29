# Transcription de l'audio à l'aide de Whisper

Ce script Python permet d'enregistrer l'audio à partir d'un périphérique spécifique, tel qu'un casque avec microphone, en utilisant la bibliothèque PyAudio et de le "traduire" en texte à l'aide d'un modèle de reconnaissance automatique de la langue, en l'occurence Whisper : 
https://github.com/openai/whisper

## Prérequis

Assurez-vous d'avoir Python installé sur votre système. Vous pouvez installer les dépendances nécessaires en utilisant la commande suivante :

```bash
pip install pyaudio whisper
```

## Utilisation

1. Exécutez le script `whisp.py`.

2. Le script affichera une liste des périphériques audio disponibles avec leurs identifiants. Identifiez l'ID du périphérique correspondant à votre casque avec microphone.

3. Modifiez la variable `chosen_device_id` dans le script en remplaçant `CHOSEN_DEVICE_ID` par l'ID de votre casque.

4. Relancez le script.

5. Appuyez sur `Ctrl+C` pour arrêter l'enregistrement lorsque vous le souhaitez.

6. Le fichier audio enregistré sera sauvegardé dans le répertoire actuel avec le nom `enregistrement.wav`.

