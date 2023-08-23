/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // Call fn after some t, using a timeout object. 
    // ...args to unpack args if it is a list of arguments. 
    // The timer starts upon creation and assignment of function obj
    let timeout= setTimeout( ()=> fn(...args) , t);

    // By clearing the timeout object, the fn will also 
    // be removed from the object, thus cancelling execution. 
    // Without `await` above, the function does not wait for
    // timeout to complete before executing the next line. (async fn)
    let cancelFn= () => clearTimeout(timeout)

    return cancelFn;
};

/**
 *  const result = []
 *
 *  const fn = (x) => x * 5
 *  const args = [2], t = 20, cancelT = 50
 *
 *  const start = performance.now() 
 *
 *  const log = (...argsArr) => {
 *      const diff = Math.floor(performance.now() - start);
 *      result.push({"time": diff, "returned": fn(...argsArr))
 *  }
 *  
 *  // Creating and assigning the fn object begins the timer in `cancel`      
 *  const cancel = cancellable(log, args, t);
 *
 *  const maxT = Math.max(t, cancelT)
 *  
 *  // If cancelT <t, then cancel() is executed. Without await, 
 *  // the function proceeds to clear timeout
 *  setTimeout(() => {
 *     cancel()
 *  }, cancelT)
 *
 *  setTimeout(() => {
 *     console.log(result) // [{"time":20,"returned":10}]
 *  }, maxT + 15)
 */
