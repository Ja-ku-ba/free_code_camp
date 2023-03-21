function confirmEnding(str, target) {
    if (str.length < target.length) {
        return false
    }
    for (let i = 0 - 1; i < target.length ; i++){
        if (str[str.length - 1 - i] !== target[target.length - 1 - i]){
            return false
        }
    }
    return true;
}

console.log(confirmEnding("Congratulation", "on"));
console.log(confirmEnding("Connor", "n"));