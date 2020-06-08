import tensorflow as tf
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = tf.convert_to_tensor(x_train, dtype=tf.float32)
mn = tf.reduce_mean(x_train,axis=0)
V = x_train - mn
V = tf.reshape(V, shape=(60000,28*28))

sigma = tf.matmul(tf.transpose(V),V)
eigs, O = tf.linalg.eigh(sigma)
eigv = tf.transpose(O)
eigv = tf.reverse(eigv,axis=[0])

N = 20
projections = tf.matmul(eigv[:N], tf.transpose(V))
projected_pictures = tf.matmul(tf.transpose(projections), eigv[:N])
projected_pictures = mn + tf.reshape(projected_pictures, (60000, 28, 28))

for i in range(8):
    plt.imshow(projected_pictures[i].numpy(), cmap='Greys')
    plt.show()
    plt.imshow(x_train[i].numpy(), cmap='Greys')
    plt.show()