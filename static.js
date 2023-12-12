document.addEventListener('DOMContentLoaded', function () {
    const anomalyForm = document.getElementById('anomalyForm');
    const anomalyList = document.getElementById('anomalyList');

    anomalyForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const millType = document.getElementById('millType').value;
        const millOperation = document.getElementById('millOperation').value;
        const anomalyDescription = document.getElementById('anomalyDescription').value;

        // Dummy function to simulate adding a new anomaly to the list
        logAnomaly(millType, millOperation, anomalyDescription);
    });

    function logAnomaly(millType, millOperation, anomalyDescription) {
        // Dummy function to simulate logging an anomaly
        const listItem = document.createElement('li');
        listItem.textContent = `${millType.toUpperCase()} - ${millOperation} - ${anomalyDescription}`;
        anomalyList.appendChild(listItem);

        // Clear the form fields after logging the anomaly
        document.getElementById('millType').value = 'rodMill';
        document.getElementById('millOperation').value = '';
        document.getElementById('anomalyDescription').value = '';
    }
});
