function intersectArray(array1, array2) {
    let hashTable = {};
    let intersectArray = [];

    for (let i = 0; i < array1.length; i++) {
        hashTable[array1[i]] = true;
    }

    for (let j = 0; j < array2.length; j++) {
        if (hashTable[array2[j]]){
            intersectArray.push(array2[j]);
        }
    }
    return intersectArray;
}