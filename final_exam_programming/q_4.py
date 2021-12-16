
import matplotlib.pyplot as plt
import numpy as np

def main():
    n= np.linspace(0,100,10)
    y= np.power(n,2)+4*n+8*np.log2(n)
    p = np.power(n,2)
    plt.plot(n,y, label = "T(n) = n^2 + 4*n+8*log2(n)")
    plt.plot(n,p, label = "O(T(n))=n^2")
    plt.title("Computational Costs: T(n) vs O(T(n))")
    plt.xlabel("Size of the problem: n")
    plt.ylabel("Total Number of Instructions: T(n)")
    plt.grid(True)
    plt.legend()
        # Display the line graph.
    plt.show()

# Call the main function.
if __name__ == '__main__':
    main()