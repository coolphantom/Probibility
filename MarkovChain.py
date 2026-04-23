import random
import pandas as pd
import matplotlib.pyplot as plt

def generate_random_string(length):
    letters = []
    
    current_letter = "V" if random.uniform(0, 1) < 0.43 else "C"
    letters.append(current_letter)
    
    for i in range(length - 1):
        random_num = random.uniform(0, 1)
        
        if current_letter == "V":
            if random_num < 0.13:
                current_letter = "V"
            else:
                current_letter = "C"
        else:
            if random_num < 0.67:
                current_letter = "V"
            else:
                current_letter = "C"
        letters.append(current_letter)
    
    return letters

def value_counts_fast(max_length):
    letters = generate_random_string(max_length)
    
    v_count = 0
    proportions_V = []
    proportions_C = []
    
    for i in range(max_length):
        if letters[i] == 'V':
            v_count += 1
        
        length = i + 1
        proportions_V.append(v_count / length)
        proportions_C.append((length - v_count) / length)
    
    return pd.DataFrame({
        "integer": range(1, max_length + 1),
        "proportion_V": proportions_V,
        "proportion_C": proportions_C
    })

def plot_proportions(df_counts):
    plt.figure(figsize=(10, 6))
    plt.plot(df_counts['integer'], df_counts['proportion_V'], label='Proportion of Vowels (V)', color='blue')
    plt.plot(df_counts['integer'], df_counts['proportion_C'], label='Proportion of Consonants (C)', color='orange')
    plt.xlabel('Length of String')
    plt.ylabel('Proportion')
    plt.title('Proportion of Vowels and Consonants in Random Strings')
    plt.legend()
    plt.grid()
    plt.show()

plot_proportions(value_counts_fast(100000))