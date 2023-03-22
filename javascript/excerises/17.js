function chunkArrayInGroups(arr, size) {
    let res = [];
    for (let i = 0; i < arr.length; i += size){
        let temp = [];
        if (i + size > arr.length) {
            temp.push(arr.slice(i, arr.length - 1))
        } else {
            temp.push(arr.slice(i, i+size))
        }
        res.push(temp)
    }
    return arr;
}

console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2))