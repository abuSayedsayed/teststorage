import face_recognition
known_image = face_recognition.load_image_file("./images/img_01.jpg")
target_image = face_recognition.load_image_file("./images/img_02.jpg")

biden_encoding = face_recognition.face_encodings(known_image)
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
print(known_image)
results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)