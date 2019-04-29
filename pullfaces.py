from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./img/groups/team1.jpg')
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
  top, right, bottom, left = face_location

  face_image = image[top:bottom, left:right]
  pil_image = Image.fromarray(face_image)
  #this will show images in preview but will not save them
  pil_image.show()

  #if you wanted to save images to drive
  pil_image.save(f'{top}.jpg')  #if doing this you wouldn't need to do .show above unless you wanted them to pop in preview