const select = document.getElementById("metodo_id").onchange = check;

function check(){
    var option = document.getElementById("metodo_id").value;
    switch (option) {
        case "1":
            setPolybios();
            break;
            case "2":
                setCesar();
                break;
                case "3":
                    setAlberti();
                    break;
        case "4":
            setVigenere();
            break;
            case "5":
                setPlayfair();
                break;
                case "6":
                    setHill();
                    break;
    }
}

function setPolybios() {
    document.getElementById("dimension_opt_id").style.display = "none";
    document.getElementById("llave_opt_id").style.display = "none";
}

function setCesar() {
    document.getElementById("dimension_opt_id").style.display = "none";
    document.getElementById("llave_opt_id").style.display = "none";
}

function setAlberti() {
    document.getElementById("dimension_opt_id").style.display = "none";
    document.getElementById("llave_opt_id").style.display = "block";
}

function setVigenere() {
    document.getElementById("dimension_opt_id").style.display = "none";
    document.getElementById("llave_opt_id").style.display = "block";
}

function setPlayfair() {
    document.getElementById("dimension_opt_id").style.display = "none";
    document.getElementById("llave_opt_id").style.display = "none";
}

function setHill() {
    document.getElementById("dimension_opt_id").style.display = "block";
    document.getElementById("llave_opt_id").style.display = "block";
}

function reset(){
    document.getElementById("dimension_opt_id").style.display = "none";
    document.getElementById("llave_opt_id").style.display = "none";
}

document.getElementById("reset_id").onclick = () => {
    reset();
}

window.onload = check();