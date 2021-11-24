import matplotlib.pyplot as plt
import numpy as np

def main():
    x= np.linspace(0,1000000,100)
    y=np.log2(x)
    q = x
    w= x*np.log2(x)
    plt.plot(x,y, label = "O(logn)")
    plt.plot(x,q, label = "O(n)")
    plt.plot(x,w, label = "O(nlogn)")
    plt.title("Computational Costs: O(log(n)), O(n), O(nlogn)")
    plt.xlabel("Size of the problem: n")
    plt.ylabel("Total Number of Instructions: T(n)")
    plt.grid(True)
    plt.legend()
        # Display the line graph.
    plt.show()

# Call the main function.
if __name__ == '__main__':
    main()