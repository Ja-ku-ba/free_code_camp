function findLongestWordLength(str) {
    str = str.split(" ");
    let longest = 0;
    for (let i =0; i < str.length; i++){
        if (str[i].length > longest) {
            longest = str[i].length
        }
    }
    return longest
}

console.log(findLongestWordLength("The quick brown fox jumped over the lazy dog"));