#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <stdexcept>
#include <cassert>
#include "MatrixGraph.h"

MatrixGraph::MatrixGraph(unsigned int n) : v(n, std::vector<int>(n, 0)) {

}

void MatrixGraph::add_edge(unsigned int row, unsigned int col)
{
    assert(("Test message", row != col));
    if (row == col)
    {
        throw std::runtime_error("Row == Col - you probably don't wanna do that");
    }
    if (v[row][col] != 0)
    {
        throw std::runtime_error("Edge already Exists");
    }
    v[row][col] = 1;
    v[col][row] = 1;
    edge_count++;
}

std::vector<int> MatrixGraph::get_neighbours(unsigned int node)
{
    std::vector<int> res;
    if (node >= v.size())
    {
        std::cout << "This node does not exist" << std::endl;
        return res;
    }

    for (int i = 0; i < v.size(); i++)
    {
        if (v[node][i])
        {
            res.push_back(i);
        }
    }
    return res;
}
unsigned int MatrixGraph::get_size()
{
    return v.size();
}
MatrixGraph MatrixGraph::get_graph_from_instance_file(const std::string &file_name)
{
    std::ifstream file(file_name);
    int size;
    file >> size;
    MatrixGraph g(size);

    unsigned int x, y;
    while ((file >> x) && (file >> y))
    {
        g.add_edge(--x, --y); // Not indexed from 0
    }
}
void MatrixGraph::print_graph_to_file()
{
    std::ofstream file("cpp_graph.txt");
    for (int i = 0; i < get_size(); i++)
    {
        for (int j = 0; j < get_size(); j++)
        {
            file << v[i][j] << " ";
        }
        file << "\n";
    }
}

int print5tostream(std::ostream &stream) {
    stream << 5 << "\n";
}

int main()
{
    // std::ifstream input("input.txt");
    // std::istream &stream = input;
    MatrixGraph G = MatrixGraph::get_graph_from_instance_file("mycie14.txt");
    G.print_graph_to_file();
    std::ofstream file("test");
    print5tostream(std::cout);
    print5tostream(file);
    G.add_edge(0,0);
    return 0;
}