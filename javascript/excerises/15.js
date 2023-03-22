// function sortArray(arr) {
//     for (let i = 0; i < arr.length - 1; i++) {
//         let currLow = arr[i];
//         for (let n = i + 1; n < arr.length; n++){
//             if (currLow > arr[n]) {
//                 currLow = arr[n]
//                 arr[n] = arr[i]
//                 arr[i] = currLow
//             }
//         }
//     }
//     return arr
// }
// const testArr = [5, 5, 3, 4, 3, 5, 8, 2, 1];
// const start = Date.now();
// console.log(sortArray(testArr))
// const end = Date.now();
// console.log(`Execution time: ${end - start} ms`);
//
// const start2 = Date.now();
// console.log(testArr.sort((a, b) => {a - b}))
// const end2 = Date.now();
// console.log(`Execution time: ${end2 - start2} ms`);

// function getIndexToIns(arr, num) {
//     arr = sortArray(arr)
//     for (let i = 0; i < arr.length; i++){
//         if (arr[i] > num || arr[i] === num) {
//             return i
//         }
//     }
//     return  arr.length
// }

function getIndexToIns(arr, num) {
    arr.sort((a,b) => a-b)
    for (let i = 0; i < arr.length; i++){
        if (arr[i] >= num) {
            return i
        }
    }
    return  arr.length
}

console.log(getIndexToIns([40, 60], 50))
console.log(getIndexToIns([10, 20, 30, 40, 50], 35))
console.log(getIndexToIns([10, 20, 30, 40, 50], 30))
console.log(getIndexToIns([5, 3, 20, 3], 5))