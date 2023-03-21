function titleCase(str) {
    str = str.split(" ")
    let word = "";
    for (let i = 0; i < str.length; i++){
        word += str[i][0].toUpperCase()
        if (str[i].length > 0) {
            let temp = str[i].slice(1)
            word += temp.toLowerCase() + " "
        }
    }
    return word.trimEnd();
}

console.log(titleCase("I'm a little tea pot"));
