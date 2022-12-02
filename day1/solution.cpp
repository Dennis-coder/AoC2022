#include <iostream>
#include <fstream>
using namespace std;

int main () {
    string temp;
    ifstream dataFile("indata.txt");
    while (getline(dataFile, temp)) {
        cout << temp;
    }
    return 0;
}