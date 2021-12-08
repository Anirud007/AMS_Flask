function id_validate() {
    let x = document.getElementById("staffusername").value;
    if(isNaN(x)) {
        alert("Staff Id Can Only Be Numeric Value")
    }
}