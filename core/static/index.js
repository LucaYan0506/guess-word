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


//functions for support-container
document.querySelector('.support-container').addEventListener('click',(event) => {
    if (event.target == document.querySelector('.support-container')){
        close_windows();
    }
})

function close_windows(){
    document.querySelector('.support-container').style.display = 'none';
}
function open_windows(){
    document.querySelector('.support-container').style.display = '';
}

function guess_more_option(){
    title = document.querySelector('h1 a');
    
    if (title.innerHTML == 'Guess another word')
        location.replace('/');
    else
        location.replace("/unlimited");
}