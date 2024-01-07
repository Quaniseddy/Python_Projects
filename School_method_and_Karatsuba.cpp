#include <iostream>
#include <string>
#include <math.h>

using namespace std;

//School method addition
string sum(string I1, string I2, int B)
{
    //zero padding
    int n = max(I1.length(), I2.length());
    while (I1.length() < n)
    {
        I1.insert(0, "0");
    }
    while (I2.length() < n)
    {
        I2.insert(0, "0");
    }

    //initialise variables
    string result = "";
    int carry = 0;
    int singleCalc = 0;

    //adding from the last digits first 
    for (int i = n - 1; i >= 0; i--)
    {
        singleCalc = (I1[i] - '0') + (I2[i] - '0') + carry;
        carry = singleCalc / B;
        result.insert(0, to_string(singleCalc % B));
    }

    //if a carry is result in the last carry
    if (carry)
    {
        result.insert(0, to_string(carry));
    }

    //remove any leading zeros
    result = result.erase(0, min(result.find_first_not_of('0'), result.size() - 1));
    return result;
}

//School method subtraction
string sub(string I1, string I2, int B)
{
    //zero padding
    int n = max(I1.length(), I2.length());
    while (I1.length() < n)
    {
        I1.insert(0, "0");
    }
    while (I2.length() < n)
    {
        I2.insert(0, "0");
    }

    //initialise variables
    string result = "";
    int borrow = 0;
    int singleCalc = 0;

    //subtracting from last digits
    //not considering a negtive case, always assume I1 >= I2
    for (int i = n - 1; i >= 0; i--)
    {
        singleCalc = (I1[i] - '0') - (I2[i] - '0') - borrow;
        if (singleCalc >= 0)
        {
            result.insert(0, to_string(singleCalc));
            borrow = 0;
        }
        else
        {
            singleCalc = singleCalc + B;
            result.insert(0, to_string(singleCalc));
            borrow = 1;
        }
    }

    //erase any leading zeros
    result = result.erase(0, min(result.find_first_not_of('0'), result.size() - 1));
    return result;
}

//School method mutiplication 
string multi(string I1, string I2, int B)
{
    //zero padding
    int n = max(I1.length(), I2.length());
    while (I1.length() < n)
    {
        I1.insert(0, "0");
    }
    while (I2.length() < n)
    {
        I2.insert(0, "0");
    }

    //initialise variables
    string result = "0";
    string tmp = "";
    int carry = 0;
    int singleCalc = 0;

    //mutiply I1 with each I2 digits
    for (int i = n - 1; i >= 0; i--)
    {
        //mutiply each digits of I1 with I2[i]
        for (int j = n - 1; j >= 0; j--)
        {
            singleCalc = (I1[j] - '0') * (I2[i] - '0') + carry;
            if (singleCalc >= B)
            {
                tmp.insert(0, to_string(singleCalc % B));
                carry = singleCalc / B;
            }
            else
            {
                tmp.insert(0, to_string(singleCalc));
                carry = 0;
            }
        }

        //if a carry is resulted from last calculation
        if (carry)
        {
            result.insert(0, to_string(carry));
        }

        //zero padding for different I2 digits
        for (int h = n - 2 - i; h >= 0; h--)
        {
            tmp = tmp + "0";
        }

        result = sum(result, tmp, B);
        //clear tmp for next loop
        tmp = "";
    }

    //erase any leading zeros
    result = result.erase(0, min(result.find_first_not_of('0'), result.size() - 1));
    return result;
}

//Karatsuba Multiplication
string Kmulti(string I1, string I2, int B)
{
    //zero padding
    int n = max(I1.length(), I2.length());
    int k = n - n / 2;
    while (I1.length() < n)
    {
        I1.insert(0, "0");
    }
    while (I2.length() < n)
    {
        I2.insert(0, "0");
    }

    //base case where single digit is been processed
    if (n == 1)
    {
        return multi(I1, I2, B);
    }

    //divide I1,I2 into a1,a0,b1,b0
    string a1 = I1.substr(0, n / 2);
    string a0 = I1.substr(n / 2, n - n / 2);
    string b1 = I2.substr(0, n / 2);
    string b0 = I2.substr(n / 2, n - n / 2);

    //recursively call Karatsuba Multiplicaition to narrow down digits in each part
    string p0 = Kmulti(a0, b0, B);
    string p2 = Kmulti(a1, b1, B);
    string p1 = Kmulti(sum(a0, a1, B), sum(b0, b1, B), B);
    string p3 = sub(p1, sum(p0, p2, B), B);

    //zero padding p0,p3 part
    for (int i = 0; i < 2 * k; i++)
    {
        p2.append("0");
    }
    for (int i = 0; i < k; i++)
    {
        p3.append("0");
    }

    //final calculation and earse leading zero
    string result = sum(sum(p2, p3, B), p0, B);
    result = result.erase(0, min(result.find_first_not_of('0'), result.size() - 1));
    return result;
}

bool isSmaller(string I1, string I2){
    if(I1.length()<I2.length()){
        return true;
    }

    if(I1.length()>I2.length()){
        return false;
    }

    int l = I1.length();
    for(int i =0; i<l; i++){
        if((I1[i]-'0') < (I2[i]-'0')){
            return true;
        }
        if((I1[i]-'0') > (I2[i] - '0')){
            return false;
        }
    }
    return false;
}

//Division method
string division(string I1, string I2, int B){   
    string result = ""; 
    //if I1 is smaller than I2 return 0
    if(I1.length()<I2.length() || isSmaller(I1,I2)){
        return "0";
    }

    //if I1 = I2 return 1
    if(I1 == I2){
        return "1";
    }

    //if I1 and I2 are the same length, and after above conditions I1 has to be greater than I2 by now
    //and the ratio has to be >=1 and <B
    int ratio = 0;
    if(I1.length() == I2.length()){
        while(isSmaller(result,I1)){
            ratio++;
            result = sum(result,I2,B);
        }
        if(isSmaller(I1,result)){
            ratio--;
        }
        return to_string(ratio);
    }

    //if I1 length is greater than i2
    int index = 0;
    string dividend = to_string(I1[index] - '0');
    //keep adding digits from the start to find the first divisable part
    while(isSmaller(dividend,I2)){
        index++;
        dividend = sum((dividend+"0"),to_string(I1[index]-'0'),B);
    }
    //looping until all digits is processed
    while(I1.size() > index){
        int i = 0;
        //find the partial digit of result
        if(I2 == dividend){
            i++;
            dividend = "0";
        }
        while(isSmaller(I2,dividend)){
            i++;
            dividend = sub(dividend,I2,B);
        }
        //store the partial digit
        result = result + to_string(i);
        //adding digits of the remainder to make up for the next divisable calculation
        dividend = sum((dividend+"0"),to_string(I1[++index]-'0'),B);
    }
    return result;
}

int main()
{
    string I1, I2, sumResult, multiResult, divResult;
    int B;

    //read and store input 
    cin >> I1 >> I2 >> B;

    sumResult = sum(I1, I2, B);
    cout << sumResult;
    multiResult = Kmulti(I1, I2, B);
    cout << " " + multiResult;
    divResult = division(I1,I2,B);
    cout << " " + divResult;
}