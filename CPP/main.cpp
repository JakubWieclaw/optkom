#include "MatrixGraph.h"

int main()
{
    MatrixGraph G = MatrixGraph::get_graph_from_instance_file("mycie14.txt", false);
    G.print_graph_to_file();
    return 0;
}