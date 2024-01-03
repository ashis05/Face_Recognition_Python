import cv2
import face_recognition
import tkinter as tk
from tkinter import messagebox
import subprocess

# Load known face images and their names
known_faces = []
known_face_names = []

# Load your known face image ("Ashis.jpg") and associate it with the name "Ashis"
Elon_musk_image = face_recognition.load_image_file("Elon Musk.jpg")
face_encodings = face_recognition.face_encodings(ElonMusk_image)
if len(face_encodings) > 0:
    Elon_Musk_encoding = face_encodings[0]
    known_faces.append(Elon_Musk_encoding)
    known_face_names.append("Elon Musk")
else:
    print("No face of Elon Musk found in the provided image.")

def crossword_interface():
    try:
        # Replace 'your_crossword_file.py' with the actual name of your crossword Python file
        subprocess.Popen(['python', 'Crossword.py'])
    except Exception as e:
        print("Error:", e)

def face_recognition_check():
    video_capture = cv2.VideoCapture(0)
    
    while True:
        ret, frame = video_capture.read()
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        if len(face_encodings) > 0:
            matches = face_recognition.compare_faces(known_faces, face_encodings[0])
            
            if True in matches:
                # Draw a rectangle around the recognized face and display the name
                (top, right, bottom, left) = face_locations[0]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, known_face_names[matches.index(True)], (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
                
                # Display the frame with the recognized face
                cv2.imshow('Video', frame)

                key = cv2.waitKey(10)
                
                # Release the webcam and close the OpenCV window
                video_capture.release()
                cv2.destroyAllWindows()
                
                return True
        
        cv2.imshow('Video', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(10) or 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return False

def login(username, password):
    flag = False

    # Check if username and password are correct
    if username == "Elon Musk" and password == "ElonMusk":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        # Perform facial recognition check
        if face_recognition_check():
            flag = True
        else:
            messagebox.showerror("Facial Recognition Failed", "Face not recognized.")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

    return flag

def interface():
    root = tk.Tk()
    root.title("Login")

    # Create labels and entry fields for username and password
    username_label = tk.Label(root, text="Username:")
    username_label.pack()

    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Password:")
    password_label.pack()

    password_entry = tk.Entry(root, show="*")  # Show '*' for password input
    password_entry.pack()

    # Create a login button
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        success = login(username, password)
        
        if success == True:
            root.destroy()  # Close the login window
            crossword_interface()  # Open crossword interface

    login_button = tk.Button(root, text="Login", command=handle_login)
    login_button.pack()

    # Start the tkinter main loop
    root.mainloop()

interface()
