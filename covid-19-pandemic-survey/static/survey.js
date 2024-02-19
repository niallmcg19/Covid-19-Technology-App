document.addEventListener('DOMContentLoaded', function() {
    const surveyForm = document.getElementById('surveyForm');

    surveyForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Collect form data
        const formData = new FormData(surveyForm);

        // Convert form data to JSON object
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });

        // Send form data to the server using fetch API or XMLHttpRequest
        fetch('/submit_survey', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Ensure correct Content-Type header
            },
            body: JSON.stringify(jsonData) // Convert data to JSON string
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to submit survey');
            }
        })
        .then(data => {
            console.log(data); // Log response from the server
            // Optionally, redirect to a thank you page
            window.location.href = 'thankyou.html';
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle error
        });
    });
});

