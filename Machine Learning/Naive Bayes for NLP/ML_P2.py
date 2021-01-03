import os
import copy, random, math
from sklearn.metrics import confusion_matrix, classification_report

target = {}
file_name = {}
totaldic = {}
alldic = {}

def stopWords():
    f = open("stopWords.txt", "r")
    stopwords = f.read()
    next_line = ['\n']
    for i in next_line:
        stopwords= stopwords.replace(i, ' ')
        li = list(stopwords.split(" "))
    text = ([ f' {x} ' for x in li])
    text.pop()
    return text


def clean(file, stopwords):
    file.replace('\n', ' ')
    symbol_remove = ['<','>','?','.','"',')','(','|','-','#','*','+','\'','&','^','`','~','\t','$','%',"'",'!','/','\\','=',',',':']
    file = file.lower()
    for i in symbol_remove:
        file = file.replace(i,' ')
    for i in stopwords:
        file = file.replace(i, ' ')
    file = file.split(' ')
    if '' in file: file.remove('')
    if ' ' in file: file.remove(' ')
    return file


def get_ran_file():
    global group
    while (len(target_l)):
        r_fo = random.randint(0, len(target_l)-1)
        folder_n = target_l[r_fo]
        if len(file_name[folder_n])== 0:
            target_l.remove(folder_n)
        else:
            r_fi = random.randint(0, len(file_name[folder_n])-1)
            fil = file_name[folder_n][r_fi]
            file_name[folder_n].remove(fil)
            group = folder_n
            data = open("20_newsgroups/"+folder_n+'/'+fil,'r')
            return data.read()
    group = 'NULL'
    return 'NULL'

def predict(target_l):
    probabilities = []
    y_pred = []
    y_true = []
    success = 0
    iteration = 0
    global group
    test = 1
    while(test):
        test = get_ran_file()
        iteration = iteration + 1
        if iteration >= 1000 and (iteration % 1000) == 0:
            print("{}% of testing done".format(iteration/100))
        if test =='NULL':
            break
        final = clean(test, stopwords)
        if '' in final: final.remove('')
        if ' ' in final: final.remove(' ')
        probabilities = []
        for k in target:
            probabilities.append(probability(final,alldic[k]))
            y_pred.append(target[probabilities.index(max(probabilities))])
            y_true.append(group)
        if group == target[probabilities.index(max(probabilities))]:
            success = success + 1
    print("Testing done")
    print('\nAccuracy = %.1f'% (float(success)/float(iteration - 1)*100))
    #print("Classification Report:",classification_report(y_true, y_pred))
    #print(confusion_matrix(y_true, y_pred))

def probability(final, dic):
    sum_ = sum(dic.values())
    pred = 0.0
    for f in final:
        value = dic.get(f, 0.0) + 0.0001
        pred = pred + math.log(float(value)/float(sum_))
    return pred

if __name__ == '__main__':
    #data preprocessing
    stopwords = stopWords()
    target = os.listdir("20_newsgroups/")
    for i in target:
        print("reading files from 20_newsgroups/{}".format(i))
        dic = {}
        filelist = os.listdir("20_newsgroups/"+i)
        split = 0
        for j in filelist:
            split = split + 1
            if split > 500:
                break
            filename = "20_newsgroups/"+i+"/"+j
            f = open(filename,"r")
            filecont = f.read()
            cleandata = clean(filecont, stopwords)
    #CountVectorization
            for word in cleandata:
                value = dic.get(word, 0)
                value_t = totaldic.get(word, 0)
                if value == 0:
                    dic[word] = 1
                else:
                    dic[word] = value + 1
                if value_t == 0:
                    totaldic[word] = 1
                else:
                    totaldic[word] = value_t + 1
            filelist.remove(j)
        file_name[i] = filelist
        alldic[i] = dic
    print("Total words is", len(totaldic))
    #predict
    target_l = copy.deepcopy(target)
    predict(target_l)