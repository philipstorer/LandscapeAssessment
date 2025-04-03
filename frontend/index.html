document.getElementById('analysisForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const payload = {
        brand: document.getElementById('brand').value,
        indication: document.getElementById('indication').value,
        geography: document.getElementById('geography').value || 'U.S.',
        competitive_focus: document.getElementById('competitiveFocus').value || 'General'
    };

    document.getElementById('result').innerHTML = "Generating analysis, please wait...";

    try {
        const response = await fetch('http://127.0.0.1:5000/generate-analysis', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        document.getElementById('result').innerHTML = data.analysis;

    } catch (error) {
        document.getElementById('result').innerHTML = "Error generating analysis. Ensure backend is running.";
    }
});
