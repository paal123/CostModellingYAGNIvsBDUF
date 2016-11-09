"""Plot of upfront vs. YAGNI"""
import matplotlib.pyplot as plt
import numpy as np

COST_A = 400
COST_BA = 40
COST_B = 90
COST_ROLLBACK_B = 5

def f_ab(probability_b):
    """Estimated cost for upfront"""
    return COST_A + COST_BA + COST_ROLLBACK_B*(1-probability_b)

def f_a(probability_b):
    """Estimated cost for YAGNI"""
    return COST_A + COST_B*probability_b

PROBABILITIES = np.arange(0., 1., 0.1)

plt.plot(PROBABILITIES, f_ab(PROBABILITIES), 'r', label='BDUF')
plt.plot(PROBABILITIES, f_a(PROBABILITIES), 'g', label='YAGNI')
plt.ylim(ymin=0)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()
