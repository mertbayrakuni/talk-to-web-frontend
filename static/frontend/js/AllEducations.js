async function populateEducations() {
    try {
        const response = await sendApiRequest('groups');
        const data = response;

        const activeContainer = document.getElementById('ActiveCourses');
        const pastContainer = document.getElementById('PastCourses');

        // Kurs adını formatlayan fonksiyon
        function formatCourseName(courseName) {
            return courseName
                .toLowerCase()
                .replace(/ö/g, 'o').replace(/ü/g, 'u')
                .replace(/ş/g, 's').replace(/ç/g, 'c')
                .replace(/ı/g, 'i').replace(/ğ/g, 'g')
                .replace(/[^a-z0-9\s]/g, '')
                .replace(/\s+/g, '-')
                .trim();
        }

        // Tekrarlanan click işlemlerini ayrı bir fonksiyona al
        function addClickListener(link, groupId) {
            link.addEventListener('click', function () {
                event.preventDefault(); // Varsayılan davranışı durdur
                const fullHref = `${link.href}?id=${groupId}`;
                window.location.href = fullHref;
            });
        }

        // Kart oluşturan fonksiyon
        function createCard(item, container) {
            const colDiv = document.createElement('div');
            colDiv.className = 'col-lg-3 col-md-6';

            const cardDiv = document.createElement('div');
            cardDiv.className = 'card shadow-lg h-100 course-card';

            const cardLink = document.createElement('a');
            const formattedCourseName = formatCourseName(item.Course.CourseName || 'egitimler');
            cardLink.href = `{{ROOT}}/egitimler/${formattedCourseName}`;
            addClickListener(cardLink, item._id);

            const imgContainer = document.createElement('div');
            imgContainer.className = 'card-img-container';

            const img = document.createElement('img');
            img.src = item.Course.Img || 'https://via.placeholder.com/150';
            img.className = 'card-img-top img-fluid';
            img.alt = item.title || 'Kurs Resmi';

            imgContainer.appendChild(img);
            cardLink.appendChild(imgContainer);

            const cardBody = document.createElement('div');
            cardBody.className = 'card-body';

            const cardTitle = document.createElement('h6');
            cardTitle.className = 'card-title';

            const titleLink = document.createElement('a');
            titleLink.href = `{{ROOT}}/egitimler/${formattedCourseName}`;
            titleLink.className = 'text-decoration-none text-primary';
            titleLink.textContent = item.Course.CourseName || 'Eğitim Başlığı';
            addClickListener(titleLink, item._id);

            cardTitle.appendChild(titleLink);
            cardBody.appendChild(cardTitle);

            cardDiv.appendChild(cardLink);
            cardDiv.appendChild(cardBody);
            colDiv.appendChild(cardDiv);

            container.appendChild(colDiv);
        }

        // Verileri işle ve kartları oluştur
        data.forEach(item => {
            if (item._id === 0) return;

            const container = item.Open ? activeContainer : pastContainer;
            createCard(item, container);
        });

    } catch (error) {
        console.error('Error populating education cards:', error);
    }
}

// Sayfa yüklenince fonksiyonu çağır
populateEducations();
