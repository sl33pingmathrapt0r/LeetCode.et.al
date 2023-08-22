/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    // promise object= 
    // eventual completion (or failure) of
    // an asynchronous operation and its 
    // resulting value. 
    
    let result= (await promise1) + (await promise2);
    // OR result= ( await Promise.all([promise1,promise2]) ).reduce((accumulate, currentVal) => accumulate + currentVal, 0);

    // console.log(typeof result); => returns number
    return result;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
