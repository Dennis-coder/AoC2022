#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool descending (int i,int j) { return (i>j); }

int main () {
    string line;
    vector<int> elfs;
    int elf = 0;
    ifstream dataFile("indata.txt");
    
    while (getline(dataFile, line)) {
        if (!line.empty()) {
            elf = elf + stoi(line);
        } else {
            elfs.push_back(elf);
            elf = 0;
        }
    }
    dataFile.close();
    if (elf) {
        elfs.push_back(elf);
    }

    sort(elfs.begin(), elfs.end(), descending);

    // Part 1
    cout << elfs[0] << endl;

    // Part 2
    cout << elfs[0] + elfs[1] + elfs[2] << endl;


    return 0;
}