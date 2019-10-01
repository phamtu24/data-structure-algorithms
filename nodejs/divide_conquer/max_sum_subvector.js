'use strict';
const arr = [-1, 8, -6];

const maxCrossVector = (arr, l, m, h) => {
    let sum = 0;
    let leftSum = -Infinity;
    for (let i = m; i > l-1; i--) {
        sum = sum + arr[i];
        if (sum > leftSum) {
            leftSum = sum;
        };
    };

    sum = 0;
    let rightSum = -Infinity;
    for (let i = m + 1; i < h+1 ; i++) {
        sum = sum + arr[i];
        if (sum > rightSum) {
            rightSum = sum;
        };
    };
    console.log(leftSum + rightSum);
    return leftSum + rightSum;
}

const maxSubVector = (arr, l, h) => {
    if (l == h) {
        return arr[l];
    };
    let m = Math.trunc((l+h)/2);
    console.log(maxSubVector(arr, l, m));
    return Math.max(maxSubVector(arr, l, m), maxSubVector(arr, m+1, h), maxCrossVector(arr, l, m, h))
}
console.log(maxSubVector(arr, 0, arr.length - 1));