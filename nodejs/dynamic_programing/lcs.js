const lcs = (str1, str2) => {
    let len1 = str1.length;
    let len2 = str2.length;

    let A = Array.from(Array(len1 + 1), () => Array(len2 + 1));

    for (let i = 0; i <= len1; i++) {
        for (let j = 0; j <= len2; j++) {
            if (i == 0 || j == 0) {
                A[i][j] = 0;
            } else if (str1[i - 1] == str2[i - 1]) {
                A[i][j] = 1 + A[i - 1][j - 1];
            } else {
                A[i][j] = Math.max(A[i - 1][j],
                                   A[i][j - 1],
                                   A[i - 1][j - 1]);
            }
        }
    }
    return A[len1][len2];
}

let str1 = 'ATGGX';
let str2 = 'ATGGX';

console.log(lcs(str1, str2));