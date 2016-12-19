#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/16 19:14
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : bayes.py
# @Software: PyCharm

# 朴素贝叶斯分类

import numpy as np

def loadDataSet():
    '''
    加载数据源，用于训练程序
    :return: 训练数据源，类别标签集合
    '''
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1] # 1 表示侮辱性文字，0 表示正常言论
    return postingList,classVec

def createVocabList(dataSet):
    '''
    获取不重复单词的文档列表
    :param dataSet: 数据源
    :return:
    '''
    vocabSet = set([]) # 创建空集合
    for document in dataSet:
        vocabSet = vocabSet | set(document) # 创建两个集合的并集
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    '''
    获取数据源的类别标签（是否为侮辱性文字）
    :param vocabList:
    :param inputSet:
    :return: 类别标签
    '''
    returnVec = [0]*len(vocabList) # 创建一个其中元素都为0的向量
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1 # 含有侮辱性文字的类别标签为1
        else: print("单词: %s 不在集合中!" % word)
    return returnVec


if __name__ == "__main__":
    listPosts,listClass = loadDataSet()
    myVocabList = createVocabList(listPosts)
    print(myVocabList)