import os
directories = os.listdir("Pictures")

number_of_features = 768
number_of_classes = len(directories) - 1
learning_rate = 0.5

import numpy as np
import tensorflow as tf
x  = tf.placeholder(tf.float32, shape=[None, number_of_features])
W  = tf.Variable(tf.zeros([number_of_features, number_of_classes]))
b  = tf.Variable(tf.zeros([number_of_classes]))
y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder(tf.float32, shape=[None, number_of_classes])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

init = tf.initialize_all_variables()
sess = tf.InteractiveSession()
saver = tf.train.Saver()
sess.run(init)

# restore the model
# saver.restore(sess, "/Users/ac-fbraz/dev/tensorflow/sw_model.ckpt")
# print("Model restored from file: %s." % save_path)

i = 0
from PIL import Image
for label in directories:
  if label == ".DS_Store":
    continue
  photos = os.listdir("Pictures/"+label)
  for photo in photos:
    try:
      img = Image.open("Pictures/"+label+"/"+photo)
    except IOError:
      print("Failed to read the image: "+"Pictures/"+label+"/"+photo)
      continue
    img = img.convert("RGB")
    l = [0] * number_of_classes
    l[i] = 1
    ll = np.array(l).reshape(1, number_of_classes)
    xx = np.array(img.histogram()).reshape(1,number_of_features)
    sess.run(train_step, feed_dict={x: xx, y_: ll})
  i = i + 1

# save the model
# save_path = saver.save(sess, "/Users/ac-fbraz/dev/tensorflow/sw_model.ckpt")
# print("Model saved in file: %s" % save_path)

# evaluate the accuracy of our model
# correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

# actually classify something
# prediction = sess.run(tf.argmax(y, 1), feed_dict={x: xx})
# prediction = sess.run(y, feed_dict={x: xx})
# print prediction
