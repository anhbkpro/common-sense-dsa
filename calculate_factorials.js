function calculateFactorials(number) {
    if (number === 1){
        return 1;
    }
    return number * calculateFactorials(number - 1)
}
