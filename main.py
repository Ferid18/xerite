import heapq
import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox


def get_city_graph(place_name):
    print(f"'{place_name}' xəritəsi OpenStreetMap-dən yüklənir...")
    try:
        # Şəbəkəni sürücülük yolları üzrə çəkirik
        G = ox.graph_from_place(place_name, network_type="drive")
        # Yalnız bir-biri ilə tam əlaqəli ən böyük alt qrafı seçirik (yol tapılmama problemi olmasın)
        largest_cc = max(nx.strongly_connected_components(G), key=len)
        G = G.subgraph(largest_cc).copy()
        G = ox.project_graph(G)
        return G
    except Exception as e:
        print(f"Xəta baş verdi: {e}")
        return None


# 1. İstifadəçidən Region / Şəhər Seçimi
city = input("Region daxil edin (məs: 'Mitte, Berlin, Germany' və ya 'Baku, Azerbaijan'): ").strip()
if not city:
    city = "Mitte, Berlin, Germany"

G = get_city_graph(city)
if G is None:
    exit()

coords = {node: (data["x"], data["y"]) for node, data in G.nodes(data=True)}
nodes = list(G.nodes())

# Başlanğıc və bitiş nöqtələrini bir-birindən kifayət qədər uzaq seçək
start_node = nodes[0]
goal_node = nodes[-1]


def heuristic(u, v):
    x1, y1 = coords[u]
    x2, y2 = coords[v]
    return math.hypot(x2 - x1, y2 - y1)


# 2. Dijkstra
def run_dijkstra(graph, start, goal):
    dist = {start: 0}
    pq = [(0, start)]
    parent = {start: None}
    visited_edges = []

    while pq:
        d, u = heapq.heappop(pq)
        if u == goal:
            break
        if d > dist.get(u, float("inf")):
            continue

        for v in graph.neighbors(u):
            weight = graph[u][v][0].get("length", 1)
            new_dist = d + weight
            if new_dist < dist.get(v, float("inf")):
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))
                visited_edges.append((u, v))
    return visited_edges, parent


# 3. A* (A-Star)
def run_astar(graph, start, goal):
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    pq = [(f_score[start], start)]
    parent = {start: None}
    visited_edges = []

    while pq:
        _, u = heapq.heappop(pq)
        if u == goal:
            break

        for v in graph.neighbors(u):
            weight = graph[u][v][0].get("length", 1)
            tentative_g = g_score[u] + weight
            if tentative_g < g_score.get(v, float("inf")):
                g_score[v] = tentative_g
                parent[v] = u
                f = tentative_g + heuristic(v, goal)
                heapq.heappush(pq, (f, v))
                visited_edges.append((u, v))
    return visited_edges, parent


# Yolu bərpa edən köməkçi funksiya
def reconstruct_path(parent, target):
    path = []
    curr = target
    while curr is not None and parent.get(curr) is not None:
        path.append((parent[curr], curr))
        curr = parent[curr]
    return path[::-1]


print("Alqoritmlər işləyir...")
dijk_edges, dijk_parents = run_dijkstra(G, start_node, goal_node)
astar_edges, astar_parents = run_astar(G, start_node, goal_node)

shortest_path_dijk = reconstruct_path(dijk_parents, goal_node)
shortest_path_astar = reconstruct_path(astar_parents, goal_node)

# 4. Qaranlıq Tema (Dark UI) və Vizuallaşdırma
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8), facecolor="#080b11")
ax1.set_facecolor("#080b11")
ax2.set_facecolor("#080b11")

ax1.set_title(f"Dijkstra — Ziyarət: {len(dijk_edges)} yol", color="#e5a93b", fontsize=13, pad=10)
ax2.set_title(f"A* (A-Star) — Ziyarət: {len(astar_edges)} yol", color="#38bdf8", fontsize=13, pad=10)

# Bütün yolları arxa fonda tünd rəngdə göstəririk
ox.plot_graph(G, ax=ax1, node_size=0, edge_color="#182030", edge_linewidth=0.7, show=False, close=False)
ox.plot_graph(G, ax=ax2, node_size=0, edge_color="#182030", edge_linewidth=0.7, show=False, close=False)

# Başlanğıc və Hədəf nöqtələri
for ax in (ax1, ax2):
    ax.scatter(*coords[start_node], color="#00ff88", s=60, zorder=6, label="Start")
    ax.scatter(*coords[goal_node], color="#ff0055", s=60, zorder=6, label="Goal")

# 5. Animasiya Funksiyası
step = 25  # Hər kadrda çəkilən yol sayı (sürət)


def update(frame):
    idx = frame * step

    # Dijkstra tərəfi
    if idx < len(dijk_edges):
        for u, v in dijk_edges[idx : idx + step]:
            ax1.plot([coords[u][0], coords[v][0]], [coords[u][1], coords[v][1]], color="#e5a93b", linewidth=1.2, alpha=0.7)
    elif shortest_path_dijk:
        # Axtarış bitdikdə ən qısa yolu qalın parlaq xəttlə göstəririk
        for u, v in shortest_path_dijk:
            ax1.plot([coords[u][0], coords[v][0]], [coords[u][1], coords[v][1]], color="#00ff88", linewidth=2.5, zorder=5)

    # A* tərəfi
    if idx < len(astar_edges):
        for u, v in astar_edges[idx : idx + step]:
            ax2.plot([coords[u][0], coords[v][0]], [coords[u][1], coords[v][1]], color="#38bdf8", linewidth=1.2, alpha=0.7)
    elif shortest_path_astar:
        for u, v in shortest_path_astar:
            ax2.plot([coords[u][0], coords[v][0]], [coords[u][1], coords[v][1]], color="#00ff88", linewidth=2.5, zorder=5)


total_frames = max(len(dijk_edges), len(astar_edges)) // step + 15
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=25, repeat=False)

plt.tight_layout()
plt.show()