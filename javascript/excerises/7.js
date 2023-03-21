function repeatStringNumTimes(str, num) {
    if (num <= 0) {
        return ""
    } else {
        const strCoppy = str;
        while (num > 1){
            str += strCoppy
            num -= 1;
        }
    }
    return str;
}

console.log(repeatStringNumTimes("*", 3));