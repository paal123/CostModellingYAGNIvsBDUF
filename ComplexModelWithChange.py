#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Plot of upfront vs. YAGNI for complex model
Intersect: A ∩ B
Union: A ∪ B
A but not B: A \ B
Exatcly one of A and B, but not both: A Δ B

Give A independent of B, A ⫫ B

P(A ∩ B) = P(A)P(B)
P(B|A) = P(A ∩ B)/P(A) = P(B)
P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = P(A) + P(B) - P(A)P(B)
P(A \ B) = P(A) - P(A ∩ B) = P(A)-P(A)P(B)
"""
import importlib
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

COST_A = 400
COST_BA = 40
COST_BA_CHANGE = 20
COST_B = 90
COST_B_CHANGED = 70
COST_ROLLBACK_B = 5

PROBABILITIES_B = np.arange(0., 1., 0.01) # P(A)
PROBABILITIES_B_SCOPECHANGE = np.arange(0., 1., 0.01) # P(B)

X,Y = np.meshgrid(PROBABILITIES_B, PROBABILITIES_B_SCOPECHANGE)

def f_ab(probability_b, probability_b_scopechange):
    """
    Estimated cost for upfront
    Probabilites:
    P(A ∩ B) Needed but must change
    1 - P(A \ B) Not needed and no change
    """
    return COST_A + COST_BA + COST_BA_CHANGE*probability_b*probability_b_scopechange + COST_ROLLBACK_B*(1-(probability_b-probability_b*probability_b_scopechange))

def f_a(probability_b, probability_b_scopechange):
    """
    Estimated cost for YAGNI
    Probabilities:
    P(A ∩ B) Needed but must change
    P(A \ B) Needed and no change
    """
    return COST_A + COST_B*(probability_b-probability_b*probability_b_scopechange) +  COST_B_CHANGED*probability_b*probability_b_scopechange

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, f_ab(X, Y), color='red', label='BDUF')
ax.plot_wireframe(X, Y, f_a(X, Y), color='blue', label='YAGNI')
ax.set_xlabel('Probability of B')
ax.set_ylabel('Probability of scope change')
ax.set_zlabel('Expected cost')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()