// AUTOMATIC CREDIT FUNCTION // 
/*
The following function redirects participants back to the specified URL to be granted a credit upon completion of an experiment. 
You may use this function to redirect participants back to any site you wish, it is NOT limited to URPP.
This function is to be used in conjuction with the jsPsych plugin package. 
*/

function automatic_credit(url) {
    let ppn = jsPsych.data.urlVariables()['participant'] // the string in the square brackets should be changed accordingly
    setTimeout( function() { window.location.assign(url+ppn) }, 8000) //timeout amount can be changed
}

// --example usage in jsPsych.init()-- //
/*
jsPsych.init({
    timeline: timeline,
    on_finish: function () {
        document.body.innerHTML = '<p>Thanks for participating. You will be redirected shortly.</p>'
        automatic_credit("https://www.google.ca/")
    },
    function() {
        jsPsych.data.get()
    }
});
*/