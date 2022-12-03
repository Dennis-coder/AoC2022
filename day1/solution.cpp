#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool descending (int i,int j) { return (i>j); }

vector<int> parse() {
    ifstream dataFile("indata.txt");
    string line;
    vector<int> elfs;
    int elf = 0;
    
    while (getline(dataFile, line)) {
        if (!line.empty()) {
            elf += stoi(line);
        } else {
            elfs.push_back(elf);
            elf = 0;
        }
    }
    dataFile.close();
    if (elf) {
        elfs.push_back(elf);
    }
    return elfs;
}

int part1(vector<int> elfs) {
    int max = 0;
    for (int i : elfs) {
        if (i > max) {
            max = i;
        }
    }
    return max;
}

int part2(vector<int> elfs) {
    int temp, x = 0, y = 0, z = 0;
    for (int i : elfs) {
        if (i > x) {
            x = i;
        }
        if (x > y) {
            temp = x;
            x = y;
            y = temp;
        }
        if (y > z) {
            temp = y;
            y = z;
            z = temp;
        }
    }
    return x + y + z;
}

int main () {
    vector<int> elfs = parse();
    int part1_res = part1(elfs);
    int part2_res = part2(elfs);
  
    cout << part1_res << endl << part2_res << endl;
    
    return 0;
}