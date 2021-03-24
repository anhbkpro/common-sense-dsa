function countdown(start) {
    console.log(start);
    if (start === 0){
        return;
    }
    else{
        countdown(start - 1);
    }
}
