function truncateString(str, num) {
    let res = "";
    if (str.length <= num) {
        return str;
    }
    return str.slice(0, num) + "..."
}

console.log(truncateString("A-tisket a-tasket A green and yellow basket", 8))
console.log(truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length))