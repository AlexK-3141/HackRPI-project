#chatbot that acts like a therapist and helps user sort out emotions (no ui(no tkinter))
from transformers import pipeline

transcriber = pipeline(task="automatic-speech-recognition")




