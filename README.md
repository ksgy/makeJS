makeJS
======

Make native JS code from input HTML

Input:

<div id="container">
    <ul class="listBox">
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
    </ul>
    <p></p>
    <h3></h3>
    <p>
        <img src="" alt="">
        <em></em>
    </p>
</div>

Output:


// DEBUG <div id='container'>
var _div_container__0 = document.createElement('DIV');
_div_container__0.setAttribute('id', 'container');
// DEBUG <ul class='listBox'>
var _ul__listBox_0 = document.createElement('UL');
_ul__listBox_0.setAttribute('class', 'listBox');
// DEBUG <li>
var _li___0 = document.createElement('LI');
// DEBUG <li>
var _li___1 = document.createElement('LI');
// DEBUG <li>
var _li___2 = document.createElement('LI');
// DEBUG <li>
var _li___3 = document.createElement('LI');
// DEBUG <li>
var _li___4 = document.createElement('LI');
// DEBUG <p>
var _p___0 = document.createElement('P');
// DEBUG <h3>
var _h3___0 = document.createElement('H3');
// DEBUG <p>
var _p___1 = document.createElement('P');
// DEBUG <img src='' alt=''>
var _img___0 = document.createElement('IMG');
_img___0.setAttribute('src', '');
_img___0.setAttribute('alt', '');
// DEBUG <em>
var _em___0 = document.createElement('EM');
document.body.appendChild(_div_container__0);


_div_container__0.appendChild(_ul__listBox_0);
_ul__listBox_0.appendChild(_li___0);
_ul__listBox_0.appendChild(_li___1);
_ul__listBox_0.appendChild(_li___2);
_ul__listBox_0.appendChild(_li___3);
_ul__listBox_0.appendChild(_li___4);
_div_container__0.appendChild(_p___0);
_div_container__0.appendChild(_h3___0);
_div_container__0.appendChild(_p___1);
_p___1.appendChild(_img___0);
_p___1.appendChild(_em___0);
