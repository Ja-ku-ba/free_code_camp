function largestOfFour(arr) {
    let res = [];
    for (let i = 0; i < arr.length; i++){
        let greatest = arr[i][0];
        for (let n = 0; n < 4; n++) {
            if (arr[i][n] > greatest) {
                greatest = arr[i][n]
            }
        }
        res.push(greatest)
    }
    return res;
}

console.log(largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]));