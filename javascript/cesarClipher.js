const alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
function rot13(str) {
    let res = "";
    for(let i = 0; i < str.length; i++) {
        const currentLetter = alphabet.indexOf(str[i])
        if (currentLetter == -1) {
            if (str[currentLetter] !== " "){
                res += str[i]
            }
            else {
                res += " "
            }
        }
        else {
            if (currentLetter + 13 > alphabet.length - 1){
                res += alphabet[currentLetter + 13 - alphabet.length]
            }
            else {
                res += alphabet[currentLetter + 13]
            }
        }
    }
    return res
}

console.log(rot13("SERR CVMMN!"))