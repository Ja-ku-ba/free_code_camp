function booWho(bool) {
    let acceptedVariables = [true, false]
    return acceptedVariables.includes(bool)
}

function  booWho(bool) {
    return typeof bool === "boolean";
}
console.log(booWho(true));
console.log(booWho(123));
console.log(booWho("false"));
console.log(booWho(null));