from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf
# input
x = tf.placeholder(tf.float32, [None, 784])

# train weights
W = tf.Variable(tf.zeros([784, 10]))

# bias
b = tf.Variable(tf.zeros([10]))

# output
y = tf.nn.softmax(tf.matmul(x, W) + b)

# validation
y_ = tf.placeholder(tf.float32, [None, 10])

# error function
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# step function
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

# init function
init = tf.initialize_all_variables()

# tf needs a session
sess = tf.Session()
# inits all placeholder values
sess.run(init)

# lets train!
for i in range(10000):
  # streams inputs and outputs from the training data in chuncks of 100 items
  batch_xs, batch_ys = mnist.train.next_batch(100)
  # runs one step of the training
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# checks the correct prediction
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
# determines the accuracy of the model
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# prints the accuracy
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
