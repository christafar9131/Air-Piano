# Air-Piano

### Objective:
The primary goal of the Air Piano project is to create an interactive, touchless musical instrument that can detect hand movements and finger positions to play piano notes. It aims to demonstrate how computer vision and gesture recognition can be used for creative, contactless human-computer interaction.

### Project Overview:
The Air Piano is a Python-based system that allows users to play the piano in the air, without physically touching any surface. It utilises real-time hand tracking and gesture recognition to simulate piano key presses based on finger positions. When a user moves their hand over virtual keys and performs a pressing gesture, the corresponding piano note is played instantly. This creates an immersive, interactive experience using just a webcam and computer.

Libraries used :
> MediaPipe: For accurate real-time hand landmark detection.

> OpenCV   : For video capture and visual processing of hand gestures.

> NumPy    : To compute distances and angles for detecting finger positions.

> Pygame   : To play piano sound files corresponding to virtual keys.

> Tkinter  : For graphical representation of the piano and user interface elements(This is optional).

### Working

1. A webcam captures live video input of the user's hand.

2. MediaPipe and OpenCV process this input to track hand landmarks in real time.

3. NumPy is used to recognise pressing gestures by analysing the relative positions of fingertips and joints.

4. When a press gesture is identified over a virtual key, the system triggers the corresponding piano sound using Pygame or PyDub.

5. (Optional) A GUI shows a virtual keyboard and highlights the pressed keys.

### Real-Life Application:

1. Music Learning & Practice: Enables beginners or students to explore music without needing an actual piano.

2. Interactive Installations: Ideal for museums, exhibitions, or public displays to create engaging touch-free experiences.

3. Accessible Music Creation: Helpful for individuals with disabilities who may find physical instruments challenging.

4. Rehabilitation & Therapy: Used in physiotherapy to make finger movement exercises more engaging.

5. Entertainment & Art: Great for digital performances or art installations involving music and motion.

### How to run the code

1. Download the project as a Zip.
2. Extract the Zip file(Do not change file structures)
3. Run the following command on the command prompt or terminal:
> pip install -r requirements.txt
4. Run the main.py Python file using any code editor or IDE.

### Conclusion:
The Air Piano is a creative fusion of computer vision, gesture recognition, and digital sound synthesis, offering a futuristic, hygienic, and fun way to make music. It opens the door to new possibilities in human-computer interaction and digital creativity.
