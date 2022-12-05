#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector<int> parse() {
    ifstream dataFile("indata.txt");
    vector<int> data;
    return data;
}

int part1(vector<int> data) {
    return 0;
}

int part2(vector<int> data) {
    return 0;
}

int main () {
    vector<int> data = parse();
    int part1_res = part1(data);
    int part2_res = part2(data);

    cout << part1_res << endl << part2_res << endl;
    
    return 0;
}