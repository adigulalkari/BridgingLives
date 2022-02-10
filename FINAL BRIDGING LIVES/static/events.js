function ShowHiddenDiv() {
    var small = document.getElementById("small");
    var medium = document.getElementById("medium");
    var big = document.getElementById("big");
    var cat1 = document.getElementById("cat1");
    var cat2 = document.getElementById("cat2");
    var cat3 = document.getElementById("cat3");
    var msg1 = document.getElementById("msg1");
    var msg2 = document.getElementById("msg2");
    var msg3 = document.getElementById("msg3");
    var msg4 = document.getElementById("msg4");
    var msg5 = document.getElementById("msg5");
    var msg6 = document.getElementById("msg6");
    var msg7 = document.getElementById("msg7");
    var msg8 = document.getElementById("msg8");
    var msg9 = document.getElementById("msg9");
    var budget = document.getElementById("budget")

    if (small.checked) {
        budget.style.display = 'block'
        msg1.style.display = cat1.checked ? 'block' : 'none';
        msg2.style.display = cat2.checked ? 'block' : 'none';
        msg3.style.display = cat3.checked ? 'block' : 'none';
        msg4.style.display = 'none'
        msg5.style.display = 'none'
        msg6.style.display = 'none'
        msg7.style.display = 'none'
        msg8.style.display = 'none'
        msg9.style.display = 'none'
    }
    if (medium.checked) {
        budget.style.display = 'block'
        msg4.style.display = cat1.checked ? 'block' : 'none';
        msg5.style.display = cat2.checked ? 'block' : 'none';
        msg6.style.display = cat3.checked ? 'block' : 'none';
        msg1.style.display = 'none'
        msg2.style.display = 'none'
        msg3.style.display = 'none'
        msg7.style.display = 'none'
        msg8.style.display = 'none'
        msg9.style.display = 'none'
    }
    if (big.checked) {
        budget.style.display = 'block'
        msg7.style.display = cat1.checked ? 'block' : 'none';
        msg8.style.display = cat2.checked ? 'block' : 'none';
        msg9.style.display = cat3.checked ? 'block' : 'none';
        msg1.style.display = 'none'
        msg2.style.display = 'none'
        msg3.style.display = 'none'
        msg4.style.display = 'none'
        msg5.style.display = 'none'
        msg6.style.display = 'none'
    }
}
