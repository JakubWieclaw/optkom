#include "MatrixGraph.h"
#include "tabu_search.h"

#include <cstdlib>
std::vector<std::vector<int>> propose_solution(MatrixGraph G, int k)
{
    std::vector<std::vector<int>> r(k);
    for (int i = 0; i < k - 1; i++)
    {
        r[i].push_back(i);
    }
    for (int i = k -1; i < G.get_size(); i++)
    {
        r[k-1].push_back(i);
    }
    return r;
}

int main(int argc, char* argv[])
{
    MatrixGraph G = MatrixGraph::get_graph_from_instance_file("mycie14.txt", false);
    G.print_graph_to_file();
    int k = 5;
    if (argc > 1)
    {
        k = std::atoi(argv[1]);
    }
    auto r = tabu_search(G, k, propose_solution(G, k), 7, 50, 50000);
    if (!r.empty())
    {
        for (int i = 0; i < r.size(); i++)
        {
            std::cout << i << ": ";
            for (auto v: r.at(i))
            {
                std::cout << v << " ";
            }
        std::cout << std::endl; 
        }
    }
    else
    {
        std::cout << "No solution found" << std::endl;
    }
    return 0;
}