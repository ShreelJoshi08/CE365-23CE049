#include <iostream>
#include <fstream>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <cctype>
using namespace std;

unordered_set<string> keywords = {
    "int","long","void","char","return",
    "if","else","while","for"
};

unordered_set<char> operators = {
    '+','-','*','/','=','<','>','&','%'
};

unordered_set<char> punctuations = {
    '(',')','{','}',';',','
};

bool isNumber(const string &s) {
    for(char c:s)
        if(!isdigit(c)) return false;
    return true;
}

int main() {
    ifstream file("Practical3_input.c");
    if(!file) {
        cout << "Error opening file\n";
        return 0;
    }

    vector<string> symbolTable;
    vector<string> lexicalErrors;

    string line;
    int lineNo = 0;
    bool inBlockComment = false;

    cout << "TOKENS\n";

    while(getline(file, line)) {
        lineNo++;

        for (int i = 0; i < line.length(); i++) {

            
            if (inBlockComment) {
                if (i + 1 < line.length() && line[i] == '*' && line[i + 1] == '/') {
                    inBlockComment = false;
                    i++;
                }
                continue;
            }

            
            if (i + 1 < line.length() && line[i] == '/' && line[i + 1] == '*') {
                inBlockComment = true;
                i++;
                continue;
            }

            
            if (i + 1 < line.length() && line[i] == '/' && line[i + 1] == '/') {
                break;
            }

            if (isspace(line[i])) continue;

            
            if (isalpha(line[i]) || line[i] == '_') {
                string word;
                while (i < line.length() && (isalnum(line[i]) || line[i] == '_'))
                    word += line[i++];

                i--;

                if (keywords.count(word))
                    cout << "Keyword: " << word << endl;
                else {
                    cout << "Identifier: " << word << endl;
                    if (find(symbolTable.begin(), symbolTable.end(), word) == symbolTable.end())
                        symbolTable.push_back(word);
                }
            }

            
            else if (isdigit(line[i])) {
                string num;
                while (i < line.length() && (isalnum(line[i]) || line[i] == '.'))
                    num += line[i++];

                i--;

                if (isNumber(num))
                    cout << "Constant: " << num << endl;
                else
                    lexicalErrors.push_back(
                        "Line " + to_string(lineNo) + " : " + num + " invalid lexeme"
                    );
            }

            
            else if (line[i] == '"') {
                string str = "\"";
                i++;
                while (i < line.length() && line[i] != '"')
                    str += line[i++];
                str += "\"";
                cout << "Constant: " << str << endl;
            }

            
            else if (operators.count(line[i])) {
                cout << "Operator: " << line[i] << endl;
            }

            
            else if (punctuations.count(line[i])) {
                cout << "Punctuation: " << line[i] << endl;
            }
        }
    }

    cout << "\nLEXICAL ERRORS\n";
    for (auto &e : lexicalErrors)
        cout << e << endl;

    cout << "\nSYMBOL TABLE ENTRIES\n";
    for (int i = 0; i < symbolTable.size(); i++)
        cout << i + 1 << ") " << symbolTable[i] << endl;

    return 0;
}