
import numpy as np
import pandas as pd
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

# speak
l=[]
while(1):
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say "+MyText)
			l.append(MyText)
			SpeakText(MyText)
			print(l)
			if(len(l)>=4):
				break
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occured")
print(l)
df=pd.DataFrame(l)
print(df)
b=[]
tablet=[]
mg=[]
for i in range(df.shape[0]):
    b.append(df.iloc[i][0].split(" "))
for i in range(df.shape[0]):
    if(len(b[i])>1):
        mg.append(b[i][1])
        tablet.append(b[i][0])
    else:
        mg.append(0)
        tablet.append(b[i][0])
print(tablet)        
print(mg)
d=dict(zip(tablet,mg))
print(d)
a=pd.DataFrame(tablet,mg)
print(a)

