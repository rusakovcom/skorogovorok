const generateBtn = document.getElementById('generateBtn');
const resultPara = document.getElementById('result');

generateBtn.addEventListener('click', () => {
    fetch('list.txt')
        .then(response => response.text())
        .then(data => {
            const strings = data.trim().split('\n');
            const randomIndex = Math.floor(Math.random() * strings.length);
            const randomString = strings[randomIndex];
            resultPara.textContent = randomString;
        })
        .catch(error => {
            console.error('Error fetching list.txt:', error);
            resultPara.textContent = 'Error fetching random string.';
        });
});
