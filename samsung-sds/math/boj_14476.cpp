// 백준 - 최대공약수 하나 빼기
 

#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int n, answer, arr[1000001], left_gcd[1000001], right_gcd[1000001], k;


int gcd(int a, int b) {
    if(b==0) return a;
    return gcd(b, a%b);
}

int main() {
    scanf("%d\n", &n);


    for(int i=1; i<= n; i++) {
        scanf("%d", &arr[i]);
    }

    for(int i=1; i<=n; i++) {
        left_gcd[i] = gcd(left_gcd[i-1], arr[i]);
        
    }

    for(int i=n; i>=1; i--) {
        right_gcd[i] = gcd(right_gcd[i+1], arr[i]);
    }



    

    answer = -1;

    for(int i=1; i<=n; i++) {
        int now_gcd = gcd(left_gcd[i-1], right_gcd[i+1]);
        if (arr[i] % now_gcd == 0) continue;
        
        if (answer < now_gcd) {
            answer = now_gcd;
            k = arr[i];
        }

    }
    if(answer == -1) printf("%d", answer);
    else printf("%d %d", answer, k);
}