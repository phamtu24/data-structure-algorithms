const array = [3 , 5, 100, 42, 2];

const bubbleSort = (array) => {
    let arr = array;
    for (let i = 0; i < arr.length; i++) {
        for (let j = i; j < arr.length; j++) {
            if (arr[i] > arr[j]) {
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
        }
    }
    return arr;
}

console.log(bubbleSort(array));