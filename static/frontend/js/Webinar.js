document.addEventListener("DOMContentLoaded", async function () {
    const urlParams = new URLSearchParams(window.location.search);
    const activityId = urlParams.get('id');

    // API'den activityId'ye göre etkinlik verisini al
    const response = await sendApiRequest('findOne', 'Activities', { '_id': detectIdType(activityId) });
    const activity = response;

    const upcomingWebinarSection = document.getElementById('upcomingWebinar');
    const pastWebinarSection = document.getElementById('pastWebinar');

    // Geçerli tarih ve etkinlik tarihini karşılaştır
    const currentDate = new Date();
    const activityDate = new Date(activity.DateTime);

    function froalaEdit(element) {
        var tempDiv = document.createElement('div');
        tempDiv.innerHTML = element;
    // Stil özniteliğine sahip tüm elementleri bul ve stil özniteliklerini temizle
    const elementsWithStyle = tempDiv.querySelectorAll('[style]');
    elementsWithStyle.forEach(el => {
        el.removeAttribute('style');
    });

    // `data-f-id="pbf"` özniteliğine sahip tüm `<p>` etiketlerini sil
    const paragraphsToRemove = tempDiv.querySelectorAll('p[data-f-id="pbf"]');
    paragraphsToRemove.forEach(p => {
        p.remove(); // `<p>` etiketini tamamen kaldır
    });
    
    return tempDiv.innerHTML;
    }
    
    // Resim ve içerik oluşturma fonksiyonu
    function createWebinarHTML(activity) {
        const webinarHTML = `
            <div class="row align-items-center">
                <div class="col-lg-6">
                    <img fetchpriority="high" decoding="async" width="626" height="367"
                        src="${activity.imageUrl}"
                        class="img-fluid image-fade-in"
                        alt="${activity.ActivityName}">
                </div>
                <div class="col-lg-6">
                    <h2 class="info-title">${activity.ActivityName}</h2>
                    <p class="info-text mb-4">${froalaEdit(activity.Content)}</p>
                    <ul class="info-subtitle list-unstyled mb-3">
                        <li>Konuşmacı: ${activity.ModName}</li>
                        <li>Tarih: ${activityDate.toLocaleDateString('tr-TR', {
                            year: 'numeric',
                            month: 'long',
                            day: 'numeric',
                        })} - ${activityDate.toLocaleTimeString('tr-TR', {
                            hour: '2-digit',
                            minute: '2-digit',
                        })}</li>
                    </ul>
                    <form id="registrationForm">
                        <div class="row">
                            <div class="col">
                                <label for="nameSurname" class="form-label">Ad Soyad</label>
                                <input type="text" class="form-control" id="nameSurname" required>
                            </div>
                            <div class="col">
                                <label for="phoneKayit" class="form-label">Telefon</label>
                                <input type="text" class="form-control" id="phoneKayit" required>
                            </div>
                            <div class="col">
                                <label for="emailKayit" class="form-label">Eposta</label>
                                <input type="text" class="form-control" id="emailKayit" required>
                            </div>
                        </div>
                        <div class="text mt-3">
                            ${activityDate > currentDate ? 
                            '<button type="submit" id="registerBtn" class="btn btn-primary">Kayıt Ol</button>' :
                            '<button type="button" class="btn btn-primary">Webinarı İzle</button>'}
                        </div>
                    </form>
                </div>
            </div>`;
        const faqSeo = document.getElementById('seo-card');
        faqSeo.innerHTML = activity.Seo ? froalaEdit(activity.Seo) : faqSeo.classList.add('d-none');
        return webinarHTML;
    }

    // Gelecek webinar mı yoksa geçmiş webinar mı olduğuna göre HTML'i ekle
    if (activityDate > currentDate) {
        upcomingWebinarSection.innerHTML = createWebinarHTML(activity);
    } else {
        pastWebinarSection.innerHTML = createWebinarHTML(activity);
    }

    $('#registrationForm').on('submit', async function (e) {
        e.preventDefault();
        const CourseName = group.Course.CourseName;
        const Name = $('#nameSurname').val();
        const Phone = $('#phoneKayit').val();
        const Email = $('#emailKayit').val()

        await fetch('https://api.talktoweb.com/PhpBack/mailSend.php', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                type: "webinar kayıt",
                name: Name,
                phone: Phone,
                courseName: CourseName,
                email:Email
            })
        });

        $('#registrationForm').trigger('reset');
    });

    // Görseller için fade-in efekti ekleme
    const images = document.querySelectorAll('.image-fade-in');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.classList.add('image-fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    images.forEach(image => {
        observer.observe(image);
    });
});