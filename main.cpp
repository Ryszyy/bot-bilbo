#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream input;

    string buffer;
    string text;
    string speaker;

    cout << "Wprowadz mowce: ";
    cin >> speaker;

    ofstream output(speaker + ".txt");
    input.open("data.txt");
    output.open(speaker + ".txt");

    speaker = "[" + speaker + ":] ``";

    if(output.is_open() && input.is_open())
    {
        int startPos = -1;
        int endPos = -1;
        int counter = 0;

        while(getline(input, buffer))
        {
           text.clear();

           int first = buffer.find(speaker);
           startPos = first != buffer.npos ? first + speaker.length() : -1;

           int last = buffer.rfind('"');
           endPos = last != buffer.npos ? last - startPos: -1;

           if(startPos != -1 && endPos != -1)
               text = buffer.substr(startPos, endPos) + "\n";

           else if(startPos != -1)
               text = buffer.substr(startPos);

           else if(startPos == -1 && endPos == -1)
               continue;

           while(endPos == -1 && getline(input,buffer))
           {
               last = buffer.rfind('"');
               endPos = last != buffer.npos ? last : -1;

               if(endPos != -1)
                    text += buffer.substr(0, endPos) + "\n";

               else
                   text += buffer;
           }



           if(text.length()!=0)
           {
               counter++;
               output.flush();
               output.clear();
               output.seekp(0, ios::end);
               output << text;
               cout<<counter<<text;
           }

        }

        cout<<endl<<"Liczba wierszy: "<<counter;
    }

    input.close();
    output.close();

    return 0;
}
