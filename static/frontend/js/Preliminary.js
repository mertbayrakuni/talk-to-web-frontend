document.addEventListener('DOMContentLoaded', function () {
    const educationOptions = [
        'Grafik Tasarım Uzmanlığı',
        'UI / UX Tasarım Uzmanlığı',
        'Video Efekt Uzmanlığı',
        'Sketchup Ile Mimari Tasarım Uzmanlığı',
        'Sosyal Medya Uzmanlığı',
        'Web Tasarım ve Wordpress Uzmanlığı',
        'Front-End Developer',
        'Back-End Developer',
        'Mobile Developer',
        '.Net Core ve Python Eğitimleri'
    ];

    const adSourceOptions = [
        'Sosyal Medya Reklamları',
        'Google Reklamları',
        'Kişisel Tavsiye'
    ];

    function populateSelect(selectId, options) {
        const selectElement = document.getElementById(selectId);
        options.forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.textContent = option;
            selectElement.appendChild(opt);
        });
    }

    populateSelect('educationForm', educationOptions);
    populateSelect('adSourceForm', adSourceOptions);
});
