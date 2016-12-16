import mnist_loader
import netw

# sesuaikan nilai epoch dan hidden_layer_size
# sesuai percobaan yang dilakukan
l_epoch = [30, 60, 90]
l_hidden_layer_size = [0, 30, 60, 90]

for epoch in l_epoch:
    for hidden_layer_size in l_hidden_layer_size:
        print "Epoch: ", epoch, "Hidden layer: ", hidden_layer_size
        train, valid, test = mnist_loader.load_data_wrapper()
        net = network.Network([784, hidden_layer_size, 10])
        net.SGD(train, epoch, 10, 3.0, test_data=test)
        print

