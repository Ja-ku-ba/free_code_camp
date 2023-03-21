function reverseString(str) {
    let strCoppy = "";
    for (let i = str.length - 1; i >= 0; i--) {
        strCoppy += str[i];
    }
    return `${str} ${strCoppy}`;
}

console.log(reverseString("hello"));