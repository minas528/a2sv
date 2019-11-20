#include<bits/stdc++.h> 

using namespace std; 

string Sum(string str1, string str2) 
{ 
    
    if (str1.length() > str2.length()) 
        swap(str1, str2); 
  
    
    string str = ""; 
  
    int n1 = str1.length(), n2 = str2.length(); 

    reverse(str1.begin(), str1.end()); 
    reverse(str2.begin(), str2.end()); 
  
    int carry = 0; 
    for (int i=0; i<n1; i++) 
    { 
        int sum = ((str1[i]-'0')+(str2[i]-'0')+carry); 
        str.push_back(sum%10 + '0'); 
  
        carry = sum/10; 
    } 

    for (int i=n1; i<n2; i++) 
    { 
        int sum = ((str2[i]-'0')+carry); 
        str.push_back(sum%10 + '0'); 
        carry = sum/10; 
    } 
  
    if (carry) 
        str.push_back(carry+'0'); 
  
    reverse(str.begin(), str.end()); 
  
    return str; 
} 

bool isSmaller(string num1, string num2){
    int l1 = num1.length(), l2 = num2.length();

    if(l1<l2)
        return true;
    if(l2<l1)
        return false;

    for( int i=0; i<l1; i++)
    if(num1[i] < num2[i])
        return true;
    else if(num1[i] > num2[i])
        return false;
    return false;
}

string Difference(string num1, string num2){
    if(isSmaller(num1,num2))
        swap(num1,num2);

    string str = "";

    int l1 = num1.length(),l2 = num2.length();

    reverse(num1.begin(),num1.end());
    reverse(num2.begin(),num2.end());

    int carry = 0;

    for(int i =0; i<l2;i++){
        int sub = ((num1[i]-'0')-(num2[i]-'0')-carry);
    
        if(sub < 0){
            sub = sub + 10;
            carry = 1;
        }
        else
            carry = 0;
        
        str.push_back(sub + '0');
    }

    for(int i = l2;i<l1;i++){
        int sub = ((num1[i]-'0')-carry);

        if(sub<0){
            sub = sub +10;
            carry =1;
        }else  {
            carry =0;
        }
        str.push_back(sub+'0');
    }

    reverse(str.begin(),str.end());
    if(str.at(0)=='0') str.erase(0,1);
    return str;
}

string mult(string num1,string num2){
    string str = ""; 
  
    int n1 = num1.length(), n2 = num2.length(); 

    reverse(num1.begin(), num1.end()); 
    reverse(num2.begin(), num2.end()); 
    int carry = 0;
    int pro =0;
    for(int i=0;i<n1;i++){
        for(int j=0;j<n2;j++){

            pro = ((num1[i]-'0')*(num2[j]-'0')+carry); 
            str.push_back(pro%10 + '0'); 
  
            carry = pro/10; 
        }
        cout << str<<endl;

    }
  
    return str;
}


int main() 
{ 
    string num1,num2;
    cout << "Please Enter numbers:\n" ; 
    cin>>num1;
    cin>>num2;

    cout<<mult(num1,num2);

    //cout << Difference(num1,num2)+"\n";
    
    // if(num1.at(0)=='-' && num2.at(0)!='-')
    // {
    //     num1.erase(0,1);
    //     cout << Difference(num1,num2);
    // } 
    // else if(num1.at(0)!='-' && num2.at(0)=='-'){
    //     num2.erase(0,1);
    //     cout << Difference(num1,num2);
    // }
    // else if(num1.at(0)=='-' && num2.at(0)=='-'){
    //     num2.erase(0,1);
    // //     num1.erase(0,1);
    // //     cout << Sum(num1,num2);
    // // }
    // // else{
    // //     cout << Sum(num1,num2);
    // // }//cout << Sum(num1, num2)+"\n"; 

    // // cout <<endl;
    return 0; 
} 
