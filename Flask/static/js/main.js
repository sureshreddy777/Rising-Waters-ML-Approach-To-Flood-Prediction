document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('predictionForm');
    const resultSection = document.getElementById('resultSection');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const riskLevel = document.getElementById('riskLevel');
    const confidence = document.getElementById('confidence');
    const resultCard = document.getElementById('resultCard');
    const resultIcon = document.getElementById('resultIcon');

    // Add scroll animation to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = 'all 0.6s ease-out';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100);
    });

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // Show loading state
        loadingSpinner.style.display = 'flex';
        resultSection.style.display = 'none';

        // Disable button
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn.innerHTML;
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';

        // Gather form data
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Send request
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                // Hide loading
                loadingSpinner.style.display = 'none';
                resultSection.style.display = 'block';

                if (data.success) {
                    riskLevel.textContent = data.risk_level;
                    confidence.textContent = `Confidence Score: ${data.confidence}%`;

                    // Style based on risk level
                    if (data.prediction === 1) { // High Risk
                        resultCard.className = 'card p-4 text-center high-risk';
                        resultIcon.className = 'fas fa-exclamation-triangle fa-3x text-danger mb-3';
                    } else { // Low Risk
                        resultCard.className = 'card p-4 text-center'; // Default is low risk style
                        resultIcon.className = 'fas fa-check-circle fa-3x text-success mb-3';
                    }

                    // Smooth scroll to result
                    resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                } else {
                    alert('Error: ' + (data.error || 'Unknown error occurred'));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while processing your request.');
                loadingSpinner.style.display = 'none';
            })
            .finally(() => {
                // Restore button
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            });
    });
});