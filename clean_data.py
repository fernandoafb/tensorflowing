import os
import tensorflow as tf

directories = os.listdir("Pokemon")

directories = []
directories.append("Spearow")

for label in directories:
  if label == ".DS_Store":
    continue
  photos = os.listdir("Pokemon/"+label)
  for photo in photos:
    print("Pokemon/"+label+"/"+photo)
    try:
      a = []
      a.append(photo)
      filename_queue = tf.train.string_input_producer(a)
      reader = tf.WholeFileReader()
      key, value = reader.read(filename_queue)
      tf.image.decode_jpeg(value, channels=3, ratio=1, fancy_upscaling=True, try_recover_truncated=False, acceptable_fraction=1)
    except InvalidArgumentError:
      print("Failed to read the image: "+"Pokemon/"+label+"/"+photo)
      os.remove("Pokemon/"+label+"/"+photo)
      continue
