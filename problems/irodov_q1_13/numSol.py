import numpy as np
import matplotlib.pyplot as plt

def numSol(u, v, l, dt, tolFrac = 1e-4, NMax = 100_000):
    # Initial Condition
    r = l
    th = np.pi/2

    rList = []
    thList = []

    tol = tolFrac * l
    # Forward Euler steps till r > tol
    stepCount = 0
    while r > tol and stepCount < NMax:
        stepCount += 1
        rList.append(r)
        thList.append(th)

        rNext = r + dt * (u*np.cos(th) - v)
        thNext = th - dt * u*np.sin(th) / r

        r,th = rNext,thNext

    # T_answer = stepCount * dt
    return stepCount, np.array(rList), np.array(thList)

if __name__ == "__main__":

    NExpts = 100
    u_arr = np.random.random_sample(NExpts) * 10
    v_arr = u_arr + np.random.random_sample(NExpts) * 10 # As v > u
    l_arr = np.random.random_sample(NExpts) * 15

    exptId = 0

    passC = 0
    passF = 0
    for u,v,l in zip(u_arr,v_arr,l_arr):
        dtC,dtF = 1e-2,1e-3
        stepCountC, rC, thC = numSol(u, v, l, dtC) # Coarse
        stepCountF, rF, thF = numSol(u, v, l, dtF) # Fine

        TExct = l*v / (v*v - u*u)

        plt.title("r vs t")
        plt.xlabel("t")
        plt.ylabel("r")
        plt.plot(dtC*np.arange(stepCountC), rC, label="Coarse Sol")
        plt.plot(dtF*np.arange(stepCountF), rF, label="Fine Sol")

        plt.axvline(TExct, ls="dashed")
        plt.legend()
        plt.grid()
        plt.savefig(f"plots/expt{exptId:003}")
        print(f"Saving @ plots/expt{exptId:003}")
        plt.close()

        TC = dtC * stepCountC
        if np.abs(TC - TExct) / TExct < 1e-2:
            passC += 1

        TF = dtF * stepCountF
        if np.abs(TF - TExct) / TExct < 1e-2:
            passF += 1

        exptId += 1

    print(f"Num expts coarse solver passed: {passC} of {NExpts}")
    print(f"Num expts fine solver passed: {passF} of {NExpts}")
