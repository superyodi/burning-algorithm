// 백준 - 에라토스테네스의 체

#include <cstdio>

using namespace std;
int n, k, cnt;
bool che[1001];

int main() {

    scanf("%d %d", &n, &k);

    for(int i=2; i <= n; i++) {
        if (!che[i]) {
            cnt++;
            che[i] = true;

            if(cnt == k) {
                printf("%d\n", i);
                break;
            }
            
            for(int j=2*i; j <= n; j += i) {
                if(!che[j]) {
                    cnt++;
                    che[j] = true;
                    

                    if(cnt == k) {
                        printf("%d\n", j);
                        return 0;
                    }
                }

            } 
        }
    }
}