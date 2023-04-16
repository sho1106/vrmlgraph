import random

def generate_random_graph(num_nodes, radius, filename):
    # ノードの位置情報のランダム生成
    nodes = []
    for i in range(num_nodes):
        node = [random.uniform(-radius, radius), random.uniform(-radius, radius), random.uniform(-radius, radius)]
        nodes.append(node)
    
    # ノード間のリンクの生成
    links = []
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            dist = ((nodes[i][0]-nodes[j][0])**2 + (nodes[i][1]-nodes[j][1])**2 + (nodes[i][2]-nodes[j][2])**2) ** 0.5
            if dist <= radius:
                links.append([i, j])
    
    # グラフ情報の出力
    with open(filename, "w") as f:
        f.write("graph = {\n")
        f.write("    \"nodes\": " + str(nodes) + ",\n")
        f.write("    \"links\": " + str(links) + "\n")
        f.write("}")

if __name__=="__main__":

    generate_random_graph(20, 0.5, "random_graph.py")