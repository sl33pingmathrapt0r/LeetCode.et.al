/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    /**
     * Flatten array up till n dimensions,
     * using recursive call (my long af sol.)
     */

    if (n===0) return arr;

    const flatten=[];

    if (n===1) {
        for (index in arr) {
            const el= arr[index]
            if (Array.isArray(el)) {
                for (x in el) flatten.push(el[x]);
            } else flatten.push(el);
        }
        return flatten
    }
    
    for (index in arr) {
        const el= arr[index]
        if (Array.isArray(el)) {
            const flatX= flat(el, n-1);
            for (x in flatX) flatten.push(flatX[x]);
        } else flatten.push(el);
    }

    return flatten;


    // BETTER ALTERNATIVE
    // if (n === 0) {
    //       return arr;
    //   }
      
    //   let answer = [];
      
    //   arr.forEach(element => {
    //       if (n > 0 && Array.isArray(element)) {
    //           // `...` unpacks arrays too, similar to `*iterable` in Python
    //           answer.push(...flat(element, n - 1));
    //       } else {
    //           answer.push(element);
    //       }
    //   });
      
    //   return answer;
    
};
