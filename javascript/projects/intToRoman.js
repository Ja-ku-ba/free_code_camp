let numbers = {
    "M":	1000,
    "CM":	900,
    "D":	500,
    "CD":	400,
    "C":	100,
    "XC":	90,
    "L":	50,
    "XL":	40,
    "X":	10,
    "IX":	9,
    "V":	5,
    "IV":	4,
    "I":    1
}

function upToNumber (numb) {
    let res = ""
    while (numb > 0) {
        for (const [key, value] of Object.entries(numbers)) {
            if (value <= numb) {
                res += key
                numb -= value
                break
            }
        }
    }
    return res;
}

function convertToRoman(numb){
    let res = ""
    let comparisions = 1
    while (numb > 1) {
        let current_number = numb % (10 * comparisions)
        let trySingle = Object.keys(numbers).find(key => numbers[key] === current_number);
        if (trySingle === undefined) {
            res = upToNumber(current_number) + res
        }
        else {
            res = trySingle + res
        }
        numb -= numb % (10 * comparisions)
        comparisions *= 10
    }
    return res.toString()
}
console.log(convertToRoman(3999))