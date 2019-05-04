# My naive-bayes classifier implementation using
# Pandas

import pandas as pd

# Remove the null counts if there are erroneous parts of data. 

# Calculate the number of class.
def calculate_class_num(data, class_col):
    class_counts = data[class_col].value_counts()
    total = len(data.dropna(subset = [class_col]))
    return data[class_col].value_counts() / total


# In this case, we are using "type"
#result_tmp = calculate_class_num(data, "type")



def train_naive_bayes(data):
    return  

def main():
    data = pd.read_csv('../../../data/iris.data') 
    train_naive_bayes(data)
    return  

if __name__ == "__main__":
    main()