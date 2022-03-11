let curr_index = -1;
let locked = [false,true,true,true,true,true];

function custom_alert(message){
    const elem = document.createElement('span')
    elem.id = 'custom-alert';
    elem.textContent = message;
    document.querySelector('#custom-alert-container').append(elem);
    elem.style.animation = "fade-out 1s forwards";
    setTimeout(() => {
        elem.style.animation = "fade-in 1s forwards";
        setTimeout(() => {
            document.querySelector('#custom-alert-container').removeChild(elem);
        }, 1000);
    }, 2000);
}

function enter_key(value){
    if (value == 'Enter'){
        let row = Math.trunc(curr_index/5);
        let word = "";
        for (let i = 0; i < 5; i++){
            word += document.querySelector(`#cell-${row * 5 + i}`).innerHTML;
            if (document.querySelector(`#cell-${row * 5 + i}`).innerHTML == ""){
                custom_alert("Not enough letters");
                return;
            }
        }

        //check if the words exists 
        fetch(`/validating_word?word=${word.toLowerCase()}`)
        .then(response => response.json()   )
        .then(data => {
            if (data.result){
                locked[row] = true;
                locked[row + 1] = false;
                let correct_letters = 0
                for (let i = 0; i < 5; i++){
                    const cell = document.querySelector(`#cell-${row * 5 + i}`)
                    const key = document.querySelector(`.${cell.innerHTML.toLowerCase()}`)
                    cell.style.color = "white";
                    key.style.color = "white";

                    if (data[i.toString()][0] == true & data[i.toString()][1] == false){
                        cell.style.background = "#ffbf00"
                        key.style.background = "#ffbf00"
                    }
                    else if (data[i.toString()][0] == true & data[i.toString()][1] == true){
                        cell.style.background = "green"
                        key.style.background = "green"
                        correct_letters += 1;
                    }
                    else{
                        cell.style.background = "gray"
                        key.style.background = "gray"
                    }
                    
                    if (correct_letters == 5){
                        custom_alert("Correct");
                        locked[row + 1] = true;
                    }
                }
            }
            else{
                custom_alert(`${word} is not in the our word list`);
            }
        })

    }   
    else if (value == 'DEL' & curr_index != -1){
        let curr_cell = document.querySelector(`#cell-${curr_index}`);
        if (!locked[Math.trunc(curr_index/5)]){
            curr_cell.innerHTML = "";
            curr_index--;
        }
    }
    else if (curr_index < 29){
        curr_index++;
        if (value.length == 1 & value >= 'A' & value <= 'Z' & !locked[Math.trunc(curr_index/5)]){
            let curr_cell = document.querySelector(`#cell-${curr_index}`);
            curr_cell.innerHTML = value;
        }
        else{
            curr_index--;
        }
    }
}

//enter keys when the user type on the physical keyboard 
window.addEventListener('keyup',(event) => {
    let key_value = event.key.toUpperCase();
    if (key_value == 'BACKSPACE')
        enter_key('DEL');
    else if (key_value == 'ENTER')
        enter_key('Enter');
    else if (key_value.length == 1 & key_value >= 'A' && key_value <= 'Z')
        enter_key(key_value);
})