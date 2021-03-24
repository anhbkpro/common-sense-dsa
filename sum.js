function sum(low, high) {
    if (low >= high){
        return 0;
    }
    return high + sum(low, high - 1)
}
