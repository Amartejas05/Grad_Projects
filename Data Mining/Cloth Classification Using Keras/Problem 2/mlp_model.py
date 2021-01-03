import torch
import torch.nn.functional as F


class Net(torch.nn.Module):
    def __init__(self, args):
        h_sizes = 64
        super(Net, self).__init__()
        self.args = args
        self.dropout = args.dropout
        self.drop = torch.nn.Dropout2d(self.dropout)
        self.fc = torch.nn.Linear(784, 3)
        #self.fc1 = torch.nn.Linear(256, 128)
        #self.fc2 = torch.nn.Linear(128, 64)
        #self.out_cifar10 = torch.nn.Linear(64,
                                          # args.class_number_cifar10)

        #self.out_fashion_mnist = torch.nn.Linear(64,
         #                                       args.class_number_fashion_mnist)

    def forward(self, x):
        #print(x.shape)
        if self.args.dataset_name == "cifar10":
            x = x.view(-1, self.args.image_cifar10_width * self.args.image_cifar10_height)
            x = self.drop(x)
            x = F.relu(self.fc(x))  # instead of Heaviside step fn
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.out_cifar10(x)

            return F.log_softmax(x)






        elif self.args.dataset_name == "fashion_mnist":
            x = x.view(-1, self.args.image_fashion_mnist_width * self.args.image_fashion_mnist_height)


            if self.args.visual_flag:
                x = F.relu(self.fc(x))  # instead of Heaviside step fn
                
                network_weight = self.fc.weight.data





                return x, network_weight
            else:
                x = self.drop(x)
                x = F.relu(self.fc(x))  # instead of Heaviside step fn
                x = F.relu(self.fc1(x))
                x = F.relu(self.fc2(x))
                x = self.out_fashion_mnist(x)
                x = F.log_softmax(x)
                ###### Mofify/Add your code here ######






                return x

