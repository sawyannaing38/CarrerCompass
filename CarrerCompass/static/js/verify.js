const wrapper = document.querySelector(".wrapper");
const verification = document.querySelector("#verification");
const form = document.querySelector("form");
const error = document.querySelector(".error");

wrapper.style.opacity = "1";

form.addEventListener("submit", function(event) {
    event.preventDefault();

    let number = verification.value;

    number = Number(number);

    if (!number)
    {
        error.textContent = "Invalid Input"
        return;
    }

    if (11111 <= number <= 99999)
    {
        form.submit();
    }
})