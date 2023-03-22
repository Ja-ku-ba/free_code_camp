function mutation(arr) {
    arr = arr.map(word => word.toLowerCase())
    for (let i = 0; i < arr[1].length; i++) {
        if (!arr[0].includes(arr[1][i])) {
            console.log(arr[1][i])
            return false
        }
    }
    return true
}

console.log(mutation(["Mary", "Aarmy"]))