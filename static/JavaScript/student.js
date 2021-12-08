function username_validate() 
{
    let x = document.getElementById("studentusername").value;
    
    if(isNaN(x)) 
    {
        alert("Username Can Only Be Numeric Value")
    }
}