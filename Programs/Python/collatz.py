# Generate Collatz graph

# Using Digraph from graphvis Python package
# Install graphviz by invoking this command: pip install graphviz
from graphviz import Digraph

# See the accepted file output format on the website: https://www.graphviz.org/doc/info/output.html 
def collatz_graph(max_num, file_name = "collatz_tree", image_format = "png", view = False):
    dot = Digraph()
    existing_num = []
    if(max_num == 1):
        dot.node(str(max_num), str(max_num))
    for num in (range(2,max_num+1)):
        if num in existing_num:
            continue
        dot.node(str(num), str(num))
        existing_num.append(num)
        while True:
            if(num == 1):
                break
            elif(num % 2 == 1):
                prev = num
                num = 3 * num + 1
                dot.node(str(num), str(num))
                dot.edge(str(prev), str(num))
                if num in existing_num:
                    break
                existing_num.append(num)
            elif(num % 2 == 0):
                prev = num
                num = num // 2
                dot.node(str(num), str(num))
                dot.edge(str(prev), str(num))
                if num in existing_num:
                    break
                existing_num.append(num)
    dot.render(file_name, format = image_format, view = view)


# Calculate the shortest graphs to reach 1 
# using dijestra

# For testing this program
if (__name__ == "__main__"):
    collatz_graph(250)
    