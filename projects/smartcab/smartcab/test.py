# #one over t squared
# self.trial_number += 1
# self.epsilon -= float(1)/(float(self.trial_number)**2)

# #exp minus a t: this just doesnt work
# self.trial_number += 1
# self.epsilon -= math.exp(-1*self.alpha*self.trial_number)

# #cosine
# self.trial_number += 1
# self.epsilon -= math.cos(self.alpha*self.trial_number)
import math
import matplotlib.pyplot as plt
epsilon = 1
alpha = .9

list = []
for i in range(1,500):
  i += 1
  epsilon-= math.exp(-1*alpha*i*.9)
  list.append(epsilon)

print(list)
plt.plot(list)
plt.show()