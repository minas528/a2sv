#include <iostream>

void DrawRightAngledTriangle(int size){
    for (int i = 1; i <= size; i++) {
        for (int j = 1; j <= i; j++) {
            std::cout <<"*";
        }
        std::cout<< "\n";
    }
}

void DrawIsoslesTraingle(int size){
    int space;

    for (int i = 1,k = 0; i <=size ; ++i,k =0 ) {
        for (space = 1; space <= size-i ; ++space) {
            std::cout<<" ";
        }
        while (k!=2*i-1){
            std::cout<<"*";
            ++k;
        }
        std::cout<<std::endl;
    }
}
int main() {
    std::cout<<"Please Enter the number of rows\n"<<std::endl;
    int size ;
    std::cin>>size;
    DrawRightAngledTriangle(size);
    DrawIsoslesTraingle(size);
    return 0;
}

