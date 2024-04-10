import sounddevice as sd
import wave
import speech_recognition as sr
import keyboard
import time
import pyautogui as pag

push_to_talk_hotkey = "q"  # Define the hotkey for starting the recording

# Specify the device index for Samson G-Track Pro
samson_gtrack_pro_device_index = 24

print("👉 Ready to record.")
print("👉 Press Q to start recording.")

FILE_NAME = './stt.wav'  # File name to save the recording
max_wave_length = 20  # Maximum recording length in seconds
sample_rate = 48000  # Sampling frequency

def stop_recording(event):
    global recording
    recording = False

while True:
    keyboard.wait(push_to_talk_hotkey)  # Wait for the hotkey to be pressed
    print('🎙️ Recording started with Samson G-Track Pro...')
    recording = True
    data = sd.rec(int(max_wave_length * sample_rate), samplerate=sample_rate, channels=1, dtype='int16', device=samson_gtrack_pro_device_index, blocking=False)
    start_time = time.time()
    keyboard.add_hotkey(push_to_talk_hotkey, stop_recording, args=({"wait_for_keyup": False},))

    # Check for the stop condition or timeout
    while recording and time.time() - start_time < max_wave_length:
        time.sleep(0.1)  # Check every 100ms

    sd.stop()  # Stop recording
    keyboard.remove_hotkey(push_to_talk_hotkey)
    print('👉 Recording stopped.')

    # Save the recorded data to a WAV file
    with wave.open(FILE_NAME, 'wb') as wf:
        wf.setnchannels(1)  # Mono audio
        wf.setsampwidth(2)  # 16 bits per sample
        wf.setframerate(sample_rate)
        wf.writeframes(data[:int((time.time() - start_time) * sample_rate)].tobytes())  # Save the recorded data
    print("✅ Audio saved to file.")

    # Now we'll try to recognize the speech in the recorded file
    r = sr.Recognizer()
    with sr.AudioFile(FILE_NAME) as source:
        print("👉 Processing audio for speech recognition...")
        audio_data = r.record(source)  # Load the audio file data

        try:
            # Attempt to recognize the speech in the audio file
            text = r.recognize_google(audio_data)
            print(f"💬 Recognized text: \033[92m{text}\033[0m")
            print("👉 Press Enter to type the recognized text.")
            keyboard.wait('enter')  # Wait for you to manually press 'enter'
            time.sleep(0.5)  # Optional delay to ensure the target field is ready
            pag.write(text)
            keyboard.press_and_release('enter')
        except sr.UnknownValueError:
            # This block is executed if the speech is unintelligible
            print("❌ Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            # This block is executed if there's an issue with the Google API request
            print(f"❌ Could not request results from Google Speech Recognition service; {e}.")

    print("👉 Press Q to start recording again.")
