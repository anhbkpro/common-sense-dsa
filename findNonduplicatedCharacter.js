function findFirstNonduplicatedCharacter(text) {
    let hashTable = {};
    for (const value of text) {
        if (!hashTable[value]){
            hashTable[value] = 1;
        }else{
            hashTable[value]++;
        }
    }
    console.log(hashTable);
    for (const value of text) {
        if (hashTable[value] == 1){
            return value;
        }
    }
    return null;
}