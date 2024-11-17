// Example function for client-side validation (optional)
function validateLoginForm() {
    const username = document.querySelector('input[type="text"]');
    const password = document.querySelector('input[type="password"]');

    if (!username.value || !password.value) {
        alert("Please fill in both username and password.");
        return false;
    }
    return true;
}

// Attach the validation function to the button click event
document.querySelector('button').addEventListener('click', function(event) {
    if (!validateLoginForm()) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
