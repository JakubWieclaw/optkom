#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cassert>
#include "MatrixGraph.h"

using namespace std;

MatrixGraph::MatrixGraph(unsigned int n) : v(n, vector<int>(n, 0)) {}

void MatrixGraph::add_edge(unsigned int row, unsigned int col){
    assert(("Row == Col - you probably don't wanna do that", row != col));
    assert(("Row or Col out of bounds", row < v.size() && col < v.size()));
    //assert(("Edge already exists", !v[row][col]));
    if (v[row][col])
    {
        cout << "Edge already exists" << endl;
        return;
    }

    v[row][col] = 1;
    v[col][row] = 1;
    edge_count++;
}

vector<int> MatrixGraph::get_neighbours(unsigned int node){
    assert(("Node out of bounds", node < v.size()));
    vector<int> res;

    for (int i = 0; i < v.size(); i++)
    {
        if (v[node][i])
        {
            res.push_back(i);
        }
    }
    return res;
}

unsigned int MatrixGraph::get_size(){
    return v.size();
}

MatrixGraph MatrixGraph::get_graph_from_instance_file(const string &file_name, bool indexed_from_zero){
    ifstream file(file_name);
    assert(("File not found",file.is_open()));
    int size;
    file >> size;
    MatrixGraph g(size);

    unsigned int x, y;
    if (indexed_from_zero)
    {
        while (file >> x >> y)
        {
            g.add_edge(x, y);
        }
    }
    else
    {
        while (file >> x >> y)
        {
            g.add_edge(x - 1, y - 1);
        }
    }
    return g;
}

void MatrixGraph::print_graph_to_file(const string file_name){
    ofstream file(file_name);
    for (int i = 0; i < get_size(); i++)
    {
        for (int j = 0; j < get_size(); j++)
        {
            file << v[i][j] << " ";
        }
        file << "\n";
    }
}

bool MatrixGraph::edge_exists(unsigned int row, unsigned int col) const
{
    if (v[row][col])
    {
        return true;
    }
    else
    {
        return false;
    }
}