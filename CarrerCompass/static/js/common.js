export function isValidPassword(password)
{
    if ((6 <= password.length <= 8) && (containUpper(password)) && (containNumber(password)) && (containSpecial(password)))
    {
        return true;
    }

    return false
}

export function moveEffect()
{   
    const information = document.querySelector(".information");
    const image = document.querySelector(".image");

    setTimeout(() => {
        information.style.transform = "translateX(0px)";
        image.style.transform = "translateX(0px)";
    }, 10)
}

function containUpper(password)
{
    for (const char of password)
    {
        if ('A' <= char && char <= 'Z')
        {
            return true;
        }
    }

    return false;
}

function containNumber(password)
{
    for (let char of password)
    {
        char = Number(char)

        if (char)
        {   
            return true;
        }
    }
    return false;
}

function containSpecial(password)
{
    for (const char of password)
    {
        if ((char == '@') || (char == '#') || (char == '!') || (char == '*' ) || (char == '$'))
        {   
            return true;
        }
    }
    return false
}

// Typing Effect
export function showTypingEffect(obj, texts)
{   
    obj.textContent = "";
    const words = texts.split(" ");
    let currentIndex = 0;

    const intervalId = setInterval(() => {
        obj.textContent += `${words[currentIndex]} `;
        currentIndex += 1;

        if (currentIndex >= words.length)
        {
            clearInterval(intervalId);
        }
    }, 100)
}

// Valid image 
export function isValidImage(imageName)
{
    let [, extenstion] = imageName.split(".");

    if (extenstion == "jpg" || extenstion == "jpeg" || extenstion == "png")
    {
        return true;
    }

    return false;
}

// For toggleing show
export function toggleShow(obj)
{
    const height = window.innerHeight;

    const objHeight = obj.getBoundingClientRect().top;
    
    if ((objHeight < height) && (obj.getBoundingClientRect().bottom >= 0))
    {
        obj.classList.add("show");
    }

    else 
    {
        obj.classList.remove("show");
    }
}

// Function for getting cookie
export function getCookie(name)
{
    let cookieValue = "";

    // Check if cookies exist
    if (document.cookie && document.cookie !== "")
    {
        // Split the cookie
        const cookies = document.cookie.split(";");

        // Check that cookies contain the desired name
        for (const cookie of cookies)
        {
    
            if (cookie.substring(0, name.length + 1) === (name + "="))
            {
                // Getting cookie after the equal sign
                cookieValue = cookie.substring(name.length + 1)

                // decoding url
                cookieValue = decodeURIComponent(cookieValue);
                return cookieValue;
            }
        }

        return cookieValue;
    }
    return cookieValue;
}