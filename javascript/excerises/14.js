function bouncer(arr) {
    let unaccepted = [false, null, 0, "", undefined, NaN]
    let res = [];
    for (let i = 0; i < arr.length; i++){
        if (!unaccepted.includes(arr[i])){
            res.push(arr[i])
        }
    }
    return res;
}

console.log(bouncer([7, "ate", "", false, 9]));