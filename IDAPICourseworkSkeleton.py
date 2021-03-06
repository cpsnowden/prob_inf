#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Coursework in Python

from IDAPICourseworkLibrary import *
from numpy import *

#######################################################################################################################
# Coursework 1 begins here

# Function to compute the prior distribution of the variable root from the data set
def Prior(theData, root, noStates):

    root_data = theData[:,root]
    print(noStates[root] + 1)
    return bincount(root_data,None, noStates[root]) / float(root_data.size)


# Function to compute a CPT with parent node varP and xchild node varC from the data array
# it is assumed that the states are designated by consecutive integers starting with 0
def CPT(theData, varC, varP, noStates):

    cPT = zeros((noStates[varC], noStates[varP]), float )

    for col in xrange(noStates[varP]):
        n = count_nonzero(theData[:,varP] == col)
        for row in xrange(noStates[varC]):
            cPT[row,col] = count_nonzero(theData[theData[:,varC] == row, varP] == col)
        cPT[:,col] = cPT[:,col] / n

    return cPT


# Function to calculate the joint probability table of two variables in the data set
def JPT(theData, varRow, varCol, noStates):

    jPT = zeros((noStates[varRow], noStates[varCol]), float )

    for col in xrange(noStates[varCol]):
        for row in xrange(noStates[varRow]):
            jPT[row,col] = count_nonzero(theData[theData[:,varRow] == row, varCol] == col)

    return jPT / theData.shape[0]


# Function to convert a joint probability table to a conditional probability table
def JPT2CPT(aJPT):

    return aJPT / aJPT.sum(axis=0)


# Function to query a naive Bayesian network
def Query(theQuery, naiveBayes):

    root_pdf = naiveBayes[0]

    #For each child, get the link vector associated with the given initialisation
    for cpt in xrange(1,len(naiveBayes)):
        root_pdf = multiply((naiveBayes[cpt])[theQuery[cpt -1]],root_pdf)

    return root_pdf / root_pdf.sum()

#
# End of Coursework 1
#######################################################################################################################
# Coursework 2 begins here

# Calculate the mutual information from the joint probability table of two variables
def MutualInformation(jP):
    mi=0.0
# Coursework 2 task 1 should be inserted here
   

# end of coursework 2 task 1
    return mi
#
# construct a dependency matrix for all the variables
def DependencyMatrix(theData, noVariables, noStates):
    MIMatrix = zeros((noVariables,noVariables))
# Coursework 2 task 2 should be inserted here
    

# end of coursework 2 task 2
    return MIMatrix
# Function to compute an ordered list of dependencies 
def DependencyList(depMatrix):
    depList=[]
# Coursework 2 task 3 should be inserted here
    

# end of coursework 2 task 3
#   return array(depList2)
#
# Functions implementing the spanning tree algorithm
# Coursework 2 task 4

def SpanningTreeAlgorithm(depList, noVariables):
    spanningTree = []
  
    return array(spanningTree)
#
# End of coursework 2

#######################################################################################################################
# Coursework 3 begins here

# Function to compute a CPT with multiple parents from he data set
# it is assumed that the states are designated by consecutive integers starting with 0
def CPT_2(theData, child, parent1, parent2, noStates):
    cPT = zeros([noStates[child],noStates[parent1],noStates[parent2]], float )
# Coursework 3 task 1 should be inserted here
   

# End of Coursework 3 task 1           
    return cPT
#
# Definition of a Bayesian Network
def ExampleBayesianNetwork(theData, noStates):
    arcList = [[0],[1],[2,0],[3,2,1],[4,3],[5,3]]
    cpt0 = Prior(theData, 0, noStates)
    cpt1 = Prior(theData, 1, noStates)
    cpt2 = CPT(theData, 2, 0, noStates)
    cpt3 = CPT_2(theData, 3, 2, 1, noStates)
    cpt4 = CPT(theData, 4, 3, noStates)
    cpt5 = CPT(theData, 5, 3, noStates)
    cptList = [cpt0, cpt1, cpt2, cpt3, cpt4, cpt5]
    return arcList, cptList
# Coursework 3 task 2 begins here

# end of coursework 3 task 2
#
# Function to calculate the MDL size of a Bayesian Network
def MDLSize(arcList, cptList, noDataPoints, noStates):
    mdlSize = 0.0
