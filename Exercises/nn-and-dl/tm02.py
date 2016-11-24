import mnist_loader
import network

# sesuaikan nilai epoch dan hidden_layer_size
# sesuai percobaan yang dilakukan
epoch = 60
hidden_layer_size = 0

train, valid, test = mnist_loader.load_data_wrapper()
net = network.Network([784, hidden_layer_size, 10])
net.SGD(train, epoch, 10, 3.0, test_data=test)

