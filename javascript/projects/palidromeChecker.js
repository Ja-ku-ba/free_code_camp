function palindrome(str) {
    let passCondition = /[a-z0-9]/i;
    let word = ""
    for (let i = 0; i < str.length; i++){
        if (!!str[i].match(passCondition)) {
            word += str[i].toLowerCase()
        }
    }
    for (let i = 0; i < word.length / 2 + 1; i++) {
        if (word[i] !== word[word.length - i - 1]) {
            return  false
        }
    }
    return true
}

console.log(palindrome("eye"))