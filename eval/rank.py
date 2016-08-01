import numpy as np
import liblinearRankSVM as LR
from sklearn.metrics import average_precision_score
from scipy import stats
import sys, random, math
import mlpy
import pdb
import time
import os

def numpyVstack(vA, vB):
	if vA == []:
		vA = vB.copy()
	else:
		vA = np.vstack((vA, vB))

	return vA

def numpyHstack(vA, vB):
        if vA == []:
                vA = vB.copy()
        else:
                vA = np.hstack((vA, vB))

        return vA

def get_q_range(q):
# q is a list of video indices, e.g., [1,1,1,1,2,2,2,3,3,3,3,3,3]
# this function will return the a list of indices where each video starts and ends. e.g., [[0,3],[4,6],[7,12]]
    q_range = []
    for i, qid in enumerate(q):
        if i == 0:
            start = 0
            prev = qid
        elif i == len(q) - 1:
            end = i
            q_range.append((start, end))
        else:
            if qid != prev:
                end = i - 1
                q_range.append((start, end))
                start = i
                prev = qid

    return q_range

def get_number_case(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def load_data(path):
    data = np.load(path)
    x = data['fv']
    y = data['label']
    q = data['q']
    return (x,y,q)

def predSVM_mp(x, y, w):
# evaluate average precision score mp and predict h-factor pred_y
    pred_y = np.dot(x,w)
    mp = average_precision_score(y, pred_y)
    return mp, pred_y

def get_hfactor(w, test_path):
    xtest, ytest, qtest = load_data(test_path)
    pred_y = np.dot(xtest,w)

    return pred_y

def testall(test_path, w):
#################### evaluation code ####################
## Inputs:
    # test_path: path for testing data in a single domain
    # w: weights of svm
##
## Outputs:
    # mp: average precision 
    # pred_y: predicted h-factor
####################                 ####################

    xtest, ytest, qtest = load_data(test_path)
    q_range = get_q_range(qtest)
    mp = []
    pred_y = []
    for ele in q_range:
        [mp_tmp, pred_y_tmp] = predSVM_mp(xtest[ele[0] : ele[1] + 1], ytest[ele[0] : ele[1] + 1], w)
        mp.append(mp_tmp)
        pred_y.append(pred_y_tmp)

    return mp, pred_y

