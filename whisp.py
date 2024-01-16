import numpy as np
import wave
import whisper
import pyaudio

model = whisper.load_model("base")

# Paramètres
CHUNK = 1024  # Nombre d'échantillons par trame
FORMAT = pyaudio.paInt16  # Format d'échantillon de 16 bits
CHANNELS = 1  # Nombre de canaux audio
RATE = 16000  # Taux d'échantillonnage
FILENAME = 'enregistrement.wav'

# Afficher la liste des périphériques audio disponibles
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"{i} {info['name']}")

# Recherche de l'ID du périphérique du casque pour l'entrée (microphone)
chosen_device_id = None
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    if "Microphone sur casque" in info["name"]:
        chosen_device_id = i
        break

if chosen_device_id is None:
    raise ValueError("Le périphérique du casque pour l'entrée (microphone) n'a pas été trouvé.")

# Ouverture du fichier WAV
wf = wave.open(FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
wf.setframerate(RATE)

def transcript(file_path):

    result = model.transcribe(file_path)

    return result["text"]

# Fonction de rappel pour enregistrer chaque trame dans le fichier WAV
def callback(in_data, frame_count, time_info, status):
    wf.writeframes(in_data)
    return (in_data, pyaudio.paContinue)

# Configuration de l'enregistrement audio avec PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=chosen_device_id,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

print('Enregistrement... Appuyez sur Ctrl+C pour arrêter.')

try:
    stream.start_stream()
    while stream.is_active():
        pass
except KeyboardInterrupt:
    print('Enregistrement terminé')
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()
    text = transcript(FILENAME) 
    print(text)