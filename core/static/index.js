setInterval(() => {
    let timer = document.querySelector('#timer');
    
    let sec = parseInt(timer.innerHTML.substr(10,2)) - 1;
    let min = parseInt(timer.innerHTML.substr(4,2));
    let hours = parseInt(timer.innerHTML.substr(0,2));


    if (sec <= 0){
        sec = 59;
        min--;
    }
    if (min < 0){
        min = 59;
        hours--;
    }

    if (hours < 0){
        location.reload();
    } 

    if (sec < 10)
        sec = "0" + sec;
    if (min < 10)
        min = "0" + min;
    if (hours < 10)
        hours = "0" + hours;

    timer.innerHTML = hours + "h " + min + "min " + sec + "sec";
}, 1000);

function show_hide_info_view(){
    const info_view = document.querySelector('.info-container');
    const keyboard = document.querySelector('.keyboard')
    const body = document.querySelector('.body')
    if (info_view.style.display == 'block'){
        keyboard.style.display = 'block';
        body.style.display = 'block';
        info_view.style.display = 'none'
    }else{
        keyboard.style.display = 'none';
        body.style.display = 'none';
        info_view.style.display = 'block'
    }
}

function show_hide_rule_view(){
    const rule_view = document.querySelector('.rule-container');

    if (rule_view.style.display == 'block'){
        rule_view.style.display = 'none';
    }else{
        rule_view.style.display = 'block';
    }
}

document.querySelector('.rule-container').addEventListener('click',event => {
    if (event.target == document.querySelector('.rule-container')){
        show_hide_rule_view()
    }
})