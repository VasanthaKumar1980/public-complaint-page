const loginTab = document.getElementById("loginTab");
const registerTab = document.getElementById("registerTab");

const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");

// Dummy user (for testing)
const validEmail = "test@gmail.com";
const validPassword = "123456";

loginForm.addEventListener("submit", function(event) {
    event.preventDefault();

    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    // Email format check
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    if (!email.match(emailPattern)) {
        alert("Please enter a valid email!");
        return;
    }

    // Authentication check
    if (email === validEmail && password === validPassword) {
        alert("Login Successful!");
        window.location.href = "complaint.html";
    } else {
        alert("Invalid Email or Password");
    }
});

// Tab switching (same as your code)
loginTab.addEventListener("click", () => {
    loginForm.style.display = "flex";
    registerForm.style.display = "none";

    loginTab.classList.add("active");
    registerTab.classList.remove("active");
});

registerTab.addEventListener("click", () => {
    loginForm.style.display = "none";
    registerForm.style.display = "flex";

    registerTab.classList.add("active");
    loginTab.classList.remove("active");
});