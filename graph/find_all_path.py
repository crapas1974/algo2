from weighted_graph import WeightedGraph

def main():
    graph = WeightedGraph(True)


    # 변 추가
    graph.add_edge(0, 1, 80)
    graph.add_edge(1, 0, 80)
    graph.add_edge(0, 5, 70)
    graph.add_edge(0, 2, 190)
    graph.add_edge(2, 0, 190)
    graph.add_edge(1, 2, 100)
    graph.add_edge(2, 1, 100)
    graph.add_edge(2, 3, 50)
    graph.add_edge(3, 4, 55)
    graph.add_edge(4, 2, 40)
    graph.add_edge(5, 4, 60)

    # 그래프 출력
    graph.print_graph()

    # 꼭짓점 0에서 4로 가는 모든 경로 출력
    paths = graph.find_all_path(0, 4)
    print("꼭짓점 0에서 꼭짓점 4까지의 모든 경로 :")
    for path in paths:
        print("  ", path)

    min_cost, min_path = graph.find_best_path(0, 4)
    print(f"꼭짓점 0에서 꼭짓점 4까지의 최적 경로 : {min_path}")
    print(f"꼭짓점 0에서 꼭짓점 4까지의 최적 경로 비용 : {min_cost}")

if __name__ == "__main__":
    main()