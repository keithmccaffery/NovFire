// This function reads the viewport size from a cookie
function getViewportWidth() {
    var name = "viewportWidth=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

// This function checks the screen width and updates the heading text accordingly
function updateHeadingText() {
    var isMobile = window.matchMedia("screen and (max-width: 600px)").matches;
    console.log("Is mobile: " + isMobile);
    if (isMobile) {
        console.log("Changing heading text");
        document.getElementById('main-heading').textContent = 'Fire Inspection';
    } else {
        document.getElementById('main-heading').textContent = 'Fire Inspection for Annual Fire Safety Statement';
    }
}

// Call the function when the window is resized
window.onresize = updateHeadingText;

// Call the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', updateHeadingText);