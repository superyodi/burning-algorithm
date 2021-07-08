// 백준 - 30

#include <cstdio>
#include <algorithm>

using namespace std;

int n, s_size, sum;
char s[100001];

bool compare(int a, int b) {
    return a > b;
}

int main() {
    scanf("%s", s);

    for(int i=0; i < 100001; i++) {
        if(s[i] == '\0') {
            s_size = i;
            break;
        }
    }

    sort(s, s+s_size, compare );


    if(s[s_size-1] == '0') {
        for(int i=0; i< s_size; i++) {
            sum += s[i] - '0';
        }

        if(sum % 3 == 0) {
            printf("%s", s);
            return 0;
        }
    }
    printf("%d", -1);



}





// 강사님 풀이 

// char s[100001];
// int sum, count[128];

// int main() {
//     scanf("%s", s);
//     for(int i=0; s[i]; i++) {
//         sum += s[i] - '0';
//         count[s[i]]++;
//     }
//     if(sum % 3 != 0 || count['0'] == 0) {
//         printf("-1");
//         return 0;
//     }
//     for(int i='9'; i>='0'; i--) {
//         for (int j = 0; j < count[i]; j++) {
//             printf("%c", i);
//         }
//     }

// }