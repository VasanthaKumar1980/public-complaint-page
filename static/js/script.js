document.addEventListener("DOMContentLoaded", function () {

    const loginForm = document.getElementById("loginForm");

    if (loginForm) {
        loginForm.addEventListener("submit", function(event) {

            const email = document.getElementById("loginEmail").value;
            const password = document.getElementById("loginPassword").value;

            const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

            if (!email.match(emailPattern)) {
                event.preventDefault();
                console.log("Invalid email");
                return;
            }

            if (password.trim() === "") {
                event.preventDefault();
                console.log("Password empty");
                return;
            }

        });
    }

});