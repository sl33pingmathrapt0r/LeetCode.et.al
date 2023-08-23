/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    // without using lodash's _.groupBy()
    let grouped= {};
    for(x of this) {
        let key= fn(x);
        if (key in grouped) grouped[key].push(x);
        else grouped[key]= [x];
    }
    return grouped;    

    // OR
    // return this.reduce((res, item)=> {
    //     const key= fn(item);
    //     if (key in res) res[key].push(item);
    //     else  res[key]=[item];
    //     return res;
    // }, {});
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
