async function populateActivities() {
    const response = await sendApiRequest('find', 'Activities');
    const datas = response;

    const pastWebinarsContainer = document.querySelector('.past-webinars .row');
    const upcomingWebinarsContainer = document.querySelector('.upcoming-webinars .row');
    const today = new Date();

    let upcomingEventCount = 0;

    for (const data of datas) {
        const eventDate = new Date(data.DateTime); // Etkinlik tarihi
        const formattedName = formatName(data.ActivityName);

        // Geçmiş etkinlikler
        if (eventDate < today) {
            const pastWebinarHTML = `
                <div class="col-lg-3 col-md-6 mb-4">
                    <div class="card past-webinar-card">
                        <a href="{{ROOT}}/etkinlikler/${formattedName}" class="webinar-link" data-activity-id="${data._id}">
                            <img src="${data.imageUrl}" class="card-img-top" alt="${data.ActivityName}">
                        </a>
                        <div class="card-body">
                            <h6 class="card-title">${data.ActivityName}</h6>
                            <p class="card-text">Konuşmacı: ${data.ModName}</p>
                            <p class="card-text">Tarih: ${eventDate.toLocaleDateString()} - ${eventDate.toLocaleTimeString()}</p>
                            <div class="btn-wrapper">
                                <a href="{{ROOT}}/etkinlikler/${formattedName}" class="webinar-link btn btn-primary" data-activity-id="${data._id}">Webinara Git</a>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            pastWebinarsContainer.innerHTML += pastWebinarHTML; // Geçmiş webinarlar kısmına ekle
        } 
        // Yaklaşan etkinlikler
        else {
            const upcomingWebinarHTML = `
                <div class="col-lg-3 col-md-6 mb-4">
                    <div class="card upcoming-webinar-card">
                        <a href="{{ROOT}}/etkinlikler/${formattedName}" class="webinar-link" data-activity-id="${data._id}">
                            <img src="${data.imageUrl}" class="card-img-top" alt="${data.ActivityName}">
                        </a>
                        <div class="card-body">
                            <h6 class="card-title">${data.ActivityName}</h6>
                            <p class="card-text">Konuşmacı: ${data.ModName}</p>
                            <p class="card-text">Tarih: ${eventDate.toLocaleDateString()} - ${eventDate.toLocaleTimeString()}</p>
                            <div class="btn-wrapper">
                                <a href="{{ROOT}}/etkinlikler/${formattedName}" class="webinar-link btn btn-primary" data-activity-id="${data._id}">Ücretsiz Kayıt</a>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            upcomingWebinarsContainer.innerHTML += upcomingWebinarHTML;
            upcomingEventCount++;
        }
    }

    if (upcomingEventCount === 0) {
        const noUpcomingEventsHTML = `
            <h2 class='m-3'>Yaklaşan Etkinlik Yok, Takipte Kalın</h2>
        `;
        document.querySelector('.upcoming-webinars .row').innerHTML = noUpcomingEventsHTML;
    }

    // Tüm a etiketlerine click event ekle
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function(event) {
            const activityId = this.getAttribute('data-activity-id');
            event.preventDefault(); // Varsayılan davranışı durdur
                    const fullHref = `${link.href}?id=${activityId}`;
                    window.location.href = fullHref; // Güncellenmiş href ile yönlendirme
        });
    });
}


function formatName(courseName) {
        return courseName
            .toLowerCase() // Tüm harfleri küçük harfe çevir
            .replace(/ö/g, 'o') // Türkçe karakterleri dönüştür
            .replace(/ü/g, 'u')
            .replace(/ş/g, 's')
            .replace(/ç/g, 'c')
            .replace(/ı/g, 'i')
            .replace(/ğ/g, 'g')
            .replace(/[^a-z0-9\s]/g, '') // Özel karakterleri kaldır
            .replace(/\s+/g, '-') // Boşlukları '-' ile değiştir
            .trim(); // Baş ve sondaki boşlukları kaldır
    }


populateActivities()