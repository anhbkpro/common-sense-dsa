function findMissingLetter(text) {
    let hashTable = {};
    for (const letter of text) {
        hashTable[letter] = true;
    }

    for (const letter of generateAlphabets()) {
        if (letter != ' ' && !hashTable[letter]){
            return letter;
        }
    }
    return null;
}

function generateAlphabets() {
    let alphabets = [];
    let start = "a".charCodeAt(0);
    let last = "z".charCodeAt(0);
    for (let i = start; i <= last; i++) {
        alphabets.push(String.fromCharCode(i));
    }

    return alphabets.join('');
}