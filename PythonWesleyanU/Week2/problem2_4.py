import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    rlist=[]
    for i in range(10):
        rlist.append(((random.random()*(35-30))+30))
    print(rlist)