# Coursework 3 task 3 begins here


# Coursework 3 task 3 ends here 
    return mdlSize 
#
# Function to calculate the joint probability of a single data point in a Network
def JointProbability(dataPoint, arcList, cptList):
    jP = 1.0
# Coursework 3 task 4 begins here


# Coursework 3 task 4 ends here 
    return jP
#
# Function to calculate the MDLAccuracy from a data set
def MDLAccuracy(theData, arcList, cptList):
    mdlAccuracy=0
# Coursework 3 task 5 begins here


# Coursework 3 task 5 ends here 
    return mdlAccuracy
#
# End of coursework 3
#######################################################################################################################
# Coursework 4 begins here


def Mean(theData):
    realData = theData.astype(float)
    noVariables=theData.shape[1] 
    mean = []
    # Coursework 4 task 1 begins here



    # Coursework 4 task 1 ends here
    return array(mean)


def Covariance(theData):
    realData = theData.astype(float)
    noVariables=theData.shape[1] 
    covar = zeros((noVariables, noVariables), float)
    # Coursework 4 task 2 begins here


    # Coursework 4 task 2 ends here
    return covar
def CreateEigenfaceFiles(theBasis):
    adummystatement = 0 #delete this when you do the coursework
    # Coursework 4 task 3 begins here

    # Coursework 4 task 3 ends here

def ProjectFace(theBasis, theMean, theFaceImage):
    magnitudes = []
    # Coursework 4 task 4 begins here

    # Coursework 4 task 4 ends here
    return array(magnitudes)

def CreatePartialReconstructions(aBasis, aMean, componentMags):
    adummystatement = 0  #delete this when you do the coursework
    # Coursework 4 task 5 begins here

    # Coursework 4 task 5 ends here

def PrincipalComponents(theData):
    orthoPhi = []
    # Coursework 4 task 3 begins here
    # The first part is almost identical to the above Covariance function, but because the
    # data has so many variables you need to use the Kohonen Lowe method described in lecture 15
    # The output should be a list of the principal components normalised and sorted in descending 
    # order of their eignevalues magnitudes

    
    # Coursework 4 task 6 ends here
    return array(orthoPhi)

#######################################################################################################################
#######################################################################################################################
# Main program part for Coursework 1

noVariables, noRoots, noStates, noDataPoints, datain = ReadFile("Neurones.txt")
theData = array(datain)
AppendString("results.txt","Coursework One Results by cps15")
AppendString("results.txt","") #blank line
AppendString("results.txt","The prior probability of node 0")
prior = Prior(theData, 0, noStates)
print("Prior")
print(prior)
AppendList("results.txt", prior)

AppendString("results.txt", "The conditional probability matrix P(2|0)")
cPT = CPT(theData,2, 0, noStates)
print("CPT")
print(cPT)
AppendArray("results.txt", cPT)
#print(cPT[:,0].sum(), cPT[:,0].sum(), cPT[:,2].sum(), cPT[:,3].sum())
print(cPT.sum(axis = 0))

AppendString("results.txt", "The joint probability matrix P(2&0)")
jPT = JPT(theData, 2, 0, noStates)
print("Joint")
print(jPT)
AppendArray("results.txt", jPT)
print(sum(jPT))

AppendString("results.txt", "The conditional probability matrix P(2|0) calculated from P(2&0)")
cPT_formJoint = JPT2CPT(jPT)
print("Conditional from joint")
print(cPT_formJoint)
AppendArray("results.txt", cPT_formJoint)
print(cPT_formJoint.sum(axis = 0))

##Create Naive Bayesian Network
#Root node prior is prior
ptble = [prior]
#Get CPT for children->node links
for child in xrange(1,theData.shape[1]):
    cpt = CPT(theData, child, 0, noStates)
    print(child, " " ,cpt)
    ptble.append(cpt)

AppendString("results.txt", "Results of query [4,0,3,2,5]")
query = [4,0,3,2,5]
posterior = Query(query,ptble)
AppendList("results.txt",posterior)

AppendString("results.txt", "Results of query [6,5,2,5,5]")
query = [6,5,2,5,5]
posterior = Query(query,ptble)
AppendList("results.txt",posterior)

#######################################################################################################################