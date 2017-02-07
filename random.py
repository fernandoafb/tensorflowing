tf.image.decode_jpeg(contents, channels=3, ratio=1, fancy_upscaling=true, try_recover_truncated=false, acceptable_fraction=1)

for i in image_lists:
  image_path = get_image_path(image_lists, label_name, image_index, image_dir, category)
  contents = image_path.read
  try
    tf.image.decode_jpeg(contents, channels=3, ratio=1, fancy_upscaling=true, try_recover_truncated=false, acceptable_fraction=1)
  rescue
    next

import os
import tensorflow as tf

directories = os.listdir("Pokemon")

for label in directories:
  if label == ".DS_Store":
    continue
  photos = os.listdir("Pokemon/"+label)
  for photo in photos:
    try:
      filename_queue = tf.train.string_input_producer(array(photo))
      reader = tf.WholeFileReader()
      key, value = reader.read(filename_queue)
      tf.image.decode_jpeg(value, channels=3, ratio=1, fancy_upscaling=true, try_recover_truncated=false, acceptable_fraction=1)
    except InvalidArgumentError:
      print("Failed to read the image: "+"Pokemon/"+label+"/"+photo)
      os.remove("Pokemon/"+label+"/"+photo)
      continue
