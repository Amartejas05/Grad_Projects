import random
from math import floor
import collections

def spliting(iris_data):
    #spliting data into train and test
    train = []
    eighty = int(0.8*len(iris_data))
    train = iris_data[:eighty]
    test = iris_data[eighty:]
    return(test, train)


def kmeans(num_cluster,kmean):
    flag = True
    while flag:
        clust = []
        next_cent = []
        for i in range(num_cluster):
            clust.append([])
            next_cent.append([0, 0, 0, 0])
        for ir in range(len(train)):
            dist = []
            for d in range(num_cluster):
                dist.append(0)
            for i in range(num_cluster):
                for j in range(4):
                    try:
                        dist[i] = floor(dist[i]) + (abs(float(train[ir][j]) - float(kmean[i][j])) ** 2)
                    except ValueError:
                        pass
            mini = min(dist)
            index_min = dist.index(mini)
            clust[index_min].append(train[ir])
            for nc in range(4):
                next_cent[index_min][nc] += float(train[ir][nc])
        for i in range(num_cluster):
            for j in range(4):
                if len(clust[i]):
                    next_cent[i][j] = next_cent[i][j] / len(clust[i])
                else:
                    next_cent[i][j] = 0.0
        if next_cent == kmean:
            flag = False
        else:
            kmean = next_cent

    cluster_name = ['', '', '']
    for i in range(3):
        name = []
        for j in range(len(clust[i])):
            name.append(clust[i][j][4])
        count = collections.Counter(name)
        if not count:
            cluster_name[i] = 'Iris-noise\\n'
        else:
            cluster_name[i] = (count.most_common(1)[0][0])
# -------TESTING------

    correct = 0
    for data in range(len(test)):
        dist1 = [0, 0, 0]
        for ik in range(3):
            for ii in range(4):
                try:
                    dist1[ik] = floor(dist1[ik]) + (abs(float(test[data][ii]) - float(kmean[ik][ii])) ** 2)
                except ValueError:
                    pass
        min_val = min(dist1)
        min_index = dist1.index(min_val)
        print(test[data], "=", cluster_name[min_index])
        if test[data][4] == cluster_name[min_index]:
            correct += 1

    accuracy = correct / len(test) * 100
    print("accuracy =", accuracy)
    return accuracy

if __name__ == '__main__':
    mean_acc = 0
    n_clust = int(input("Enter the Number of clusters"))
    for i in range(5):
        print("Iteration=", i+1)
        iris_data = []
        f = open("iris.csv", "r")
        for i in f:
            if i == "":
                continue
            data = i[:-1].split(",")
            iris_data.append(data)
        random.shuffle(iris_data)
        test, train = spliting(iris_data)
        # random centroid
        kmean = random.sample(iris_data[:len(train)], 10)
        acc = kmeans(n_clust,kmean)
        mean_acc += acc
    Final_acc = mean_acc/5
    print("AVG Accuracy", Final_acc)
