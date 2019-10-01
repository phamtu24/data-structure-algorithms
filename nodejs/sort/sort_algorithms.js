const array = [3, 5, 100, 42, 2];

const bubbleSort = (array) => {
    let arr = array;
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length - i - 1; j++) {
            if (arr[j] < arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    return arr;
}

const selectionSort = (array) => {
    let arr = array;
    for (let i = 0; i < arr.length; i++) {
        let min = i;
        for (let j = i; j < arr.length; j++) {
            if (arr[min] < arr[j]) {
                min = j
            }
        }
        [arr[i], arr[min]] = [arr[min], arr[i]];
    };
    return arr;
}

const insertionSort = (array) => {
    let arr = array;
    for (let i = 1; i < arr.length; i++) {
        let key = arr[i];
        let j = i - 1;
        while (j >= 0 && key > arr[j]) {
            arr[j + 1] = arr[j];
            j -= 1;
        };
        arr[j + 1] = key;
    };
    return arr;
}

const combSort = (arrar) => {
    let arr = array;
    const getNextGap = (gap) => {
        gap = gap * 1.3;
        if (gap < 1) { return 1 }
        return gap
    }

    let n = arr.length;
    let gap = n;
    let swapped = true;
    while (gap !== -1 || swapped == 1) {
        gap = getNextGap(gap);
        swapped = false;
        for (let i = 0; i < n - gap; i++) {
            if (arr[i] > arr[i + gap]) {
                [arr[i], arr[i + gap]] = [arr[i + gap], arr[i]]
                swapped = true;
            }
        }
    }
    return arr;
}


console.log(combSort(array));