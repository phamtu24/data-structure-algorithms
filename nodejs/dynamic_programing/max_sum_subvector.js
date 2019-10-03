'use strict';
const array = [3, 2, -1, 3, 6, 3];

const maxSumSubvector = (array) => {
    let maxSum = array[0];
    let sumSoFar = array[0];
    
    for (let i = 1; i < array.length; i++) {
        sumSoFar = Math.max(array[i], array[i] + sumSoFar);
        maxSum = Math.max(maxSum, sumSoFar);
    }
    return maxSum;
};

console.log(maxSumSubvector(array));
