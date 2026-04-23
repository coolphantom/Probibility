import random
import pandas as pd
import matplotlib.pyplot as plt

def flip_coin(num_flips):
    outcomes = []
    for _ in range(num_flips):
        
        if random.uniform(0, 1) < 0.5:
            outcome = 'H'
        else:
            outcome = 'T'
        
        outcomes.append(outcome)
    return outcomes

def value_counts(num_flips):
    outcomes = flip_coin(num_flips)
    
    h_count = 0
    proportionsH = []
    proportionsT = []
    
    for i in range(num_flips):
        if outcomes[i] == 'H':
            h_count += 1
        
        length = i + 1
        proportionsH.append(h_count / length)
        proportionsT.append((length - h_count) / length)
    
    return pd.DataFrame({
        "integer": range(1, num_flips + 1),
        "proportion_H": proportionsH,
        "proportion_T": proportionsT
    })

def plot_proportions(df_counts):
    
    plt.figure(figsize=(10, 6))
    plt.plot(df_counts['integer'], df_counts['proportion_H'], label='Proportion of Heads (H)', color='blue')
    plt.plot(df_counts['integer'], df_counts['proportion_T'], label='Proportion of Tails (T)', color='orange')
    plt.xlabel('Number of Flips')
    plt.ylabel('Proportion')
    plt.title('Proportion of Heads and Tails in Coin Flips')
    plt.legend()
    plt.grid()
    plt.show()

plot_proportions(value_counts(100000))

