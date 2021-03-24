function revertString(text) {
    let stack = [];
    let result = "";
    for (const value of text) {
        stack.push(value);
    }

    while(stack.length > 0){
        result += stack.pop();
    }
    return result;
}
