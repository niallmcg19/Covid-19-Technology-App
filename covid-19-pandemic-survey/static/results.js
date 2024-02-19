document.addEventListener("DOMContentLoaded", function() {
    // Fetch survey results from the backend
    fetchSurveyResults();

    function fetchSurveyResults() {
        // Make an HTTP GET request to fetch survey results
        fetch("/survey_results")
            .then(response => {
                if (!response.ok) {
                    throw new Error("Failed to fetch survey results");
                }
                return response.json();
            })
            .then(data => {
                // Display survey results
                displaySurveyResults(data);
            })
            .catch(error => {
                console.error("Error fetching survey results:", error);
            });
    }

    function displaySurveyResults(results) {
        var surveyResultsContainer = document.getElementById("surveyResults");
        var resultsHTML = "<h2>Survey Responses:</h2><ul>";

        // Iterate through survey results and create HTML for display
        for (var key in results) {
            if (results.hasOwnProperty(key)) {
                resultsHTML += "<li><strong>" + key + ":</strong> " + results[key] + "</li>";
            }
        }
        resultsHTML += "</ul>";

        // Display HTML in the container
        surveyResultsContainer.innerHTML = resultsHTML;
    }
});
