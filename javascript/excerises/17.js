function chunkArrayInGroups(arr, size) {
    let res = [];
    for (let i = 0; i < arr.length; i += size){
        if (i + size > arr.length) {
            res.push(arr.slice(i, arr.length))
        } else {
            res.push(arr.slice(i, i+size))
        }
    }
    return res
}
function chunkArrayInGroups(arr, size) {
    const chunks = [];
    let i = 0;
    while (i < arr.length) {
        chunks.push(arr.slice(i, i + size));
        i += size;
    }
    return chunks;
}