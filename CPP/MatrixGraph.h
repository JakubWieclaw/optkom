#pragma once

#include <vector>
#include <string>

class MatrixGraph
{
public:
    MatrixGraph(unsigned int x);
    void add_edge(unsigned int row, unsigned int col);
    std::vector<int> get_neighbours(unsigned int node);
    unsigned int get_size();
    void print_graph_to_file(const std::string file_name="cpp_graph.txt");
    bool edge_exists(unsigned int row, unsigned int col) const;
    static MatrixGraph get_graph_from_instance_file(const std::string &file_name, bool indexed_from_zero);

private:
    std::vector<std::vector<int>> v;
    unsigned int edge_count = 0;
};