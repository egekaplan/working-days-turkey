

<body>

<h1>Working Days Calculator</h1>
<p>This Python script calculates the total number of working days for each month in a given year, excluding weekends and holidays in Turkey.</p>

<h2>Prerequisites</h2>
<ul>
    <li>Python 3.x</li>
    <li><code>workalendar</code> library (install using <code>pip install workalendar</code>)</li>
</ul>

<h2>Usage</h2>
<ol>
    <li>Ensure you have Python 3.x installed on your system.</li>
    <li>Install the required library by running: <code>pip install workalendar</code></li>
    <li>Run the script using your preferred method (e.g., <code>python working-days-tr.py</code>).</li>
</ol>

<h2>Description</h2>
<p>The script utilizes the <code>workalendar</code> library to calculate the total number of working days for each month in the current year. It excludes weekends (Saturdays and Sundays) and considers holidays specific to Turkey.</p>

<h2>Adjustments</h2>
<p>To account for discrepancies in the holiday calendar, the script subtracts the 2nd of January as a holiday since it is not observed in Turkey, contrary to the information in the holiday calendar library.</p>

<h2>License</h2>
<p>This script is provided under the MIT License.</p>

</body>

</html>
