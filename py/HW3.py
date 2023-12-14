import numpy as np
import random

class AR:
    def __init__(self, phi, epsilon, Y0):
        self.phi = np.array(phi)
        self.epsilon = epsilon
        self.Y0 = np.array(Y0)
        self.memory = np.array([])
        self.YPast = np.array(self.Y0)
    def simulate_onePeriod(self):
        # Simulate one period of ar process
        y_onePeriod_ahead = self.phi@self.YPast + (1-alpha)*self.epsilon

        # Update YPast
        ar.YPast = np.append(y_onePeriod_ahead, self.YPast[:-1])

        ## append the new element to the memory
        ar.memory = np.append(self.memory, y_onePeriod_ahead)
    def simulate_nPeriods(self, n):
        for i in range(n):
            _ = AR.simulate_onePeriod()

epsilon = random.choice([0, 0.01])
alpha  = 0.3
rho = 0.9
phi = [[alpha + rho], [alpha * rho]]
ar = AR(phi = phi, epsilon = epsilon, Y0=[0, 0])

print(ar.simulate_onePeriod)

